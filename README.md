# canonJAM
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23471387.svg)](https://doi.org/10.5281/zenodo.23471387)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Tests](https://img.shields.io/badge/tests-25%20passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

*[Leer en español](README.es.md)*

Canonicalization method for duplicate detection in layered structures
represented with the JAM notation.

## Author

Edgar R. H. Castillo (Independent Researcher)

## Scientific basis

This package implements a computational method on top of the JAM
notation described in:

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
from canonjam import canonical_key_std, disc_equivalents_canonical_std
import numpy as np

# A 3-layer structure
a = np.array([['+0', '+j', '+j'],
              ['+0', '+j', '+j'],
              ['+0', '+j', '+j']])

# Compute its canonical key
key = canonical_key_std(a, optionx=1)
print(key)

# Filter a list of structures
unique = disc_equivalents_canonical_std([a, a, a], optionx=1)
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
- `tests/` — validation scripts and formal test suite.
- `docs/` — formal mathematical description (PDF).

## Running the validation

```bash
pip install -e ".[tests]"

# Option A: use xjam2 installed via pip
pip install git+https://github.com/Theochem-merida/xjam2.git

# Option B: use a local copy of xjam2
export PYTHONPATH=/path/to/xjam2:$PYTHONPATH

cd tests
python3 validacion.py
```

The validation compares the canonical method against the original
pairwise method for all 8 JAM options, verifying that both produce
the same equivalence classes.

## Running the formal tests

```bash
pytest tests/test_canonical.py -v
```

## License

MIT (see `LICENSE`).
