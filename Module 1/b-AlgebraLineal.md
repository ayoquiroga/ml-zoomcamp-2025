## 1.8 Repaso de álgebra lineal


El álgebra lineal sirve para resolver problemas que involucran vectores y matrices. Es una rama fundamental de las matemáticas con aplicaciones en casi todos los campos de la ciencia y la tecnología, ya que proporciona un lenguaje y herramientas para modelar relaciones y sistemas complejos de manera simple y organizada.


### Repaso de Álgebra Lineal

* Operaciones vectoriales
* Multiplicación
* Multiplicación vector-vector
* Multiplicación matriz-vector
* Multiplicación matriz-matriz
* Matriz identidad
* Inversa

### Operaciones vectoriales

~~~~python
u = np.array([2, 7, 5, 6])
v = np.array([3, 4, 8, 6])

# Suma
u + v

# Resta
u - v

# Multiplicación escalar
2 * v
~~~~


### Multiplicación

##### Multiplicación vector-vector

~~~~python
def vector_vector_multiplication(u, v):
    # verifica que la cantidad de columnas de los vectores sean iguales
    assert u.shape[0] == v.shape[0]
    # asigna la cantidad de columnas a n
    n = u.shape[0]
    # inicializa result con 0.0
    result = 0.0
    # recorre cada elemento de los vectores, los multiplica y los va sumando en result
    for i in range(n):
        result = result + u[i] * v[i]
    # retorna result
    return result
~~~~


Existe un método en Numpy que permite lo anterior de manera mas simple

~~~~python
u.dot(v) #Multiplicación vector-vector
~~~~

##### Multiplicación matriz-vector

Para poder realizar esta operación debe coincidir la cantidad de columnas de la matriz U(U.shape[1]), ejemplo: 2x3, debe ser igual a la cantidad de filas de v(v.shape[0]), ejemplo: 3x5

~~~~python
def matrix_vector_multiplication(U, v):
    # verifica que la cantidad de columnas de la matriz U sea igual a la de filas del vector v
    assert U.shape[1] == v.shape[0]
    # asigna la cantidad de columnas de U num_rows
    num_rows = U.shape[0]
    # inicializa con ceros el vector 'result' donde se guardará el resultado
    result = np.zeros(num_rows)
    # cada fila de U[i] la multiplica por v y retorna la sumatoria de esas i repeteciones
    for i in range(num_rows):
        result[i] = vector_vector_multiplication(U[i], v)
    
    return result
~~~~



##### Multiplicación matriz-matriz


~~~~python
def matrix_matrix_multiplication(U, V):
    # verifica que la cantidad de columnas de U y la de filas de V sean iguales
    assert U.shape[1] == V.shape[0]
    # asigna las cantidades a variables num_rows y num_cols
    num_rows = U.shape[0]
    num_cols = V.shape[1]
    # inicializa con ceros la matriz 'result' donde se guardarán el resultado
    result = np.zeros((num_rows, num_cols))
    # iterna un rango de num_cols, vi guarda la columna de V[:,i], la sumatoria de U.vi en Uvi que luego se ubicará en su lugar de la matriz de resultado 'result'
    for i in range(num_cols):
        vi = V[:, i]
        Uvi = matrix_vector_multiplication(U, vi)
        result[:, i] = Uvi
    
    return result
~~~~


### Matriz identidad

Es una matriz cuadrada que contiene todos 1 en su diagonal principal, ceros en todas las demas posiciones, se nombra con I y 


~~~~python
I = np.eye(3)
~~~~



### Inversa

Una matriz inversa (V⁻¹) es una matriz que, al ser multiplicada por la matriz original (V), da como resultado la matriz identidad (I), es decir, V * V⁻¹ = I

En numpy se utiliza 'np.linalg.inv()' para enconctrar la inversa de una matriz.

~~~~python
V = np.array([
[1, 1, 2],
[0, 0.5, 1],
[0, 2, 1],
])
inv = np.linalg.inv(V)
~~~~