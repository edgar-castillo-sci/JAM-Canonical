# canonJAM
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23471387.svg)](https://doi.org/10.5281/zenodo.23471387)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Tests](https://img.shields.io/badge/tests-33%20passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

*[Leer en español](README.es.md)*

Canonicalization method for duplicate detection in layered structures
represented with the JAM notation.

## Author

Edgar Castillo (Independent Researcher)

## Associated paper

This package is the reference implementation for the manuscript:

> Castillo, E., Arcudia, J. "Canonical representation of JAM chains:
> formalism and a linear-time algorithm." *Manuscript* (2026).

The paper formalizes the symmetry group of the JAM notation, defines a
canonical representative for each equivalence class, presents an
O(mk) filtering algorithm, and derives closed forms for the number of
inequivalent n-layer configurations via Burnside's lemma. It also
proves a dichotomy: the BPL and BU chain sets are isomorphic as
G-sets if and only if n is even.

## Scientific basis

The JAM notation itself is described in:

> Arcudia, J., Ortiz-Chi, F., Sanchez-Valenzuela, A., Aspuru-Guzik, A.,
> Merino, G. (2023). "Joining and arrangement of multilayers: A string
> representation for honeycomb layered materials." Matter, 6(5),
> 1503–1513. doi: 10.1016/j.matt.2023.02.014

The package is self-contained: it does not require `xjam2` at runtime.
The validation tests optionally use `xjam2` to compare against the
original pairwise method.

> **Note on the formalization.** The PDF in `docs/` is the initial
> formalization of the method. The current implementation reflects a
> later correction (confirmed by Dr. Jessica Arcudia): for buckled
> options, the vertical symmetry is the composition `sign·flip`, not
> `sign` and `flip` independently. The group for all options has order
> 12. See `canonjam/canonical.py` and the section "The symmetry
> group" above for the current version.

## Installation

```bash
pip install -e .
```

For running the validation tests:

```bash
pip install -e ".[tests]"
```

## Usage

```python
from canonjam import canonical_key, canonical_key_fast, filter_duplicates
import numpy as np

# A 3-layer structure
a = np.array([['+0', '+j', '+j'],
              ['+0', '+j', '+j'],
              ['+0', '+j', '+j']])

# Literal computation (Definition 3.14 of the paper): 12 group evaluations
key = canonical_key(a, optionx=1)
print(key)

# Optimal computation (Theorem 3.17 of the paper): 2 evaluations, O(k)
key = canonical_key_fast(a, optionx=1)
print(key)

# Filter a list of structures
unique = filter_duplicates([a, a, a], optionx=1)
print(len(unique))
```

## What it does

JAM generates all possible stacking configurations for an n-layer
system. Many of them are equivalent under symmetry (column rotation,
column swap, layer inversion). The original method detects duplicates
by pairwise comparison, which is O(m²). This package replaces that
with a dictionary of canonical keys, which is O(m).

The canonical key of a structure is the lexicographic minimum of its
orbit under the symmetry group. Two equivalent structures produce
the same key.

The package provides two implementations:

- `canonical_key`: the literal definition (minimum over the 12 group
  elements). Used in the benchmarks of the paper for direct
  correspondence with the theory.
- `canonical_key_fast`: the optimal computation of Theorem 3.17
  (minimum of the sorted-column concatenations of the chain and its
  v-image). O(k) with a constant of 2. Verified to agree with
  `canonical_key` for all 8 options and n=2,3.

## The symmetry group

For option 1 (planar monoelemental) and option 2 (planar binary):

    G = S3 × {e, flip}

For options 3–8 (buckled and ternary):

    G = S3 × {e, sign·flip}

In all cases, |G| = 12.

The vertical symmetry is the composition `sign·flip` (global reflection),
not `sign` and `flip` independently. This was confirmed by Dr. Jessica
Arcudia.

## Contents

- `canonjam/` — the package.
- `tests/` — reproducibility scripts for the paper, the formal test
  suite, and (under `tests/exploration/`) exploratory scripts for the
  BPL/BU dichotomy and the classification of G-sets.
- `docs/` — formal mathematical description (PDF).

## Reproducing the paper

The scripts in `tests/` reproduce the figures and tables of the
manuscript. All of them are self-contained (no `xjam2` required) unless
noted otherwise.

| Script | Reproduces |
|---|---|
| `tests/validacion_tabla1.py` | Class counts against Table 1 of [Arcudia2023] for n=4,5 |
| `tests/escalabilidad.py` | Scalability experiment for n=6,8,10,12 (planar) |
| `tests/recursion_check.py` | Closed forms vs. recursive formulas up to n=30 |
| `tests/burnside.py`, `tests/burnside_all.py` | Fixed-point counts (Table 1 of the paper) |
| `tests/structural.py`, `tests/structural_all.py` | Verification of Theorem 3.16 |
| `tests/kappa_equal_kappa_prime.py` | Verification of Theorem 3.17 (optimality) |
| `tests/benchmark.py` | Filtering-time comparison (Table 3) |
| `tests/validacion.py`, `tests/reporte_completo.py` | Pairwise vs. canonical comparison (Table 2) |

Run any of them from the `tests/` directory, e.g.:

```bash
cd tests
python3 validacion_tabla1.py
python3 escalabilidad.py
python3 recursion_check.py
```

## Running the formal tests

```bash
pytest tests/test_canonical.py tests/test_canonical_fast.py -v
```

## License

MIT (see `LICENSE`).
