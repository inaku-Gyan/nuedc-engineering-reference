## NUEDC engineering knowledge base

An Agent-oriented NUEDC engineering reference repository is available at `<NUEDC_REFERENCE_PATH>`.
It curates official manuals, datasheets, and other originals (usually PDFs) alongside
selective extracts, concise summaries, metadata, indexes, and source links. Its purpose is to help
Agents locate and verify reusable hardware and toolchain facts.

Consult it only when the task involves NUEDC, electronic components, development boards,
instruments, embedded toolchains, hardware design, measurement, or debugging:

1. If `<NUEDC_REFERENCE_PATH>/KNOWLEDGE_AGENT.md` exists, read and follow it before using or
   changing the knowledge base.
2. If that file is missing, treat the knowledge base as read-only, start from
   `<NUEDC_REFERENCE_PATH>/catalog/README.md`, and tell the user to run
   `python <NUEDC_REFERENCE_PATH>/configure_agent.py` before any knowledge-base update.
   next and open original PDFs only when exact verification is necessary.
3. Keep project-specific decisions in this business repository. Put only reusable
   engineering knowledge in the reference repository.

Do not preload or scan the knowledge base for unrelated tasks.
