
# Linear regression Introduction


¿Cómo predecir el precio de un auto?

Supongamos que un vendedor de autos usados quiere saber cuánto vale un auto que acaba de comprar. En lugar de adivinar, puede usar el modelo de regresión lineal para hacer una predicción. El modelo le ayudará a encontrar una relación entre el precio del auto y una o más de sus características, como el kilometraje.

El modelo va a buscar una línea recta que represente la relación entre el kilometraje y el precio. Por lo general, a más kilometraje, menor es el precio. La regresión lineal nos ayuda a cuantificar exactamente cuánto baja el precio por cada kilómetro adicional.

La fórmula es:

* ***Y = m.X + b***

esto se traduce a:

* **Precio del auto** = m * Kilometraje + b

* **Precio del auto (Y)**: Lo que queremos predecir.

* **Kilometraje (X)**: La variable que usamos para la predicción.

* **m (la pendiente)**: Nos dice cuánto cambia el precio por cada kilómetro recorrido. Como el precio baja a medida que aumenta el kilometraje, esta pendiente será un número negativo. Por ejemplo, si m = -0.10, significa que por cada kilómetro adicional, el precio del auto baja 10 centavos.

* **b (el intercepto)**: Es el precio inicial estimado del auto cuando su kilometraje es cero.

El modelo de regresión lineal toma datos de autos que ya se han vendido (con su kilometraje y precio real) y ajusta los valores de m y b hasta encontrar la línea que mejor se adapte a todos esos datos históricos.

Ejemplo:
Supongamos que el modelo ya aprendió de miles de ventas de autos y encontró la siguiente relación:

Precio del auto = -0.10 * Kilometraje + 20,000

Ahora, si tienes un auto con 100,000 kilómetros y quieres predecir su precio, simplemente usas la fórmula:

Precio = -0.10 * 100,000 + 20,000
Precio = -10,000 + 20,000
Precio = $10,000

El modelo predice que el precio justo para ese auto es de $10,000. Este es el poder de la regresión lineal: tomar datos del pasado para hacer una predicción inteligente sobre el futuro.

