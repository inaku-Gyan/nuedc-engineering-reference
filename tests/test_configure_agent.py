from __future__ import annotations

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from configure_agent import (
    AgentConfiguration,
    ConfigurationError,
    PolicyGenerator,
    main,
    run_interactive,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
POLICY_DIR = REPO_ROOT / "agent-policy"
PRESET_NAMES = ("readonly", "curate-on-use", "autonomous", "maintainer")


class PolicyGeneratorTests(unittest.TestCase):
    def make_generator(self) -> tuple[tempfile.TemporaryDirectory[str], PolicyGenerator]:
        temporary = tempfile.TemporaryDirectory()
        generator = PolicyGenerator(Path(temporary.name), POLICY_DIR)
        return temporary, generator

    def test_all_presets_render_without_runtime_mode_names(self) -> None:
        configs = (
            AgentConfiguration("readonly", False, False),
            AgentConfiguration("curate-on-use", False, False),
            AgentConfiguration("autonomous", True, False),
            AgentConfiguration("maintainer", True, True),
        )
        limits = (2048, 3072, 4096, 4608)
        for config, limit in zip(configs, limits, strict=True):
            with self.subTest(preset=config.preset):
                prompt = PolicyGenerator(REPO_ROOT).render(config)
                self.assertLessEqual(len(prompt.encode("utf-8")), limit)
                self.assertNotIn(".agent-mode", prompt)
                for name in PRESET_NAMES:
                    self.assertNotIn(name, prompt)

    def test_capabilities_are_composed_for_selected_configuration(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        readonly = generator.render(
            AgentConfiguration("readonly", False, False)
        )
        autonomous = generator.render(
            AgentConfiguration("autonomous", False, False)
        )
        maintainer = generator.render(
            AgentConfiguration("maintainer", True, False)
        )

        self.assertIn("Treat this repository as read-only", readonly)
        self.assertNotIn("Filling relevant knowledge gaps", readonly)
        self.assertIn("Filling relevant knowledge gaps", autonomous)
        self.assertIn("Leave repository edits in the working tree", autonomous)
        self.assertIn("Repository maintenance", maintainer)
        self.assertIn("create a local commit", maintainer)
        self.assertIn("Do not", maintainer)
        self.assertIn("or push.", maintainer)

    def test_invalid_git_combinations_are_rejected(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        base = {
            "schema_version": 1,
            "preset": "autonomous",
            "git": {"auto_commit": False, "auto_push": True},
        }
        with self.assertRaises(ConfigurationError):
            generator.parse_configuration(base)

        base["preset"] = "readonly"
        base["git"] = {"auto_commit": True, "auto_push": False}
        with self.assertRaises(ConfigurationError):
            generator.parse_configuration(base)

    def test_unknown_fields_are_rejected(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        with self.assertRaises(ConfigurationError):
            generator.parse_configuration(
                {
                    "schema_version": 1,
                    "preset": "readonly",
                    "git": {"auto_commit": False, "auto_push": False},
                    "extra": True,
                }
            )

    def test_unknown_schema_is_rejected(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        with self.assertRaises(ConfigurationError):
            generator.parse_configuration(
                {
                    "schema_version": 99,
                    "preset": "readonly",
                    "git": {"auto_commit": False, "auto_push": False},
                }
            )

    def test_write_rolls_back_both_files_when_second_replace_fails(self) -> None:
        temporary, generator = self.make_generator()
        self.addCleanup(temporary.cleanup)
        generator.config_path.write_text("old config\n", encoding="utf-8")
        generator.prompt_path.write_text("old prompt\n", encoding="utf-8")
        calls = 0

        def fail_second(source: Path, destination: Path) -> None:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated failure")
            os.replace(source, destination)

        with self.assertRaises(OSError):
            generator.write(
                AgentConfiguration("maintainer", True, False),
                replace=fail_second,
            )
        self.assertEqual(
            generator.config_path.read_text(encoding="utf-8"), "old config\n"
        )
        self.assertEqual(
            generator.prompt_path.read_text(encoding="utf-8"), "old prompt\n"
        )

    def test_check_detects_matching_and_stale_prompt(self) -> None:
        temporary, generator = self.make_generator()
        self.addCleanup(temporary.cleanup)
        config = AgentConfiguration("autonomous", True, False)
        generator.write(config)
        self.assertEqual(
            generator.check(), (True, "配置和 KNOWLEDGE_AGENT.md 一致")
        )

        generator.prompt_path.write_text("stale\n", encoding="utf-8")
        valid, message = generator.check()
        self.assertFalse(valid)
        self.assertIn("不一致", message)

    def test_check_reports_missing_configuration(self) -> None:
        temporary, generator = self.make_generator()
        self.addCleanup(temporary.cleanup)
        valid, message = generator.check()
        self.assertFalse(valid)
        self.assertIn("未找到", message)

    def test_cancelled_interaction_does_not_write_files(self) -> None:
        temporary, generator = self.make_generator()
        self.addCleanup(temporary.cleanup)
        with patch("builtins.input", side_effect=["1", "n"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(run_interactive(generator), 1)
        self.assertFalse(generator.config_path.exists())
        self.assertFalse(generator.prompt_path.exists())

    def test_invalid_configuration_is_preserved_until_confirmation(self) -> None:
        temporary, generator = self.make_generator()
        self.addCleanup(temporary.cleanup)
        invalid = '{"schema_version": 99}\n'
        generator.config_path.write_text(invalid, encoding="utf-8")
        with patch("builtins.input", side_effect=["1", "n"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(run_interactive(generator), 1)
        self.assertEqual(
            generator.config_path.read_text(encoding="utf-8"), invalid
        )
        self.assertFalse(generator.prompt_path.exists())

    def test_serialized_configuration_is_valid_json(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        config = AgentConfiguration("maintainer", True, False)
        raw = json.loads(generator.serialized_configuration(config))
        self.assertEqual(generator.parse_configuration(raw), config)

    def test_generated_prompt_uses_knowledge_specific_filename(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        self.assertEqual(generator.prompt_path.name, "KNOWLEDGE_AGENT.md")

    def test_parent_integration_prompt_substitutes_normalized_path(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        prompt = generator.render_integration_prompt(
            r"third_party\nuedc-reference\\", "parent"
        )
        self.assertIn("`third_party/nuedc-reference`", prompt)
        self.assertNotIn("<NUEDC_REFERENCE_PATH>", prompt)
        self.assertIn("catalog/README.md", prompt)

    def test_user_integration_prompt_is_available_without_local_config(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        prompt = generator.render_integration_prompt("vendor/reference", "user")
        self.assertIn("本任务需要查阅", prompt)
        self.assertIn("`vendor/reference`", prompt)

    def test_both_integration_prompts_have_copyable_sections(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        prompt = generator.render_integration_prompt("refs/nuedc", "both")
        self.assertIn("# Parent AGENTS.md snippet", prompt)
        self.assertIn("# One-off user prompt", prompt)

    def test_integration_prompt_rejects_unsafe_path(self) -> None:
        generator = PolicyGenerator(REPO_ROOT)
        for path in ("", "refs/`injected`", "refs/\nother"):
            with self.subTest(path=path):
                with self.assertRaises(ConfigurationError):
                    generator.render_integration_prompt(path)

    def test_cli_prints_integration_prompt_without_writing(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(
                main(
                    [
                        "--print-integration-prompt",
                        "third_party/nuedc-reference",
                        "--prompt-kind",
                        "user",
                    ]
                ),
                0,
            )
        self.assertIn("third_party/nuedc-reference", output.getvalue())

    def test_cli_writes_beside_script_not_current_working_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_name:
            temporary = Path(temporary_name)
            script_root = temporary / "knowledge-repository"
            caller_root = temporary / "caller"
            script_root.mkdir()
            caller_root.mkdir()
            shutil.copy2(REPO_ROOT / "configure_agent.py", script_root)
            shutil.copytree(POLICY_DIR, script_root / "agent-policy")

            result = subprocess.run(
                [sys.executable, str(script_root / "configure_agent.py")],
                cwd=caller_root,
                input="1\ny\n",
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((script_root / ".agent-mode.json").is_file())
            self.assertTrue((script_root / "KNOWLEDGE_AGENT.md").is_file())
            self.assertFalse((caller_root / ".agent-mode.json").exists())
            self.assertFalse((caller_root / "KNOWLEDGE_AGENT.md").exists())


if __name__ == "__main__":
    unittest.main()
