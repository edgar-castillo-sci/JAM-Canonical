"""
x_canonical.py

Run x.jam with the canonical method activated.

This script monkey-patches disc_equivalents in xjam2 to use
filter_duplicates from canonJAM. It then executes x.jam
as if nothing had changed.

Requirements:
  - xjam2 must be importable (installed or in PYTHONPATH)
  - A valid JAM.inp must exist in the current directory

Usage:
    python3 x_canonical.py
"""

import os
import sys

# 1. Import xjam2 modules
import xjam.libjamstd as std
import xjam.libjamtdm as tdm

# 2. Import the canonical filter
from canonjam import filter_duplicates


# 3. Define the replacement
def disc_equivalents_canonical(stackinglist, optionx, eqnum=None):
    """
    Drop-in replacement for disc_equivalents.

    The canonical method does both passes (eqnum=1 and eqnum=2)
    in a single call, so eqnum is ignored.
    """
    return filter_duplicates(stackinglist, optionx)


# 4. Apply the monkey patch
std.disc_equivalents = disc_equivalents_canonical
tdm.disc_equivalents = disc_equivalents_canonical

print("Canonical method activated for xjam2.")
print()

# 5. Execute x.jam from the current working directory
xjam_script = os.path.join(os.getcwd(), "x.jam")
if not os.path.isfile(xjam_script):
    print(f"Error: no x.jam found in {os.getcwd()}")
    sys.exit(1)

exec(open(xjam_script).read())
