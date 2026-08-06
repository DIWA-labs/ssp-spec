# SKP Profile Mechanism — Draft 00

## Purpose

SKP Core defines a shared envelope. Profiles define domain vocabularies and additional constraints.

## Profile requirements

A profile specification MUST publish:

- a stable URI identifier;
- version;
- allowed semantic spaces;
- coordinate meanings;
- allowed actions;
- subject and object types;
- transition values;
- reach restrictions;
- required optional fields;
- extension namespaces;
- profile validation rules;
- examples and test vectors.

A profile MUST NOT redefine Core field meanings.

## Immutable kernels

When a profile maps an immutable external kernel, it MUST:

1. identify the kernel specification and version;
2. treat kernel coordinates as opaque or exactly defined by that specification;
3. avoid renaming axes or inventing additional axes;
4. place application interpretation outside SKP Core;
5. include round-trip vectors proving that encoding and decoding preserve the original kernel value.

## Compatibility

A packet declares one primary profile. Additional compatible profile identifiers MAY be listed in a profile-defined extension until Core defines a multi-profile mechanism.
