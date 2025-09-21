## 1.7 Introducción a NumPy

# Introducción sencilla

Numpy(Numerical Python) es una potente biblioteca para el cálculo numérico en Python. Ofrece compatibilidad con matrices y arreglos multidimensionales de gran tamaño, además de una colección de funciones matemáticas para operar con estos arreglos.
Constituye la base de muchas tareas científicas y relacionadas con datos. 

### Instalación


```bash
pip install numpy
```

### Importando Numpy


Importamos Numpy con el alias `np`


```python
import numpy as np
```


### Creación de matrices


Las matrices son los componentes básicos de Numpy y pueden considerarse como listas, pero con funciones mejoradas.


#### Crear arreglos NumPy 


```python
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```


#### Creación de matrices con ceros, unos o constantes


crear matrices con ceros, unos o cualquier constante usando `np.zeros()`, `np.ones()` y `np.full()`:


```python
zeros_array = np.zeros(10)
ones_array = np.ones(10)
constant_array = np.full(10, 3)
```


### Conversión de listas a matrices


Para convertir una lista de Python en una matriz de Numpy, puede usar `np.array()`:


```python
my_list = [2, 3, 4]
array_from_list = np.array(my_list)
```

### Generación de rangos de números


```python
range_array = np.arange(10) # Crea un array del 0 al 9
```


### Creación de arrays con espaciado lineal


`np.linspace()` crea arrays con números espaciados uniformemente dentro de un rango especificado:


```python
linspace_array = np.linspace(0, 1, 11) # Crea 11 números del 0 al 1
```


### Matrices multidimensionales


Numpy admite arrays multidimensionales, también conocidos como matrices. Aquí hay algunos ejemplos:


```python
zeros_matrix = np.zeros((5, 2)) # Crea matriz de 5 filas y 2 columnas completa con ceros
ones_matrix = np.ones((5, 2))   # Crea matriz de 5 filas y 2 columnas completa con ceros 
constant_matrix = np.full((5, 2), 3)    # Crea matriz de 5 filas y 2 columnas completa con treses
```


## Indexación y segmentación de matrices

Se puede acceder a los elementos de las matrices de Numpy mediante indexación y segmentación. Para matrices bidimensionales:


```python
arr = np.array([[2, 3, 4], [4, 5, 6]])
first_row = arr[0] # Obtiene la primera fila
first_col = arr[:, 0] # Obtiene la primera columna
```


## Generación de matrices aleatorias


Numpy puede crear matrices con números aleatorios. Para garantizar la reproducibilidad, puede establecer una semilla usando `np.random.seed()`:


```python
np.random.seed(2) # Establece la semilla
random_array = np.random.rand(5, 2) # Genera números aleatorios entre 0 y 1
```


Para números aleatorios de una distribución normal o enteros dentro de un rango:


```python
normal_distribution = np.random.randn(5, 2)
random_integers = np.random.randint(low=0, high=100, size=(5, 2))
```


## Operaciones con matrices


Numpy destaca por realizar operaciones matemáticas con matrices de forma eficiente.


### Operaciones por elemento

Puedes realizar operaciones en matrices completas, elemento por elemento:


```python
arr = arr + 1 # Suma 1 a cada elemento
arr = arr * 2 # Multiplica cada elemento por 2
arr = arr / 3 # Divide cada elemento por 3
arr = arr - 5 # Resta 5 a cada elemento
```

### Operaciones por elemento con dos matrices


También puedes realizar operaciones entre dos matrices de la misma forma:


```python
arr1 = np.ones(4)
arr2 = np.full(4, 3)
result = arr1 + arr2 # Suma por elemento
result = arr1 / arr2 # División por elemento
```


### Operaciones de comparación


Puedes realizar comparaciones por elemento y crear matrices booleanas:


```python
arr = np.array([1, 2, 3, 4])
mayor_que_2 = arr > 2 # Produce [Falso, Falso, Verdadero, Verdadero]
```


### Selección de elementos según condiciones


Puede crear submatrices según ciertas condiciones:


```python
selected_elements = arr[arr > 1] # Obtiene elementos mayores que 1 en 'arr' y crea con ellos 'selected_elements'
```


## Operaciones de resumen


Numpy proporciona funciones para resumir datos de matrices:


```python
min_value = arr.min() # Valor mínimo
max_value = arr.max() # Valor máximo
sum_value = arr.sum() # Suma de todos los elementos
mean_value = arr.mean() # Valor medio (promedio)
std_deviation = arr.std() # Desviación estándar
```