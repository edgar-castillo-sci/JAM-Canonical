
# Documentation

This folder contains supporting documents for the project.

## Contents

- `Sobre_la_canonicalizacion_de_cadenas_JAM.pdf`: initial formalization of the
  canonicalization method. Written in Spanish.

## Note on the symmetry group

The PDF describes the vertical symmetry as four independent operations
(`r`, `t`, `f`, `c`), giving a group of order 24 for buckled options.

The current implementation reflects a later correction, confirmed by
Dr. Jessica Arcudia:

- The vertical symmetry for buckled options is the composition `sign·flip`,
  not `sign` and `flip` independently.
- The group has order 12 for all options.
- The canonical key is the same in both formulations (the orbit is smaller,
  but the minimum is the same).

See `jam_canonical/canonical.py` and the main README for the current
formulation.

## Regenerating

The PDF is a static document. If the method changes substantially, it
should be replaced with an updated version. The current code is the
authoritative source.
