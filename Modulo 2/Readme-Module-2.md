

> Nota: Este trabajo es un resumen del curso. Es casi un traducción acompañada por momentos de lo que fui sintetizando.

Regresión de Aprendizaje Automático (AA) o 
La regresión es una técnica fundamental del aprendizaje automático que se utiliza para predecir resultados continuos. Se utiliza ampliamente en diversos ámbitos, como finanzas, salud y economía, para pronosticar tendencias, analizar relaciones y realizar predicciones basadas en variables de entrada.

En la regresión, el objetivo es encontrar la línea o curva de mejor ajuste que describa la relación entre las características de entrada (variables independientes) y la variable objetivo (variable dependiente). La regresión lineal es una de las técnicas de regresión más sencillas y utilizadas, y su objetivo es ajustar una ecuación lineal a los datos.

Regresión mediante regresión lineal: Un proceso paso a paso
1. Preparar los datos y realizar un análisis exploratorio de datos (AED):
Limpiar los datos, gestionar los valores faltantes y preprocesar las características.
Explorar y comprender los datos mediante análisis estadístico, visualización y estadísticas de resumen. 2. Usar regresión lineal para predecir el objetivo (precio en este ejemplo):
Seleccione las características (variables independientes) y la variable objetivo (p. ej., precio de la vivienda).
Divida los datos en conjuntos de entrenamiento y prueba.
Entrene un modelo de regresión lineal con los datos de entrenamiento.
3. Funcionamiento interno de la regresión lineal:
La regresión lineal ajusta una línea (en regresión lineal simple) o un hiperplano (en regresión lineal múltiple) para minimizar la suma de las diferencias cuadradas entre los valores observados y predichos.
Utiliza técnicas como los mínimos cuadrados ordinarios (MCO) para estimar los parámetros del modelo (coeficientes) que definen la línea.
4. Evalúe el modelo utilizando el error cuadrático medio (RMSE):
El RMSE mide el error promedio entre los valores observados y predichos.
Un RMSE bajo indica un mejor ajuste del modelo a los datos.
5. Ingeniería de características:
Mejore la capacidad predictiva del modelo creando nuevas características o transformando las existentes. La ingeniería de características puede implicar escalado, agrupamiento, codificación one-hot o la extracción de información útil de datos sin procesar.

6. Regularización (opcional):
Implemente técnicas de regularización como la regresión Lasso (L1) o Ridge (L2) para evitar el sobreajuste y mejorar la generalización del modelo.
La regularización añade una penalización a los parámetros del modelo para evitar coeficientes excesivamente altos.

7. Uso del modelo para predicciones:
Aplique el modelo entrenado para realizar predicciones sobre datos nuevos e inéditos.
Utilice el modelo para pronosticar precios basándose en las características seleccionadas.
Siguiendo este proceso paso a paso, podrá utilizar eficazmente la regresión lineal para la predicción, comprender sus mecanismos internos, evaluar su rendimiento y mejorarla mediante la ingeniería de características y la regularización.

Ejemplo: Predicción de precios de viviendas
A continuación, se muestra un ejemplo de Python para cada paso del proceso utilizando una regresión lineal simple para predecir precios de viviendas:

Preparación de los datos y análisis exploratorio de datos (EDA):