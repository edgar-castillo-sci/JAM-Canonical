# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-10-21

### Added

- `canonical_key_fast`: optimal computation of κ via column sorting
  (Theorem 3.17 of Castillo & Arcudia, 2026). Verified to agree with
  `canonical_key` for all 8 options and n=2,3.
- `sort_cols` helper.
- 8 reproducibility scripts under `tests/` for the paper:
  `validacion_tabla1.py`, `escalabilidad.py`, `recursion_check.py`,
  `burnside.py`, `burnside_all.py`, `structural.py`,
  `structural_all.py`, `kappa_equal_kappa_prime.py`.
- 10 exploration scripts under `tests/exploration/` for the BPL/BU
  dichotomy (Proposition 3.22 of the paper) and the classification of
  G-sets (future work).
- "Reproducing the paper" section in README, mapping each script to
  the table or theorem it reproduces.
- `tests/test_canonical_fast.py`: parametrized tests verifying
  `canonical_key_fast == canonical_key` for all 8 options and n=2,3.

### Changed

- Version bumped to 1.1.0.
- README reorganized: associated paper, reproducibility section,
  exploration scripts.
- `tests/README.md` reorganized into three categories: formal tests,
  reproducibility scripts, exploration scripts.
- Test suite now includes 33 tests (was 25).

### Notes

- The package now implements the optimal computation of κ proved in
  the paper (Theorem 3.17). `canonical_key` remains the literal
  definition (Definition 3.14) and is the function used by the
  benchmarks reported in the paper, for direct correspondence with
  the theory.
  
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
