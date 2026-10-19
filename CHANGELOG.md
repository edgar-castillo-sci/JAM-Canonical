# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-10-19

### Added

- Canonicalization method for JAM strings (`canonical_key`, `filter_duplicates`)
- Symmetry group construction for all 8 JAM options (`generate_group`)
- Array ↔ chain conversion (`array_to_chain`, `chain_to_array`)
- 25 pytest tests
- Validation scripts comparing against the original pairwise method
- Benchmark showing up to 145x speedup
- Examples: standalone pipeline and xjam2 integration
- Bilingual README (EN/ES)
- Zenodo DOI: [10.5281/zenodo.23471387](https://doi.org/10.5281/zenodo.23471387)

### Notes

- The PDF in `docs/` is the initial formalization. The code reflects a later
  correction: for buckled options, the vertical symmetry is the composition
  `sign·flip`, not `sign` and `flip` independently. The group for all options
  has order 12.
