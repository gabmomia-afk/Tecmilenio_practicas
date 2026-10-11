# Datos

Las fotografías originales **no se redistribuyen** en este repositorio. Se descargan desde las fuentes públicas indicadas en el notebook, respetando las condiciones de uso de cada conjunto.

- **PlantVillage:** el notebook usa `datasets.load_dataset("geraldmc/plantvillage-full")`; se seleccionan las clases `Tomato___healthy`, `Tomato___Early_blight` y `Tomato___Late_blight`.
- **PlantDoc:** el notebook descarga el repositorio `pratikkayal/PlantDoc-Dataset` y utiliza imágenes de las carpetas `train/` y `test/` para esas tres categorías de tomate.

## Campos de los manifiestos

| Campo | Descripción |
|---|---|
| `division` | Partición original (`train` o `test`). |
| `ruta` | Ruta relativa a la sesión de Colab donde se descargó la imagen. |
| `clase_original` | Nombre de la carpeta/categoría original de PlantDoc. |
| `etiqueta_real` | Etiqueta normalizada al esquema PlantVillage de 38 clases. |
| `indice` | Identificador secuencial de las 27 imágenes del subconjunto de prueba, cuando está presente. |
| `sha256` | Hash de archivo para detectar duplicados byte a byte, cuando está presente. |

Se analizaron 262 imágenes de tomate en PlantDoc (235 train, 27 test), sin duplicados **exactos** entre esas 262 imágenes. No se ha demostrado ausencia de duplicados visuales ni solapamiento con los datos originales de entrenamiento de los checkpoints.
