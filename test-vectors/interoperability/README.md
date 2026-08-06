# Interoperability vectors

Each implementation should:

1. validate all files listed in `../valid/index.json`;
2. reject all files listed in `../invalid/index.json` with the expected error category;
3. serialize `../canonical/input.json` to the bytes in `../canonical/expected.json`;
4. parse and re-emit every example without changing Core field values;
5. preserve unknown extension members.
