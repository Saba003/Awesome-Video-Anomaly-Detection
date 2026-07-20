# Contributing

Thank you for helping maintain this VAD resource.

## Contribution types

You may submit:

- A new paper entry
- A benchmark correction
- A dataset entry
- A metadata or link correction
- A taxonomy or documentation improvement

## Data rules

1. Use the official paper, project page, or repository as the primary source.
2. Record benchmark values exactly as reported.
3. Include the evaluation level and protocol where available.
4. Do not compare incompatible metrics as if they were directly equivalent.
5. Add notes for non-standard splits or evaluation protocols.

## Pull request checklist

- [ ] No duplicate paper ID
- [ ] URLs are valid
- [ ] Dataset names match existing canonical names
- [ ] Metric units are explicit
- [ ] Benchmark values are traceable to a source
- [ ] `python analysis/scripts/validate_entries.py` passes
