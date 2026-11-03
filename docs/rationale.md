# Rationale

## Why an envelope?

Replacing every native format would be unrealistic. An envelope allows semantic identity and provenance to travel with existing content.

## Why profiles?

Documents, code, AI agents, workflows, and simulations need different vocabularies. Profiles permit those vocabularies without making Core domain-specific.

## Why explicit subject and object?

Natural-language statements often obscure which entity acted and which entity was affected. Explicit references improve interoperability and validation.

## Why provenance?

A packet can be syntactically valid but untrustworthy. Provenance preserves origin while leaving authentication and trust policy to separate mechanisms.

## Why not embeddings?

Embeddings are useful indexes but are model-dependent and not stable semantic identifiers. SSP may reference embeddings through profiles, but Core does not treat them as authoritative meaning.
