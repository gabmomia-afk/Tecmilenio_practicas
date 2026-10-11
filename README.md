# Comparación de modelos de IA para enfermedades en hojas de tomate

**Actividad 4 — Maestría en Inteligencia Artificial, Universidad Tecmilenio**

## Objetivo y caso de uso

Comparar tres clasificadores preentrenados para reconocer hojas de tomate **sanas**, con **tizón temprano** o con **tizón tardío**, con una aplicación potencial de apoyo a inspecciones de vivero. Se estudian precisión, recall, F1 macro, latencia y errores fuera de las tres categorías.

## Modelos y procedencia

| Modelo | Checkpoint | Framework | Parámetros | Licencia reportada* |
|---|---|---|---:|---|
| Vision Transformer (ViT) | `kimcomehome/plantvillage-vit-leaf-disease` | PyTorch / Transformers | 85,827,878 | CC BY-SA 3.0 |
| EfficientNetV2-S | `BrandonFors/effnetv2_s_plant_disease` | PyTorch / torchvision | 20,226,166 | MIT |
| ResNet-50 | `raysarocha/plant-resnet50-38classes` | TensorFlow / Keras | 24,788,134 | Apache 2.0 |

*Licencias reportadas durante el análisis; verificar las tarjetas y archivos de licencia de los repositorios antes de redistribuir modelos o desplegar una solución.*

## Entorno

- Google Colab, GPU NVIDIA Tesla T4, Python 3.13.15.
- TensorFlow 2.21.0, PyTorch 2.11.0+cu130, Transformers 5.18.0, scikit-learn 1.6.1.
- Dependencias declaradas en [`requirements.txt`](requirements.txt). Las versiones exactas de algunas librerías dependen de la imagen CUDA de Colab.
- Autenticación Hugging Face: guardar un secreto de Colab llamado `HF_TOKEN`; **nunca** introducirlo en código ni publicarlo.

## Pasos de ejecución

1. Abrir [`notebooks/GRO_AL02626506_GPIA_ACTIVIDAD_4.ipynb`](notebooks/GRO_AL02626506_GPIA_ACTIVIDAD_4.ipynb) en Google Colab y seleccionar GPU T4 si está disponible.
2. Configurar el secreto `HF_TOKEN` en el panel **Secrets** de Colab, con acceso habilitado para el notebook.
3. Seguir las celdas **en su orden original**, instalando dependencias, cargando los modelos/datasets y ejecutando las evaluaciones.
4. El notebook contiene **intencionalmente** intentos, errores y correcciones documentados durante la práctica; algunas celdas intermedias fallan y son reemplazadas por celdas posteriores. **No se ha verificado una ejecución limpia de principio a fin en una sesión nueva**.
5. Consultar los CSV y las matrices de confusión en [`results/`](results/). Para resumir CSV ya generados sin descargar modelos, ejecutar `python src/resumir_resultados.py` desde la raíz del repositorio.

**Datos:** las imágenes originales se descargan de las fuentes citadas en el notebook; en [`data/`](data/) se incluyen manifiestos y diccionario de campos. Algunas rutas de los manifiestos son relativas a Colab y requieren la estructura de descarga descrita en el notebook.

## Resultados principales

| Modelo | Accuracy PlantVillage (908) | Accuracy PlantDoc (27) | F1 macro PlantDoc | Latencia PlantDoc registrada |
|---|---:|---:|---:|---:|
| ViT | 99.89 % | 62.96 % | 50.46 % | 16.22 ms |
| EfficientNetV2-S | 99.89 % | 55.56 % | 65.12 % | 36.52 ms |
| ResNet-50 | 32.93 % | 29.63 % | 34.99 % | 574.69 ms directa / **24.84 ms compilada** |

La latencia compilada de ResNet-50 se obtuvo con `tf.function` sobre las 27 imágenes y conservó **27/27** predicciones. **No comparar las latencias como un benchmark homogéneo**: las rutas de inferencia y los frameworks difieren.

## Conclusiones

- ViT logró la mayor accuracy en PlantDoc, pero **0/8** hojas sanas correctas.
- EfficientNetV2-S logró el mayor F1 macro y reconoció **5/8** hojas sanas.
- ResNet-50 tuvo bajo desempeño de clasificación; la optimización de inferencia no cambió las predicciones.
- Ningún modelo está validado para diagnóstico autónomo. El conjunto externo tiene solamente 27 imágenes; no se descartó solapamiento con datos de entrenamiento de los checkpoints.
- Se recomienda evaluación adicional con imágenes reales, revisión de etiquetas y supervisión humana.

## Estructura

- `notebooks/`: cuaderno original **sin modificaciones**, con el historial de diagnóstico.
- `results/`: métricas, predicciones, análisis de errores y gráficas.
- `data/`: manifiestos y documentación de origen/esquema; no incluye fotografías.
- `src/`: script auxiliar para resumir resultados existentes.
- `docs/`: informe técnico editable.
- `requirements.txt`: dependencias del proyecto.

## Consideraciones de seguridad y publicación

No publicar credenciales ni tokens. Antes de crear un repositorio **público**, revisar el notebook y sus salidas, que pueden contener nombres, identificadores de cuenta, mensajes de error o metadatos de la sesión. También verificar los términos de uso de modelos y datasets.
