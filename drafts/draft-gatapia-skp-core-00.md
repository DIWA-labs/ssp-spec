---
title: "Semantic State Protocol (SKP) Core Specification"
abbrev: "SKP Core"
docname: draft-gatapia-skp-core-00
category: exp
ipr: trust200902
area: Applications and Real-Time
workgroup: Independent Submission
stand_alone: yes
author:
  - ins: R. Gatapia
    name: Ramulus Gatapia
    organization: Independent
date: 2026-08-06
---

# Abstract

Semantic State Protocol (SKP) defines a transport-independent semantic envelope for exchanging references to identity, action, relationship, transition, reach, payload, result, and provenance across heterogeneous systems. It is designed to accompany existing documents, source code, workflow messages, agent communication, simulation events, and knowledge objects without replacing their native formats.

# Status of This Memo

This document is an experimental individual draft. It has not been adopted by an IETF working group and is not an RFC.

# 1. Introduction

Modern software systems exchange related information through incompatible representations. Source repositories identify symbols by paths and ranges. Documents use headings, citations, and links. Workflow engines use tasks and state names. AI agents exchange natural-language instructions and tool outputs. Simulations store entity changes in runtime-specific structures.

These representations often refer to the same underlying object, event, or decision, but identity, transition, reach, and provenance are lost or reconstructed through custom adapters.

SKP defines a common semantic envelope. It does not prescribe storage, transport, execution, ontology, AI reasoning, or user-interface behavior.

# 2. Conventions and Terminology

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY indicate requirement levels.

Terms are defined in `docs/terminology.md` in the source repository. Publication versions should inline those definitions.

# 3. Problem Statement

Interoperability is commonly achieved through pairwise adapters:

~~~
Document <-> Agent
Agent <-> Workflow
Workflow <-> Repository
Repository <-> Knowledge Graph
~~~

As the number of systems grows, the number of translations and opportunities for semantic loss grows. A shared envelope reduces the need to infer identity, action, transition, and provenance from unstructured payloads.

# 4. Design Goals

SKP is intended to be:

- transport-independent;
- implementation-neutral;
- profile-extensible;
- provenance-aware;
- safe to parse;
- compact enough for routine exchange;
- readable in its text form.

# 5. Non-Goals

SKP Core does not define:

- domain ontologies;
- AI reasoning;
- embeddings;
- workflow execution;
- storage engines;
- application-specific kernels;
- user interfaces;
- authorization policy.

# 6. Abstract Data Model

An SKP packet consists of:

- protocol version;
- packet identifier;
- profile identifier;
- semantic address;
- action;
- subject;
- optional object;
- optional transition;
- reach;
- optional payload;
- optional result;
- provenance;
- extensions.

# 7. Core Fields

The normative field definitions are maintained in `SPEC.md` for draft-00 and are intended to be incorporated verbatim into the next rendered draft revision.

# 8. Processing Model

A processor:

1. decodes the transport representation;
2. performs Core validation;
3. identifies the profile;
4. performs profile validation;
5. applies local policy;
6. processes or forwards the packet;
7. preserves unknown extensions when forwarding.

# 9. Versioning

Draft-00 uses `1.0-draft`. Unsupported major versions MUST be rejected unless explicit pass-through behavior preserves the packet.

# 10. Profiles

Profiles constrain tokens and add domain rules. Profiles MUST NOT reinterpret Core fields.

# 11. Security Considerations

Packets and payloads are untrusted. Implementations MUST impose size and nesting limits, reject duplicate object keys, avoid implicit URI dereferencing, and separate provenance from authentication.

# 12. Privacy Considerations

Packets may reveal identity, relationships, actions, and provenance. Producers SHOULD minimize personal data and select the smallest appropriate reach.

# 13. IANA Considerations

This document requests no IANA actions.

# 14. Implementation Status

The source repository includes preliminary Python, Rust, and C# implementations and machine-readable test vectors. These implementations are non-normative.

# 15. References

## 15.1 Normative References

No external normative references are fixed in draft-00.

## 15.2 Informative References

Future revisions should add references for requirement language, URI syntax, JSON, timestamps, and security guidance after formal review.
