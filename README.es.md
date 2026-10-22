# canonJAM
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23471387.svg)](https://doi.org/10.5281/zenodo.23471387)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Tests](https://img.shields.io/badge/tests-33%20passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

*[Read in English](README.md)*

Método de canonicalización para detección de duplicados en estructuras
laminadas representadas con la notación JAM.

## Autor

Edgar Castillo (Investigador Independiente)

## Artículo asociado

Este paquete es la implementación de referencia del manuscrito:

> Castillo, E., Arcudia, J. "Canonical representation of JAM chains:
> formalism and a linear-time algorithm." *Manuscrito* (2026).

El artículo formaliza el grupo de simetría de la notación JAM, define un
representante canónico para cada clase de equivalencia, presenta un
algoritmo de filtrado O(mk), y deriva formas cerradas para el número de
configuraciones de n capas no equivalentes mediante el lema de Burnside.
También demuestra una dicotomía: los conjuntos de cadenas BPL y BU son
isomorfos como G-conjuntos si y solo si n es par.

## Base científica

La notación JAM está descrita en:

> Arcudia, J., Ortiz-Chi, F., Sanchez-Valenzuela, A., Aspuru-Guzik, A.,
> Merino, G. (2023). "Joining and arrangement of multilayers: A string
> representation for honeycomb layered materials." Matter, 6(5),
> 1503–1513. doi: 10.1016/j.matt.2023.02.014

El paquete es autocontenido: no requiere `xjam2` en tiempo de ejecución.
Los scripts de validación usan opcionalmente `xjam2` para comparar contra
el método pairwise original.

> **Nota sobre la formalización.** El PDF en `docs/` es la formalización
> inicial del método. La implementación actual refleja una corrección
> posterior (confirmada por la Dra. Jessica Arcudia): para las opciones
> buckled, la simetría vertical es la composición `sign·flip`, no `sign`
> y `flip` de forma independiente. El grupo para todas las opciones tiene
> orden 12. Ver `canonjam/canonical.py` y la sección "The symmetry group"
> arriba para la versión actual.

## Instalación

```bash
pip install -e .
```

Para correr los tests de validación:

```bash
pip install -e ".[tests]"
```

## Uso

```python
from canonjam import canonical_key, canonical_key_fast, filter_duplicates
import numpy as np

# Una estructura de 3 capas
a = np.array([['+0', '+j', '+j'],
              ['+0', '+j', '+j'],
              ['+0', '+j', '+j']])

# Cómputo literal (Definición 3.14 del artículo): 12 evaluaciones del grupo
key = canonical_key(a, optionx=1)
print(key)

# Cómputo óptimo (Teorema 3.17 del artículo): 2 evaluaciones, O(k)
key = canonical_key_fast(a, optionx=1)
print(key)

# Filtrar una lista de estructuras
unique = filter_duplicates([a, a, a], optionx=1)
print(len(unique))
```

## Qué hace

JAM genera todas las configuraciones de apilamiento posibles para un
sistema de n capas. Muchas son equivalentes bajo simetría (rotación de
columnas, intercambio de columnas, inversión de capas). El método
original detecta duplicados por comparación pairwise, que es O(m²).
Este paquete reemplaza eso con un diccionario de claves canónicas, que
es O(m).

La clave canónica de una estructura es el mínimo lexicográfico de su
órbita bajo el grupo de simetría. Dos estructuras equivalentes producen
la misma clave.

El paquete ofrece dos implementaciones:

- `canonical_key`: la definición literal (mínimo sobre los 12 elementos
  del grupo). Usada en los benchmarks del artículo para correspondencia
  directa con la teoría.
- `canonical_key_fast`: el cómputo óptimo del Teorema 3.17 (mínimo de
  las concatenaciones de columnas ordenadas de la cadena y de su
  v-imagen). O(k) con constante 2. Verificado que coincide con
  `canonical_key` para las 8 opciones y n=2,3.

## El grupo de simetría

Para la opción 1 (planar monoelemental) y la opción 2 (planar binaria):

    G = S3 × {e, flip}

Para las opciones 3–8 (buckled y ternarias):

    G = S3 × {e, sign·flip}

En todos los casos, |G| = 12.

La simetría vertical es la composición `sign·flip` (reflexión global),
no `sign` y `flip` de forma independiente. Esto fue confirmado por la
Dra. Jessica Arcudia.

## Contenido

- `canonjam/` — el paquete.
- `tests/` — scripts de reproducibilidad para el artículo, la suite
  de tests formal, y (bajo `tests/exploration/`) scripts de
  exploración para la dicotomía BPL/BU y la clasificación de
  G-conjuntos.
- `docs/` — descripción matemática formal (PDF).

## Reproduciendo el artículo

Los scripts en `tests/` reproducen las figuras y tablas del manuscrito.
Todos son autocontenidos (no requieren `xjam2`) salvo que se indique.

| Script | Reproduce |
|---|---|
| `tests/validacion_tabla1.py` | Conteos de clase contra la Tabla 1 de [Arcudia2023] para n=4,5 |
| `tests/escalabilidad.py` | Experimento de escalabilidad para n=6,8,10,12 (planar) |
| `tests/recursion_check.py` | Formas cerradas vs. fórmulas recursivas hasta n=30 |
| `tests/burnside.py`, `tests/burnside_all.py` | Conteos de puntos fijos (Tabla 1 del artículo) |
| `tests/structural.py`, `tests/structural_all.py` | Verificación del Teorema 3.16 |
| `tests/kappa_equal_kappa_prime.py` | Verificación del Teorema 3.17 (optimalidad) |
| `tests/benchmark.py` | Comparación de tiempos de filtrado (Tabla 3) |
| `tests/validacion.py`, `tests/reporte_completo.py` | Comparación pairwise vs. canónico (Tabla 2) |

Corre cualquiera desde el directorio `tests/`, por ejemplo:

```bash
cd tests
python3 validacion_tabla1.py
python3 escalabilidad.py
python3 recursion_check.py
```

## Corriendo los tests formales

```bash
pytest tests/test_canonical.py tests/test_canonical_fast.py -v
```

## Licencia

MIT (ver `LICENSE`).
