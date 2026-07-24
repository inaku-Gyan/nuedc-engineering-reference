## NUEDC engineering knowledge base

`<NUEDC_REFERENCE_PATH>` is an Agent-oriented NUEDC engineering reference repository, not project
source code. It curates official manuals, datasheets, and other originals (usually PDFs) alongside
selective extracts, concise summaries, metadata, indexes, and source links. Its purpose is to help
Agents locate and verify reusable hardware and toolchain facts without loading whole documents.

Consult it only when the task involves NUEDC, electronic components, development boards,
instruments, embedded toolchains, hardware design, measurement, or debugging:

1. If `<NUEDC_REFERENCE_PATH>/KNOWLEDGE_AGENT.md` exists, read and follow it before using or
   changing the knowledge base.
2. If that file is missing, treat the knowledge base as read-only, start from
   `<NUEDC_REFERENCE_PATH>/catalog/README.md`, and tell the user to run
   `python <NUEDC_REFERENCE_PATH>/configure_agent.py` before any knowledge-base update.
3. Follow catalog links to a package `README.md` and `meta.yaml`; read focused extracts
   next and open original PDFs only when exact verification is necessary.
4. Cite repository-relative paths and original document pages/chapters for exact claims.
5. Keep project-specific decisions in this business repository. Put only reusable
   engineering knowledge in the reference repository.

Do not preload or scan the knowledge base for unrelated tasks.
