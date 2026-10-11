"""Lee los CSV ya generados por el notebook; no descarga ni ejecuta modelos."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
archivo = ROOT / "results" / "resultados_finales.csv"
if not archivo.exists():
    raise SystemExit(f"No se encontró: {archivo}")
df = pd.read_csv(archivo)
columnas = ["Modelo", "Dataset", "Imagenes", "Accuracy", "Precision_macro", "Recall_macro", "F1_macro", "Latencia_original_ms", "Latencia_optimizada_ms"]
print(df[columnas].to_string(index=False, float_format=lambda v: f"{v:.4f}"))
print("\nNota: las latencias provienen de diferentes rutas de inferencia; no son estrictamente comparables.")
