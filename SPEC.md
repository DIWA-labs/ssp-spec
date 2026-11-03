# Semantic State Protocol (SSP) Infrastructure

**Version:** 1.0-draft  
**Repository release:** 0.0.0-draft.00  
**Status:** Experimental

## 1. Abstract

Semantic State Protocol (SSP) defines a transport-independent semantic envelope for exchanging references to identity, action, relationship, state transition, reach, payload, result, and provenance across heterogeneous systems. SSP does not replace documents, source code, workflow messages, databases, or application-specific kernels. It provides a common envelope that can accompany them.

## 2. Introduction

Modern systems exchange related information through incompatible representations. A source repository identifies a symbol with a path and line range. A document system refers to a heading or citation. A workflow engine uses task identifiers and state names. An AI agent often receives natural-language instructions and tool results. A simulation records entity changes in runtime-specific structures.

Although these systems may refer to the same object, event, or decision, the relationship is frequently reconstructed through custom adapters or inferred from unstructured text. Identity can be lost when content moves between systems. State transitions may be recorded without their subject, cause, reach, or provenance. Agent messages may report a change without a durable link to the file, task, evidence, or runtime event that motivated it.

SSP addresses this interoperability problem by defining a common semantic envelope. The envelope can identify the relevant semantic space, locate an object within that space, state an action or relationship, identify the subject and object, describe a transition, constrain its reach, carry an optional payload and result, and retain provenance.

SSP is complementary to existing serialization, transport, version-control, workflow, and knowledge-graph technologies. It does not prescribe storage, execution, reasoning, ontology, user interface, or transport behavior.

## 3. Terminology

- **Packet:** One SSP envelope.
- **Producer:** A system that emits a packet.
- **Consumer:** A system that reads a packet.
- **Processor:** A producer, consumer, validator, forwarder, or transformer.
- **Profile:** A named specification that constrains values or adds domain semantics without redefining Core fields.
- **Semantic address:** A space name and ordered coordinate sequence.
- **Subject:** The primary entity performing, holding, or undergoing the action.
- **Object:** An optional secondary entity related to the subject.
- **Transition:** An optional before/after state pair.
- **Reach:** The declared scope in which the packet is intended to apply.
- **Extension:** A namespaced, non-Core value.

## 4. Conformance language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate requirement levels.

## 5. Core packet model

A draft-00 packet contains:

| Field | Required | Meaning |
|---|---:|---|
| `ssp` | yes | Protocol version identifier. |
| `id` | yes | Globally unique packet identifier. |
| `profile` | yes | Profile identifier. |
| `semantic_address` | yes | Semantic space and ordered coordinates. |
| `action` | yes | Profile-defined action token. |
| `subject` | yes | Primary entity reference. |
| `object` | no | Secondary entity reference. |
| `transition` | no | Before/after state description. |
| `reach` | yes | Scope token. |
| `payload` | no | Typed data or reference. |
| `result` | no | Processing or domain result. |
| `provenance` | yes | Producer and creation time. |
| `extensions` | yes | Namespaced extension map; empty object permitted. |

## 6. Protocol version

Draft-00 uses:

```json
"ssp": "1.0-draft"
```

A processor MUST reject a packet whose major version it does not support, unless operating in explicit pass-through mode. A pass-through processor MUST preserve the original packet bytes or all unknown fields.

## 7. Packet identifier

`id` MUST be a URI. UUID URNs are RECOMMENDED for generated packet identifiers.

Packet identity is distinct from subject and object identity.

## 8. Profile identifier

`profile` MUST be a URI. Profiles MUST NOT redefine the meaning of a Core field. Profiles MAY:

- restrict allowed `space`, `action`, `reach`, type, or transition tokens;
- require optional fields;
- define extension namespaces;
- define domain validation rules;
- map an immutable external kernel specification into SSP without altering that kernel.

## 9. Semantic address

```json
"semantic_address": {
  "space": "document",
  "coordinates": ["manual.md", "section-2"]
}
```

`space` MUST be a non-empty token. `coordinates` MUST be a non-empty ordered array of strings.

