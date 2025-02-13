import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

# Paso 1: Crear un entorno virtual (Explicación en documento externo)
# python -m venv env_vino
# Activar el entorno:
# Windows: env_vino\\Scripts\\activate
# Instalar librerías:
# pip install pandas numpy matplotlib seaborn scikit-learn

# Paso 2: Cargar los datos
dataset = load_wine()

# Paso 3: Convertir a DataFrame
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

# Paso 4: Inspeccionar la estructura de los datos
print("Estructura del dataset:")
print(df.info())
print("\nPrimeras filas del dataset:")
print(df.head())

# Paso 5: Estadísticas descriptivas
descriptive_stats = df.describe()
print("\nEstadísticas descriptivas:")
print(descriptive_stats)

# Paso 6: Detección de valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Paso 7: Análisis de correlación
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Matriz de Correlación")
plt.show()

# Paso 8: Distribución del pH
plt.figure(figsize=(8, 5))
sns.histplot(df['od280/od315_of_diluted_wines'], bins=20, kde=True, color='blue')
plt.title("Distribución del pH del Vino")
plt.xlabel("pH")
plt.ylabel("Frecuencia")
plt.show()

# Paso 9: Comparación del pH entre diferentes clases de vino
plt.figure(figsize=(8, 5))
sns.boxplot(x='target', y='od280/od315_of_diluted_wines', data=df, palette='Set2')
plt.title("Distribución del pH por Tipo de Vino")
plt.xlabel("Clase de Vino")
plt.ylabel("pH")
plt.show()

# Paso 10: Guardar el análisis en un archivo CSV
output_file = "analisis_vino.csv"
df.to_csv(output_file, index=False)
print(f"Análisis completado y guardado en {output_file}")

# Verificación de la generación del archivo
if os.path.exists(output_file):
    print("Archivo CSV generado exitosamente.")
else:
    print("Error al generar el archivo CSV.")
