# Governance

## Draft-00 governance

Ramulus Gatapia is the initial editor of SSP draft-00. This role controls repository publication but does not make unreviewed implementation behavior normative.

## Sources of authority

In descending order:

1. The latest published numbered draft under `drafts/`.
2. `SPEC.md`, when synchronized with that draft.
3. JSON Schemas and conformance vectors.
4. Reference implementations.
5. Examples and discussion documents.

If these conflict, the numbered draft controls and the conflict MUST be filed as an issue.

## Decisions

Protocol-affecting decisions are recorded in `discussions/` or a future `decisions/` directory. A decision should state:

- problem;
- constraints;
- alternatives;
- compatibility impact;
- security and privacy impact;
- selected resolution;
- test evidence.

## Profiles

Profiles may define domain vocabularies and constraints but MUST NOT reinterpret SSP Core fields. Immutable external kernels should be referenced by profile identifier and specification version rather than copied or redefined.

## Publication

GitHub publication does not constitute IETF approval, an RFC, or a standards-track designation.
