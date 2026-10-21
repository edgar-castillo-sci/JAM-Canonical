# canonJAM
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23471387.svg)](https://doi.org/10.5281/zenodo.23471387)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Tests](https://img.shields.io/badge/tests-25%20passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

*[Read in English](README.md)*

Método de canonicalización para detección de duplicados en estructuras
laminares representadas con la notación JAM.

## Autor

Edgar R. H. Castillo (Independent Researcher)

## Base científica

Este paquete implementa un método computacional sobre la notación JAM
descrita en:

> Arcudia, J., Ortiz-Chi, F., Sanchez-Valenzuela, A., Aspuru-Guzik, A.,
> Merino, G. (2023). "Joining and arrangement of multilayers: A string
> representation for honeycomb layered materials." Matter, 6(5),
> 1503–1513. doi: 10.1016/j.matt.2023.02.014

El paquete es autocontenido: no requiere `xjam2` en tiempo de ejecución.
Los tests de validación usan `xjam2` opcionalmente para comparar contra
el método original.

> **Nota sobre la formalización.** El PDF en `docs/` es la formalización
> inicial del método. La implementación actual refleja una corrección
> posterior (confirmada por la Dra. Jessica Arcudia): para opciones
> buckled, la simetría vertical es la composición `sign·flip`, no `sign`
> y `flip` de forma independiente. El grupo para todas las opciones
> tiene orden 12. Ver `canonjam/canonical.py` y la sección "El grupo
> de simetría" arriba para la versión actual.

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
from canonjam import canonical_key_std, disc_equivalents_canonical_std
import numpy as np

# Una estructura de 3 capas
a = np.array([['+0', '+j', '+j'],
              ['+0', '+j', '+j'],
              ['+0', '+j', '+j']])

# Calcular su clave canónica
clave = canonical_key_std(a, optionx=1)
print(clave)

# Filtrar una lista de estructuras
unicas = disc_equivalents_canonical_std([a, a, a], optionx=1)
print(len(unicas))
```

## Qué hace

JAM genera todas las configuraciones de apilamiento para un sistema de
n capas. Muchas son equivalentes bajo simetría (rotación de columnas,
intercambio de columnas, inversión de capas). El método original detecta
duplicados por comparación pairwise, que es O(m²). Este paquete lo
reemplaza por un diccionario de claves canónicas, que es O(m).

La clave canónica de una estructura es el mínimo lexicográfico de su
órbita bajo el grupo de simetría. Dos estructuras equivalentes producen
la misma clave.

## El grupo de simetría

Para opción 1 (planar monoelemental) y opción 2 (planar binaria):

    G = S3 × {e, flip}

Para opciones 3–8 (buckled y ternarias):

    G = S3 × {e, sign·flip}

En todos los casos, |G| = 12.

La simetría vertical es la composición `sign·flip` (reflexión global),
no `sign` y `flip` de forma independiente. Esto fue confirmado por la
Dra. Jessica Arcudia.

## Contenido

- `canonjam/` — el paquete.
- `tests/` — scripts de validación y suite formal de tests.
- `docs/` — descripción matemática formal (PDF).

## Correr la validación

```bash
pip install -e ".[tests]"

# Opción A: usar xjam2 instalado vía pip
pip install git+https://github.com/Theochem-merida/xjam2.git

# Opción B: usar una copia local de xjam2
export PYTHONPATH=/ruta/a/xjam2:$PYTHONPATH

cd tests
python3 validacion.py
```

La validación compara el método canónico contra el método pairwise
original para las 8 opciones de JAM, verificando que ambos producen
las mismas clases de equivalencia.

## Correr los tests formales

```bash
pytest tests/test_canonical.py -v
```

## Licencia

MIT (ver `LICENSE`).
