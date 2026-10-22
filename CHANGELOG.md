## [1.1.0] - 2026-10-21

### Added

- `canonical_key_fast`: optimal computation of κ via column sorting.
  O(k) with a constant of 2. Verified to agree with `canonical_key`
  for all 8 options and n=2,3.
- `sort_cols` helper.
- 8 reproducibility scripts under `tests/`:
  `validacion_tabla1.py`, `escalabilidad.py`, `recursion_check.py`,
  `burnside.py`, `burnside_all.py`, `structural.py`,
  `structural_all.py`, `kappa_equal_kappa_prime.py`.
- 10 exploration scripts under `tests/exploration/` for the BPL/BU
  dichotomy and the classification of G-sets.
- "Reproducing the theoretical results" section in README, mapping
  each script to the result it reproduces.
- `tests/test_canonical_fast.py`: parametrized tests verifying
  `canonical_key_fast == canonical_key` for all 8 options and n=2,3.

### Changed

- Version bumped to 1.1.0.
- README reorganized: scientific basis, reproducibility section,
  exploration scripts.
- `tests/README.md` reorganized into three categories: formal tests,
  reproducibility scripts, exploration scripts.
- Test suite now includes 33 tests (was 25).

### Notes

- `canonical_key` remains the literal definition (minimum over the
  12 group elements) and is the function used by the benchmarks, for
  direct correspondence with the theory. `canonical_key_fast` is the
  optimal computation via column sorting.
