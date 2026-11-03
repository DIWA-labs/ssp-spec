# Semantic State Protocol (SSP)

> **Status:** Experimental public draft. This repository is not an IETF standard and has not been assigned an RFC number.

Semantic State Protocol (SSP) is a transport-independent semantic envelope for exchanging references to identity, action, relationship, transition, reach, payload, result, and provenance across heterogeneous systems.

The initial problem is simple: documents, source code, AI agents, workflows, simulations, and knowledge systems frequently refer to the same underlying objects and events using incompatible internal representations. SSP provides a small shared envelope that can accompany existing content without replacing the content, storage system, or transport.

## Repository map

- [`SPEC.md`](SPEC.md) — current working specification.
- [`drafts/draft-diwa-ssp-core-00.md`](drafts/draft-diwa-ssp-core-00.md) — Internet-Draft-style core document.
- [`drafts/draft-diwa-ssp-text-00.md`](drafts/draft-diwa-ssp-text-00.md) — provisional JSON text encoding.
- [`drafts/draft-diwa-ssp-profiles-00.md`](drafts/draft-diwa-ssp-profiles-00.md) — profile mechanism.
- [`schemas/`](schemas/) — JSON Schemas for draft-00 packets and profiles.
- [`examples/`](examples/) — examples for documents, code, agents, workflows, and simulations.
- [`test-vectors/`](test-vectors/) — valid, invalid, canonicalization, and interoperability vectors.
- [`reference/`](reference/) — small reference implementations in Python, Rust, and C#.
- [`docs/`](docs/) — terminology, rationale, FAQ, and implementation guidance.
- [`discussions/`](discussions/) — open design questions requiring public review.

## Draft-00 packet

```json
{
  "ssp": "1.0-draft",
  "id": "urn:uuid:11111111-1111-4111-8111-111111111111",
  "profile": "urn:ssp:profile:core",
  "semantic_address": {
    "space": "document",
    "coordinates": ["manual.md", "section-2"]
  },
  "action": "references",
  "subject": {"id": "urn:example:claim:17", "type": "claim"},
  "object": {"id": "urn:example:evidence:9", "type": "evidence"},
  "transition": {"from": "proposed", "to": "supported"},
  "reach": "local",
  "payload": {"media_type": "application/json", "value": {"confidence": 0.82}},
  "result": {"status": "recorded"},
  "provenance": {
    "producer": "urn:example:agent:reviewer",
    "created_at": "2026-08-06T17:00:00Z"
  },
  "extensions": {}
}
```

Draft-00 intentionally leaves domain semantics to profiles. It does **not** redefine DNL, TAO, VNF, AWSP, LIK, DIWA, or any other application-specific kernel.

## Quick validation

Python 3.11+:

```bash
cd reference/python
python -m unittest discover -s tests
```

The Python implementation validates the bundled examples using only the standard library. JSON Schema files are supplied for integrations that use a schema validator.

## Design principles

1. **Envelope, not replacement.** SSP accompanies existing content.
2. **Transport independence.** It may be stored in files, databases, messages, or event streams.
3. **Profile separation.** Core syntax is independent of domain vocabularies.
4. **Explicit provenance.** Producers and creation time can be retained.
5. **Forward-compatible extensions.** Unknown extensions are preserved where possible.
6. **Implementation neutrality.** No particular database, AI model, language, or UI is required.

## Current limitations

Draft-00 is suitable for experimentation, not production standardization. Open issues include canonical numeric representation, registry governance, signatures, privacy minimization, binary encoding, and formal treatment of immutable kernel profiles.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`GOVERNANCE.md`](GOVERNANCE.md), and the files under [`discussions/`](discussions/).

## License

Repository source code and documentation are available under the Apache License. Standards bodies or publication streams may require separate contribution terms.
