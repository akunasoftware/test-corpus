# Fixture Rules

This directory contains semi-realistic content fixtures for extraction and file-type tests.
Local `AGENTS.md` files are maintenance instructions, not test fixtures.

## Expected Snippets

- `code.*` files contain `extraction fixture marker: shared code sample` exactly once.
- `text.*` files contain `life is but an instant; his substance` exactly once.
- Exceptions require matching manual test setup.

Place expected snippets in normal body content.
For source/config files, use a string value, record field, query value, or similar natural content.
Avoid putting expected snippets in comments, titles, filenames, metadata, or obvious top-level locations.

## Fixture Shape

Use one fixture per extension unless tests intentionally cover multiple content types for the same extension.

Keep fixtures realistic and representative:

- enough structure to exercise real parsers
- multiple sections, records, blocks, or nested elements where natural
- normal imports, declarations, functions, or records for source code
- moderate size; avoid tiny one-line fixtures unless the format is normally tiny

Use valid syntax for structured formats like XML, XHTML, RSS, YAML, TOML, and source code.
Do not use runtimes, compilers, LSPs, formatters, linters, or parser tools to validate fixtures.
Validate syntax by eye only.

Avoid external URLs unless the format needs one.
Avoid secrets, credentials, personal data, and excessive cleverness.
