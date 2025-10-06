## 1.9 Introducción a Pandas

Pandas es una librería de código abierto para el lenguaje de programación Python que facilita tareas: como leer, escribir, limpiar, transformar y analizar datos.
Ofrece estructuras de datos como DataFrames, que son similares a hojas de cálculo, para trabajar con datos tabulares. 


### Instalación
```python
pip install pandas
```
### Importar librería

```python
import pandas as pd
```


## Ejemplos de manejo de DataFrames con Pandas

```python
# 1. Crear un DataFrame desde un diccionario
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# 2. Leer un archivo CSV
df = pd.read_csv('archivo.csv')

# 3. Mostrar las primeras filas
df.head()

# 4. Mostrar las últimas filas
df.tail()

# 5. Obtener información general
df.info()

# 6. Describir estadísticamente
df.describe()

# 7. Seleccionar una columna
df['A']

# 8. Seleccionar varias columnas
df[['A', 'B']]

# 9. Seleccionar filas por índice
df.iloc[0]

# 10. Seleccionar filas por condición
df[df['A'] > 1]

# 11. Añadir una nueva columna
df['C'] = df['A'] + df['B']

# 12. Eliminar una columna
df.drop('C', axis=1, inplace=True)

# 13. Renombrar columnas
df.rename(columns={'A': 'Alpha'}, inplace=True)

# 14. Ordenar por columna
df.sort_values('B', ascending=False)

# 15. Resetear el índice
df.reset_index(drop=True)

# 16. Filtrar valores nulos
df[df['A'].notnull()]

# 17. Reemplazar valores
df.replace({2: 20})

# 18. Agrupar por columna y sumar
df.groupby('B').sum()

# 19. Pivotar datos
df.pivot_table(values='A', index='B', aggfunc='mean')

# 20. Concatenar DataFrames
pd.concat([df, df])

# 21. Unir DataFrames por columna
pd.merge(df1, df2, on='A')

# 22. Aplicar una función a una columna
df['A'].apply(lambda x: x * 2)

# 23. Eliminar filas con valores nulos
df.dropna()

# 24. Llenar valores nulos
df.fillna(0)

# 25. Obtener valores únicos
df['B'].unique()

# 26. Contar valores únicos
df['B'].nunique()

# 27. Contar frecuencia de valores
df['B'].value_counts()

# 28. Crear un DataFrame vacío
pd.DataFrame()

# 29. Cambiar el tipo de datos
df['A'] = df['A'].astype(float)

# 30. Guardar DataFrame a CSV
df.to_csv('nuevo_archivo.csv', index=False)
```
