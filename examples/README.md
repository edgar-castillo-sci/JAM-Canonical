# Examples

Two examples showing how to use canonJAM with and without xjam2.

## `pipeline.py` — self-contained pipeline

Generates candidates for a JAM option and filters duplicates using
canonJAM. Does not require xjam2.

### Usage

```bash
python3 pipeline.py --options 1 --levels 2 3 4 5 6
```

### Output

```
Option 1:
  n=2: 2 classes
  n=3: 4 classes
  n=4: 10 classes
  n=5: 25 classes
  n=6: 70 classes
```

### How it works

Replicates the generation logic of `x.jam` (incremental, level by level),
but replaces the pairwise filter with `filter_duplicates` from
canonJAM.

---

## `x_canonical.py` — integrate with xjam2 via monkey patching

Runs `x.jam` with the canonical method activated. Requires xjam2 and a
valid `JAM.inp` in the current directory.

### Requirements

**xjam2 must be importable.** Two options:

**Option A: install from the original repository**
```bash
pip install git+https://github.com/Theochem-merida/xjam2.git
```

**Option B: use a local copy**
```bash
export PYTHONPATH=/path/to/xjam2:$PYTHONPATH
```

### Step-by-step test

```bash
# 1. Create a test directory
mkdir /tmp/jam-test
cd /tmp/jam-test

# 2. Copy x_canonical.py and x.jam into it
cp /path/to/canonJAM/examples/x_canonical.py .
cp /path/to/xjam2/x.jam .

# 3. Create a test JAM.inp
cat > JAM.inp << 'EOF'
option       1
num_layers   3
poscargen    F
atom_list    C
latticep     2.46
z_vacuum     20.0
buckling     0.0
distance     3.0
EOF

# 4. Run with the canonical method
python3 x_canonical.py
```

### Expected output

```
Canonical method activated for xjam2.

[... output of x.jam ...]
```

The output files (`jamstrings002.txt`, `jamstrings003.txt`, etc.) are
generated as usual, but the filtering uses the canonical method.

### How it works

Monkey-patches `disc_equivalents` in `xjam.libjamstd` and
`xjam.libjamtdm` to use `filter_duplicates` from canonJAM. Then
executes `x.jam` as if nothing had changed.

### Caveats

- This is a monkey patch. It works because `disc_equivalents` is
  replaced at import time. It may break if xjam2 changes internally.
- The canonical method does both passes (`eqnum=1` and `eqnum=2`) in a
  single call. The `eqnum` argument is ignored.
- If you run `x_canonical.py` from a directory without `x.jam` or
  `JAM.inp`, you will get an error. That is expected.
