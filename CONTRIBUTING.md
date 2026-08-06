# Contributing to SKP

SKP is an experimental protocol. Contributions should improve interoperability without silently expanding the meaning of the core.

## Ways to contribute

- Report ambiguity or contradictions.
- Add valid and invalid test vectors.
- Implement an independent parser.
- Propose a profile without modifying SKP Core.
- Identify security, privacy, or canonicalization defects.
- Provide interoperability reports from two independent implementations.

## Contribution rules

1. Open an issue before making a protocol-breaking pull request.
2. Distinguish editorial changes from semantic changes.
3. Add or update test vectors for every normative change.
4. Do not redefine application-specific kernels in SKP Core.
5. Preserve unknown extension fields unless the specification explicitly permits dropping them.
6. Mark unresolved design questions as `OPEN ISSUE`; do not conceal them behind implementation behavior.
7. Include validation evidence in the pull request description.

## Pull request checklist

- [ ] Scope is stated.
- [ ] Normative text uses MUST, MUST NOT, SHOULD, SHOULD NOT, or MAY deliberately.
- [ ] Schema changes are synchronized with examples and test vectors.
- [ ] Backward compatibility is explained.
- [ ] Security and privacy impacts are considered.
- [ ] Reference implementations remain consistent.
- [ ] No unrelated large change was made silently.

## Change classes

- **Editorial:** wording, formatting, non-normative examples.
- **Compatible:** optional fields, clarified behavior, additional test vectors.
- **Breaking:** changed field meaning, changed required fields, incompatible canonicalization.
- **Profile-only:** domain semantics that do not alter Core.

Breaking changes require a design discussion and a new draft revision.
