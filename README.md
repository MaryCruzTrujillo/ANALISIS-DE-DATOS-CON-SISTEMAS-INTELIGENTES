# **Análisis Exploratorio de Datos del Vino**

## **Descripción del Proyecto**
Este proyecto realiza un **análisis exploratorio de datos** sobre un conjunto de datos de vinos utilizando **Python y librerías de análisis de datos**. El objetivo principal es evaluar la influencia del **pH en la clasificación del vino** y visualizar patrones relevantes.

El dataset utilizado es `load_wine` de `sklearn.datasets`, que contiene información sobre diferentes **variedades de vino**, incluyendo propiedades químicas como **alcohol, acidez, flavonoides y pH**.

## **Requisitos Previos**
Antes de ejecutar el código, asegúrate de tener instalado **Python 3.8 o superior** y las siguientes librerías:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Si no las tienes instaladas, ejecuta el siguiente comando en tu terminal:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## **Estructura del Proyecto**
El proyecto contiene los siguientes archivos:

```
📂 Analisis_Vino
 ├── 📄 analisis_vino.py        # Código principal para el análisis
 ├── 📄 analisis_vino.csv       # Archivo generado con datos analizados
 ├── 📄 informe.docx            # Informe detallado del análisis
 ├── 📄 README.md               # Instrucciones del proyecto
```

## **Ejecutar el Código**
Para ejecutar el análisis, sigue estos pasos:

1. **Clonar el repositorio o descargar los archivos:**
   ```bash
   git clone https://github.com/tu_usuario/Analisis_Vino.git
   cd Analisis_Vino
   ```

2. **Crear un entorno virtual:**
   ```bash
   python -m venv env_vino
   ```
   - **Windows**: `env_vino\Scripts\activate`
   - **Mac/Linux**: `source env_vino/bin/activate`

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el script:**
   ```bash
   python analisis_vino.py
   ```

5. **Revisar los resultados**:
   - Se generarán **visualizaciones** para el análisis de correlaciones y distribución del pH.
   - Se guardará un archivo **`analisis_vino.csv`** con los datos analizados.

## **Visualizaciones Incluidas**
El análisis exploratorio genera las siguientes gráficas:
1. **Matriz de correlación** para identificar relaciones entre variables.
2. **Histograma de distribución del pH**.
3. **Boxplot de pH en diferentes clases de vino**.

## **Conclusiones**
El análisis revela que el pH del vino tiene una relación con otras características químicas, lo que influye en su clasificación y calidad. Se observan diferencias significativas en el pH según la categoría de vino.

## **Referencias**
- Documentación de Pandas: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- Documentación de Seaborn: [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
- Documentación de Scikit-Learn: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)