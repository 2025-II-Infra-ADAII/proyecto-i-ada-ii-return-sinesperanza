# Informe de Complejidad — Problema de la Mochila 0/1

En este informe se presentan los análisis de **complejidad temporal** y **espacial** de las soluciones implementadas al problema de la mochila: fuerza bruta, programación dinámica y algoritmo voraz. Se utilizará notación matemática estándar para expresar el costo en función del número de objetos \(n\) y la capacidad de la mochila \(W\).

---

## 1. Fuerza bruta (solución ingenua)

### Complejidad temporal

La fuerza bruta consiste en explorar absolutamente todas las combinaciones posibles de los objetos.  
Cada objeto puede **incluirse o no incluirse** en la mochila, lo que genera un total de:
\[
2^n
\]
subconjuntos.

Para cada subconjunto, se debe calcular el peso y el valor total, lo cual implica recorrer hasta \(n\) elementos. En el peor caso, se hace este recorrido en todas las combinaciones, resultando en:
\[
T(n) = O(n \cdot 2^n)
\]

Esto significa que el algoritmo escala **exponencialmente**: un aumento modesto en el número de objetos hace que el tiempo de ejecución crezca de manera incontrolable. Por ejemplo, con \(n=30\), ya se tendrían más de mil millones de combinaciones a evaluar. Por eso, esta solución solo es viable para instancias muy pequeñas del problema.

### Complejidad espacial

El algoritmo mantiene:

- La lista de objetos: \(O(n)\).
- Una lista temporal para almacenar subconjuntos (se libera al final de cada iteración).

Por tanto:
\[
S(n) = O(n)
\]

---

## 2. Programación dinámica

### Complejidad temporal

La programación dinámica construye una tabla de tamaño \((n+1) \times (W+1)\).  
Para cada uno de los \(n\) objetos, se recorren todas las capacidades parciales de la mochila (de 1 a \(W\)). Cada celda se calcula en tiempo constante, tomando el máximo entre incluir o no incluir el objeto. Por lo tanto:
\[
T(n, W) = O(n \cdot W)
\]

Esto significa que el tiempo crece de manera **lineal con respecto a \(n\)**, pero también depende de \(W\). Como \(W\) es un parámetro numérico y no una dimensión natural del input, se dice que esta complejidad es **pseudopolinomial**: parece polinómica, pero en realidad depende del valor numérico de la capacidad de la mochila. Si \(W\) es muy grande, el tiempo de ejecución se vuelve prohibitivo incluso para valores moderados de \(n\).

### Complejidad espacial

- La tabla \(V\) requiere:
  \[
  S(n, W) = O(n \cdot W)
  \]
- Puede optimizarse guardando solo dos filas (fila actual y anterior), reduciendo a:
  \[
  S\_{\text{optimizado}}(W) = O(W)
  \]

---

## 3. Algoritmo voraz (greedy por razón valor/peso)

### Complejidad temporal

El algoritmo voraz comienza calculando la razón valor/peso de cada objeto, lo que requiere:
\[
O(n)
\]

Luego, se ordenan los objetos según esta razón, lo cual domina el costo total, ya que el ordenamiento eficiente requiere:
\[
O(n \log n)
\]

Finalmente, se recorre la lista ordenada para llenar la mochila, con un costo lineal:
\[
O(n)
\]

Por tanto, la complejidad total es:
\[
T(n) = O(n \log n)
\]

Esto convierte al algoritmo voraz en el más eficiente en tiempo entre las tres aproximaciones. Sin embargo, a diferencia de la programación dinámica, no garantiza la solución óptima, ya que tomar siempre el objeto con mejor razón local no asegura la mejor combinación global.

### Complejidad espacial

- Lista de objetos con razón valor/peso: \(O(n)\).
- No se requiere matriz adicional.

Así:
\[
S(n) = O(n)
\]

---

## 4. Resumen comparativo

| Estrategia            | Complejidad temporal | Complejidad espacial                   |
| --------------------- | -------------------- | -------------------------------------- |
| Fuerza bruta          | \(O(n \cdot 2^n)\)   | \(O(n)\)                               |
| Programación dinámica | \(O(n \cdot W)\)     | \(O(n \cdot W)\) ó \(O(W)\) optimizado |
| Voraz                 | \(O(n \log n)\)      | \(O(n)\)                               |

---

### 4.1 Analisis mediante gráficas

Comparacion teorica de complejidades en tiempo y espacio para las tres estrategias implementadas.

! [Comparativa de tiempo](../imagenes/g1.png)

Analisis de DP con W con n fijo

! [Comparativa DP](../imagenes/g2.png)

Recordar incluir la comparacion de tiempos con respecto a lo implementado. No se incluye en este ejemplo.

## 5. Conclusiones

- La **fuerza bruta** es inviable para \(n\) moderados debido a su crecimiento exponencial.
- La **programación dinámica** es óptima en exactitud, pero depende de \(W\), lo que puede ser prohibitivo si \(W\) es muy grande (pseudopolinomial).
- El **algoritmo voraz** es eficiente en tiempo y espacio, pero no garantiza la solución óptima.
