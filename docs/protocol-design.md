# Protocol Design Notes

The draft separates four layers:

1. **Core abstract model**
2. **Text encoding**
3. **Profiles**
4. **Application integration**

This prevents application behavior from becoming accidental protocol law.

A packet is intentionally event-neutral. It may represent an observation, command, relationship, transition, evidence link, or indexing record depending on the profile.

Open design pressure exists between compactness and explicitness. Draft-00 favors explicit JSON fields. A future compact or binary encoding should be derived only after stable semantics and interoperability tests exist.