Core does not assign meaning to coordinate positions. The active profile does.

## 10. Entity references

A subject or object has:

```json
{"id": "urn:example:entity:1", "type": "claim", "label": "Optional display label"}
```

- `id` MUST be a URI.
- `type` MUST be a non-empty profile-defined token.
- `label` MAY be present but MUST NOT be used as canonical identity.

## 11. Action

`action` is a profile-defined token describing the relationship, operation, or observation represented by the packet.

A consumer MUST NOT infer action semantics solely from natural-language payload text when an action token is present.

## 12. Transition

```json
"transition": {"from": "proposed", "to": "supported"}
```

At least one of `from` or `to` MUST be present. Values are profile-defined strings or `null`.

## 13. Reach

Draft-00 recommends the following Core-neutral tokens:

- `local`
- `project`
- `organization`
- `network`
- `global`
- `private`

Profiles MAY restrict this set. `reach` does not by itself grant authorization.

## 14. Payload

A payload is either inline data or an external reference.

Inline:

```json
{"media_type": "application/json", "value": {"confidence": 0.82}}
```

Referenced:

```json
{
  "media_type": "text/markdown",
  "ref": "urn:example:document:17",
  "digest": {"algorithm": "sha-256", "value": "HEX"}
}
```

A payload MUST contain exactly one of `value` or `ref`.

Processors MUST treat payloads as untrusted input.

## 15. Result

`result` is an object describing processing or domain outcome. Draft-00 defines only the optional `status` token. Profiles MAY add fields.

## 16. Provenance

```json
{
  "producer": "urn:example:agent:reviewer",
  "created_at": "2026-08-06T17:00:00Z",
  "source": "urn:example:task:44"
}
```

- `producer` MUST be a URI.
- `created_at` MUST use RFC 3339-style UTC timestamp syntax ending in `Z` in draft-00.
- `source` MAY identify the originating task, event, message, or artifact.

Provenance describes origin; it does not establish truth or trust.

## 17. Extensions

`extensions` MUST be an object. Extension keys MUST be URI strings or reverse-domain names.

Example:

```json
"extensions": {
  "org.example.review": {"severity": "warning"}
}
```

Processors SHOULD preserve unknown extensions.

## 18. Text serialization

Draft-00 uses UTF-8 JSON. See `drafts/draft-gatapia-ssp-text-00.md`.

## 19. Validation

A conforming validator MUST detect:

- missing required fields;
- unknown or malformed major version;
- non-URI identifiers;
- empty address coordinate arrays;
- payloads containing both `value` and `ref`;
- transitions containing neither `from` nor `to`;
- non-object `extensions`.

Profile validation occurs after Core validation.

## 20. Error identifiers

Draft-00 defines:

- `SSP_REQUIRED_FIELD`
- `SSP_UNSUPPORTED_VERSION`
- `SSP_INVALID_URI`
- `SSP_INVALID_ADDRESS`
- `SSP_INVALID_ENTITY`
- `SSP_INVALID_TRANSITION`
- `SSP_INVALID_PAYLOAD`
- `SSP_INVALID_PROVENANCE`
- `SSP_INVALID_EXTENSIONS`
- `SSP_PROFILE_VIOLATION`

## 21. Security considerations

Processors MUST:

- impose input-size and nesting limits;
- reject duplicate JSON object keys;
- avoid executing payload content during parsing;
- treat labels and payload text as untrusted;
- prevent URI dereferencing unless explicitly authorized;
- distinguish provenance from authentication.

Signatures and trust policy are deferred to a separate profile.

## 22. Privacy considerations

SSP packets can expose identity, relationships, actions, and provenance. Producers SHOULD minimize personal information, use pseudonymous identifiers when appropriate, and avoid global reach where a smaller scope is sufficient.

## 23. IANA considerations

Draft-00 requests no IANA action.

## 24. Non-goals

SSP Core does not define:

- AI reasoning;
- embeddings;
- ontologies;
- workflow execution;
- database schemas;
- user-interface behavior;
- immutable application-kernel meanings;
- a binary format;
- authorization policy.

## 25. Open issues

See `discussions/`.
