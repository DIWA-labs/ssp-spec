# Implementation Guide

## Validation order

1. Decode JSON with duplicate-key detection.
2. Validate required Core fields.
3. Validate URI syntax.
4. Validate address, entity, transition, payload, provenance, and extensions.
5. Resolve the declared profile.
6. Apply profile rules.
7. Apply local authorization and privacy policy.

## Storage

Store the original packet when possible. Parsed database columns are indexes, not replacements for the authoritative serialized packet.

## Forwarding

Unknown extension fields should be preserved. Do not silently normalize profile-defined opaque coordinates.

## Logging

Log validation errors without copying sensitive payload data unnecessarily.

## Testing

Use:

- valid vectors;
- invalid vectors;
- canonicalization vectors;
- round-trip tests;
- cross-language interoperability tests;
- size and malformed-input tests.
