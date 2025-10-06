# ml-zoomcamp-2025

Hola, esta vez compartiendo notas de la experiencia obtenida en el curso de Machine Learning Zoomcamp 2025 de DatatalkClub.

El aprendizaje automático(Machine Learning) es un proceso de extracción de patrones de los datos y existen dos tipos: 

    - características(features: información sobre el objeto) y 

    - objetivo ( target: propiedad a predecir para objetos no visibles).

Por lo tanto, se presentan nuevos valores de características al modelo y este realiza predicciones a partir de los patrones aprendidos.

> Nota: Este trabajo es un resumen del curso. Es casi un traducción acompañada por momentos de lo que fui sintetizando.


## 1.2 ML vs Sistemas Basados en Reglas (Rule-Based Systems)

La diferencia se basa en que en un sistema basado en reglas a menudo es necesario actualizar las "reglas" debido a que los elementos que estas identifican van cambiando, esto es dificil de mantener a medida que el sistema crece.

    Data + Code => Software => Outcome

ML puede resolver este problema con estos pasos:

    ### 1. Obtener datos
    ### 2. Definir y calcular características
    ### 3. Entrenar y usar el Modelo

    Data + Outcome => ML => Model


Las **predicciones son probabilidades**, y para tomar una decisión es necesario definir un umbral que las clasifique.


## 1.3 Supervised Machine Learning

En el Aprendizaje Automático Supervisado (AMS o SML) siempre hay etiquetas asociadas a ciertas características. El modelo se entrena y, posteriormente, puede realizar predicciones sobre nuevas características. De esta manera, el modelo se entrena mediante ciertas características y objetivos.

    Matriz de características (X): compuesta por observaciones u objetos (filas) y características (columnas).

    Variable objetivo (y): un vector con la información del objetivo que queremos predecir. 

Para cada fila de X hay un valor en y.

El modelo se puede representar como una función g que toma la matriz X como parámetro e intenta predecir valores lo más cercanos posible a los objetivos y. La obtención de la función g se denomina entrenamiento.

            g(X) ≈ y

### Tipos de problemas de AMS o SML

Regresión: el resultado es un número (predicción del precio de un coche).

Clasificación: el resultado es una categoría (por ejemplo, probabilidades de spam).

Dentro de Clasificación hay 2 subtipos:

    Binario: hay dos categorías.

    Problemas multiclase: hay más de dos categorías.

Ranking: el resultado son las puntuaciones más altas asociadas a los elementos correspondientes. Se aplica en sistemas de recomendación.

En resumen, SML consiste en enseñar el modelo mediante diferentes ejemplos, y el objetivo es crear una función que tome la matriz de características como parámetro y realice predicciones lo más cercanas posible a los objetivos y.


## 1.4 CRISP-DM

CRISP-DM, acrónimo de Proceso Estándar Intersectorial para Minería de Datos, es un modelo de proceso estándar abierto que describe los enfoques comunes utilizados por los expertos en minería de datos. Es el modelo de análisis más utilizado.

1. **Comprensión del negocio:** Una pregunta importante es si necesitamos Machine Learning para el proyecto. El objetivo del proyecto debe ser medible.

2. **Comprensión de los datos:** Analizar las fuentes de datos disponibles y decidir si se requieren más datos.

3. **Preparación de los datos:** Limpiar los datos, eliminar el ruido mediante pipelines y convertirlos a formato tabular para poder incorporarlos a Machine Learning.

4. **Modelado:** Entrenar diferentes modelos y elegir el mejor. Considerando los resultados de este paso, es conveniente decidir si es necesario añadir nuevas funciones o corregir problemas de datos.

5. **Evaluación:** Medir el rendimiento del modelo y si resuelve el problema de negocio.

6. **Implementación:** Implementar en producción para todos los usuarios. La evaluación y la implementación suelen realizarse juntas (evaluación en línea).

Es importante considerar la facilidad de mantenimiento del proyecto.

En general, los proyectos de aprendizaje automático requieren muchas iteraciones.

**Iteración:**
* Empezar de forma sencilla
* Aprender de los comentarios
* Mejorar


## 1.5 Proceso de Selección del Modelo

### ¿Qué modelo elegir?

- Regresión logística
- Árbol de decisión
- Red neuronal
- O muchos otros

Primero dividir el dataset para entrenamiento, otro para validación y otro para pruebas.

El modelo se ajusta con datos de entrenamiento y se utiliza para predecir los valores y de la matriz de características de validación. Luego, los valores y predichos (probabilidades) se comparan con los valores y reales.

**Problema de comparaciones múltiples (PCM) o Multiple comparisons problem (MCP):** por pura casualidad, un modelo puede tener suerte y obtener buenas predicciones, ya que todas son probabilísticas.

El conjunto de prueba puede ayudar a evitar el PCM o MCP. La obtención del mejor modelo se realiza con los conjuntos de datos de entrenamiento y validación, mientras que el conjunto de datos de prueba se utiliza para garantizar que el mejor modelo propuesto sea el mejor.

1. Dividir los conjuntos de datos en entrenamiento, validación y prueba. Por ejemplo: 60%, 20% y 20% respectivamente
2. Entrenar los modelos
3. Evaluar los modelos
4. Seleccionar el mejor modelo
5. Aplicar el mejor modelo al conjunto de datos de prueba
6. Comparar las métricas de rendimiento de la validación y la prueba


