# Tests and reproducibility scripts

This directory contains three kinds of scripts:

1. A **formal test suite** (`test_canonical.py`, `test_canonical_fast.py`)
   that validates the package itself. Does not require `xjam2`.
2. **Reproducibility scripts** for the theoretical results of the
   package. Most are self-contained; `validacion.py` and
   `reporte_completo.py` optionally use `xjam2` as a baseline.
3. An **exploration** subdirectory (`exploration/`) with scripts used to
   construct and verify the BPL/BU G-set isomorphism and to explore the
   classification of G-sets. Not part of the reproducibility suite.

## Requirements

The formal test suite and most reproducibility scripts are
self-contained. Only `validacion.py` and `reporte_completo.py` need
`xjam2` as an optional baseline. Two options:

**Option A: install from the original repository**
```bash
pip install git+https://github.com/Theochem-merida/xjam2.git
```

**Option B: use a local copy**
```bash
export PYTHONPATH=/path/to/xjam2:$PYTHONPATH
```

Note: installing `xjam2` via `pip` may fail with newer setuptools versions
(`pkg_resources` was removed). If so, use Option B.

## Running the formal tests

```bash
cd ..
pip install -e ".[tests]"
pytest tests/test_canonical.py tests/test_canonical_fast.py -v
```

## Reproducibility scripts

### `validacion.py`

Validates the canonical method against the original pairwise method for
all 8 JAM options, verifying that both produce the same equivalence classes.

```bash
python3 validacion.py
python3 validacion.py --levels 2 3 4
```

Options:
- `--levels`: layer counts to validate (default: `2 3`).
  `n=2` and `n=3` are sufficient. `n>=4` is slow for the original method.
  `n>=5` is prohibitively slow.

### `validacion_tabla1.py`

Checks the class counts against Table 1 of [Arcudia2023] for n=2,3,4,5
on all 8 options.

```bash
python3 validacion_tabla1.py
```

### `reporte_completo.py`

Generates a detailed report with all canonical keys produced by each
method, side by side.

```bash
python3 reporte_completo.py
python3 reporte_completo.py --levels 2 3 4 --output /tmp/report.txt
```

Options:
- `--levels`: layer counts to report (default: `2 3`).
- `--output`: output file path (default: `reporte_completo_salida.txt`).

### `benchmark.py`

Measures the filtering time of both methods. The original method is O(m²),
so it is measured only while its estimated time stays below `--max-time`
(default: 30 s). Above that threshold, only the canonical method is measured.

```bash
python3 benchmark.py
python3 benchmark.py --options 1 5 --levels 2 3 4 5 --max-time 60
```

Options:
- `--levels`: layer counts to benchmark (default: `2 3 4 5`).
- `--options`: JAM options to benchmark (default: `1 5 7`).
- `--max-time`: max estimated time for the original method, in seconds
  (default: 30).
- `--output`: output TSV file path (default: `benchmark_salida.tsv`).

### `escalabilidad.py`

Scalability experiment for the planar case up to n=12. Self-contained:
uses the canonical filter for intermediate deduplication, which is what
makes generation feasible at that scale.

```bash
python3 escalabilidad.py
```

Expected output:
```
n=6:  m=150,     classes=70,     gen=0.05s, filter=0.03s
n=8:  m=1,176,   classes=574,    gen=0.41s, filter=0.27s
n=10: m=10,086,  classes=5,002,  gen=3.66s, filter=2.42s
n=12: m=89,304,  classes=44,530, gen=34.68s, filter=22.77s
```

### `recursion_check.py`

Verifies that the closed forms derived via Burnside's lemma agree with
the recursive formulas of [Arcudia2023] for n=2..30, for PL, BPL/BU,
and BBU. Self-contained.

```bash
python3 recursion_check.py
```

Expected output: `All match for N=2..30 (PL, BPL/BU, BBU)`.

### `burnside.py`, `burnside_all.py`

Compute the fixed-point counts \(|Fix(g)|\) for each conjugacy class of
\(G = S_3 \times \mathbb{Z}/2\). `burnside.py` covers PL; `burnside_all.py`
covers all 8 options.

```bash
python3 burnside.py
python3 burnside_all.py
```

### `structural.py`, `structural_all.py`

Verify that \(a \sim b\) iff the column multisets of \(a\) and \(b\)
coincide, or the column multiset of \(a\) equals that of \(v(b)\).
`structural.py` covers options 1–4; `structural_all.py` covers all 8
options.

```bash
python3 structural.py
python3 structural_all.py
```

### `kappa_equal_kappa_prime.py`

Verifies that the literal minimum over the 12 group elements equals the
\(O(k)\)-with-constant-2 computation. Covers all 8 options for n=2,3.

```bash
python3 kappa_equal_kappa_prime.py
```

Expected output: `kappa == kappa' for all options and n=2,3`.

## Exploration scripts (`exploration/`)

These scripts were used to construct and verify the BPL/BU G-set
isomorphism and to explore the classification of \(X_n^{\tau}\) as a
\(G\)-set. They are not part of the reproducibility suite, but are kept
for future work on canonical augmentation and on the classification of
\(G\)-sets.

| Script | Purpose |
|---|---|
| `build_bijection.py`, `build_bijection_v2.py`, `build_bijection_exact.py` | Construct the bijection \(\varphi_2\) between \(X_2^{BPL}\) and \(X_2^{BU}\) |
| `verify_bijection.py`, `verify_bijection_n4.py` | Verify that \(\varphi_2\) (and \(\varphi_4 = \varphi_2^{\otimes 2}\)) are \(G\)-equivariant bijections |
| `block_product_equiv.py` | Verify that \(\varphi_2^{\otimes m}\) is \(G\)-equivariant for m up to 3 |
| `orbit_sizes.py` | Compute the distribution of orbit sizes for BPL and BU |
| `stabilizer_types.py`, `stabilizer_conjclasses.py` | Compare the stabilizer distributions of BPL and BU |
| `pattern_search.py` | Search for a general pattern for \(\varphi_{2m}\) |

## Exit codes

All scripts exit with:
- `0` if all validations pass (or the experiment completes without error).
- `1` if any validation fails.
