# SKP JSON Text Encoding — Draft 00

## Status

Experimental companion draft.

## Encoding

Packets are encoded as UTF-8 JSON objects.

## Required object keys

`skp`, `id`, `profile`, `semantic_address`, `action`, `subject`, `reach`, `provenance`, and `extensions`.

## Parser requirements

A parser MUST:

- reject duplicate keys;
- reject invalid UTF-8;
- reject trailing non-whitespace data;
- enforce configured depth and size limits;
- preserve unknown extension members.

## Provisional canonical form

Canonical hashing is not final in draft-00. For repository test vectors, the provisional form is:

1. UTF-8;
2. object keys sorted lexicographically by Unicode code point;
3. no insignificant whitespace;
4. strings encoded using JSON escaping;
5. arrays retain order;
6. numbers use the shortest JSON representation produced by the reference implementation;
7. a single trailing line feed is permitted in files but excluded from the canonical digest.

Because cross-language numeric formatting may differ, profiles requiring signatures SHOULD avoid floating-point numbers until canonical numeric rules are finalized.

## Media type

No media type registration is requested in draft-00. Implementations MAY use `application/json` with an out-of-band SKP profile declaration.
