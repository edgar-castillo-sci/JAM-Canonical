# Validation scripts

Three standalone scripts and one formal test suite.

## Requirements

`xjam2` must be available for the validation scripts. Two options:

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

The formal test suite (`test_canonical.py`) does **not** require `xjam2`.

## Running the formal tests

```bash
cd ..
pip install -e ".[tests]"
pytest tests/test_canonical.py -v
```

## Running the validation scripts

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

## Exit codes

All three scripts exit with:
- `0` if all validations pass (or benchmark completes without error).
- `1` if any validation fails.
