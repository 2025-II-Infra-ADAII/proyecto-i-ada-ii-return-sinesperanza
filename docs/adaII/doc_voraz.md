# 4.2 Solución mediante Algoritmo Voraz

## 4.2.1 Descripción del Algoritmo

### Criterio de Selección (Decisión Voraz)

Nuestro algoritmo voraz utiliza la siguiente clave de ordenamiento para determinar el orden en que se deben regar los tablones:

$$\text{clave}_i = \frac{ts_i}{p_i \cdot tr_i}$$

Donde:
- $ts_i$ es el tiempo de supervivencia del tablón $i$
- $p_i$ es la prioridad del tablón $i$
- $tr_i$ es el tiempo de regado del tablón $i$

### Intuición del Criterio

La estrategia voraz ordena los tablones de **menor a mayor** según esta clave. La intuición detrás de este criterio es:

- **Numerador ($ts_i$)**: Representa el tiempo disponible antes de que el tablón sufra. Un valor alto indica que el tablón puede esperar más tiempo.
- **Denominador ($p_i \cdot tr_i$)**: Representa el "costo potencial" del tablón, combinando su prioridad (importancia) con el tiempo que consumirá el riego.

**Interpretación**: Al ordenar por esta razón de menor a mayor, priorizamos tablones que tienen poco tiempo de supervivencia en relación con su costo de riego ponderado por prioridad. En otras palabras, atendemos primero aquellos tablones más "urgentes" relativos a su impacto.

### Algoritmo Paso a Paso

1. **Calcular claves**: Para cada tablón $i$, calcular $\text{clave}_i = \frac{ts_i}{p_i \cdot tr_i}$
2. **Ordenar**: Ordenar los tablones por clave de menor a mayor
3. **Construir permutación**: Obtener la secuencia de índices según el ordenamiento
4. **Calcular costo**: Evaluar el costo total de la programación resultante

### Pseudocódigo

```
Algoritmo RiegoVoraz(F)
Entrada: F = lista de tablones [(ts₀, tr₀, p₀), ..., (tsₙ₋₁, trₙ₋₁, pₙ₋₁)]
Salida: (Π, CRF_Π) donde Π es la permutación y CRF_Π su costo

1. claves ← lista vacía
2. Para i desde 0 hasta n-1:
     clave ← ts[i] / (p[i] * tr[i])
     Agregar (clave, i) a claves
3. Ordenar claves por el primer componente (ascendente)
4. Π ← [i para cada (_, i) en claves]
5. CRF_Π ← CalcularCostoTotal(F, Π)
6. Retornar (Π, CRF_Π)

Función CalcularCostoTotal(F, Π)
1. tiempo ← 0
2. costo ← 0
3. Para cada índice idx en Π:
     (ts, tr, p) ← F[idx]
     fin_riego ← tiempo + tr
     retraso ← máx(0, fin_riego - ts)
     costo ← costo + p * retraso
     tiempo ← fin_riego
4. Retornar costo
```

---

## 4.2.2 Verificación del Algoritmo

### Ejemplo 1

**Entrada:**
$$F_1 = \langle \langle 10, 3, 4 \rangle, \langle 5, 3, 3 \rangle, \langle 2, 2, 1 \rangle, \langle 8, 1, 1 \rangle, \langle 6, 4, 2 \rangle \rangle$$

**Cálculo de claves:**

| Tablón | $ts_i$ | $tr_i$ | $p_i$ | $\text{clave}_i = \frac{ts_i}{p_i \cdot tr_i}$ | Valor |
|--------|--------|--------|-------|------------------------------------------------|-------|
| 0      | 10     | 3      | 4     | $\frac{10}{4 \cdot 3} = \frac{10}{12}$        | 0.833 |
| 1      | 5      | 3      | 3     | $\frac{5}{3 \cdot 3} = \frac{5}{9}$           | 0.556 |
| 2      | 2      | 2      | 1     | $\frac{2}{1 \cdot 2} = \frac{2}{2}$           | 1.000 |
| 3      | 8      | 1      | 1     | $\frac{8}{1 \cdot 1} = \frac{8}{1}$           | 8.000 |
| 4      | 6      | 4      | 2     | $\frac{6}{2 \cdot 4} = \frac{6}{8}$           | 0.750 |

**Ordenamiento por clave (menor a mayor):**
$$\Pi_{\text{voraz}} = \langle 1, 4, 0, 2, 3 \rangle$$

**Cálculo de tiempos de inicio y costos:**

| Tablón ($\pi_j$) | $ts$ | $tr$ | $p$ | $t^*_{\pi_j}$ | $t^*_{\pi_j} + tr$ | Retraso | Penalización |
|------------------|------|------|-----|---------------|--------------------|---------|--------------| 
| 1                | 5    | 3    | 3   | 0             | 3                  | 0       | 0            |
| 4                | 6    | 4    | 2   | 3             | 7                  | 1       | 2            |
| 0                | 10   | 3    | 4   | 7             | 10                 | 0       | 0            |
| 2                | 2    | 2    | 1   | 10            | 12                 | 10      | 10           |
| 3                | 8    | 1    | 1   | 12            | 13                 | 5       | 5            |

**Costo total:** 
$$CRF_{\Pi_{\text{voraz}}} = 0 + 2 + 0 + 10 + 5 = 17$$

**Comparación con solución óptima (Fuerza Bruta):**
- Costo voraz: 17
- Costo óptimo: [COMPLETAR después de ejecutar fuerza bruta]
- ¿Es óptima?: [SÍ/NO]

---

### Ejemplo 2

**Entrada:**
$$F_2 = \langle \langle 9, 3, 4 \rangle, \langle 5, 3, 3 \rangle, \langle 2, 2, 1 \rangle, \langle 8, 1, 1 \rangle, \langle 6, 4, 2 \rangle \rangle$$

**Cálculo de claves:**

| Tablón | $ts_i$ | $tr_i$ | $p_i$ | $\text{clave}_i = \frac{ts_i}{p_i \cdot tr_i}$ | Valor |
|--------|--------|--------|-------|------------------------------------------------|-------|
| 0      | 9      | 3      | 4     | $\frac{9}{4 \cdot 3} = \frac{9}{12}$          | 0.750 |
| 1      | 5      | 3      | 3     | $\frac{5}{3 \cdot 3} = \frac{5}{9}$           | 0.556 |
| 2      | 2      | 2      | 1     | $\frac{2}{1 \cdot 2} = \frac{2}{2}$           | 1.000 |
| 3      | 8      | 1      | 1     | $\frac{8}{1 \cdot 1} = \frac{8}{1}$           | 8.000 |
| 4      | 6      | 4      | 2     | $\frac{6}{2 \cdot 4} = \frac{6}{8}$           | 0.750 |

**Ordenamiento por clave (menor a mayor):**
$$\Pi_{\text{voraz}} = \langle 1, 0, 4, 2, 3 \rangle$$
(Nota: tablones 0 y 4 tienen la misma clave, el orden entre ellos depende del algoritmo de ordenamiento estable)

**Cálculo de tiempos de inicio y costos:**

| Tablón ($\pi_j$) | $ts$ | $tr$ | $p$ | $t^*_{\pi_j}$ | $t^*_{\pi_j} + tr$ | Retraso | Penalización |
|------------------|------|------|-----|---------------|--------------------|---------|--------------| 
| 1                | 5    | 3    | 3   | 0             | 3                  | 0       | 0            |
| 0                | 9    | 3    | 4   | 3             | 6                  | 0       | 0            |
| 4                | 6    | 4    | 2   | 6             | 10                 | 4       | 8            |
| 2                | 2    | 2    | 1   | 10            | 12                 | 10      | 10           |
| 3                | 8    | 1    | 1   | 12            | 13                 | 5       | 5            |

**Costo total:** 
$$CRF_{\Pi_{\text{voraz}}} = 0 + 0 + 8 + 10 + 5 = 23$$

**Comparación con solución óptima (Fuerza Bruta):**
- Costo voraz: 23
- Costo óptimo: [COMPLETAR después de ejecutar fuerza bruta]
- ¿Es óptima?: [SÍ/NO]

---

### Casos de Prueba Adicionales

Se diseñaron 4 casos de prueba adicionales para verificar el comportamiento del algoritmo voraz:

#### Caso de Prueba 1: Tablones con prioridades crecientes
**Entrada:**
```
F₃ = ⟨⟨8, 2, 1⟩, ⟨7, 2, 2⟩, ⟨6, 2, 3⟩, ⟨5, 2, 4⟩⟩
```

[COMPLETAR CON RESULTADOS]

#### Caso de Prueba 2: Tablones con tiempos de supervivencia iguales
**Entrada:**
```
F₄ = ⟨⟨5, 1, 1⟩, ⟨5, 2, 2⟩, ⟨5, 3, 3⟩, ⟨5, 4, 4⟩⟩
```

[COMPLETAR CON RESULTADOS]

#### Caso de Prueba 3: Tablones con tiempos de regado iguales
**Entrada:**
```
F₅ = ⟨⟨10, 3, 1⟩, ⟨8, 3, 2⟩, ⟨6, 3, 3⟩, ⟨4, 3, 4⟩⟩
```

[COMPLETAR CON RESULTADOS]

#### Caso de Prueba 4: Caso con posible no-optimalidad
**Entrada:**
```
F₆ = ⟨⟨20, 5, 1⟩, ⟨3, 1, 4⟩, ⟨15, 3, 2⟩⟩
```

[COMPLETAR CON RESULTADOS]

### Tabla Resumen de Resultados

| Caso | Tamaño (n) | Solución Voraz (Π) | Costo Voraz | Solución Óptima (Π) | Costo Óptimo | ¿Es Óptima? |
|------|------------|-------------------|-------------|---------------------|--------------|-------------|
| F₁   | 5          | ⟨1,4,0,2,3⟩       | 17          | [COMPLETAR]         | [COMPLETAR]  | [SÍ/NO]     |
| F₂   | 5          | ⟨1,0,4,2,3⟩       | 23          | [COMPLETAR]         | [COMPLETAR]  | [SÍ/NO]     |
| F₃   | 4          | [COMPLETAR]       | [COMPLETAR] | [COMPLETAR]         | [COMPLETAR]  | [SÍ/NO]     |
| F₄   | 4          | [COMPLETAR]       | [COMPLETAR] | [COMPLETAR]         | [COMPLETAR]  | [SÍ/NO]     |
| F₅   | 4          | [COMPLETAR]       | [COMPLETAR] | [COMPLETAR]         | [COMPLETAR]  | [SÍ/NO]     |
| F₆   | 3          | [COMPLETAR]       | [COMPLETAR] | [COMPLETAR]         | [COMPLETAR]  | [SÍ/NO]     |

---

## 4.2.3 Análisis de Complejidad

### Complejidad Temporal

Analizamos cada parte del algoritmo:

**1. Cálculo de claves:**
```python
for i, (ts, tr, p) in enumerate(f):
    clave = ts / (p * tr)
    claves.append((clave, i))
```
- Se itera sobre los $n$ tablones: $O(n)$
- Cada operación (división, append) es $O(1)$
- **Subtotal:** $O(n)$

**2. Ordenamiento:**
```python
claves.sort(key=lambda x: x[0])
```
- Utiliza el algoritmo de ordenamiento de Python (Timsort)
- **Subtotal:** $O(n \log n)$

**3. Construcción del orden:**
```python
orden = [i for (_, i) in claves]
```
- Comprensión de lista sobre $n$ elementos: $O(n)$
- **Subtotal:** $O(n)$

**4. Cálculo del costo total:**
```python
for idx in orden:
    ts, tr, p = finca[idx]
    fin_riego = tiempo + tr
    retraso = max(0, fin_riego - ts)
    costo += p * retraso
    tiempo = fin_riego
```
- Se itera sobre los $n$ tablones: $O(n)$
- Cada operación dentro del bucle es $O(1)$
- **Subtotal:** $O(n)$

### Complejidad Total

$$T(n) = O(n) + O(n \log n) + O(n) + O(n) = O(n \log n)$$

La complejidad temporal del algoritmo voraz es **$O(n \log n)$**, dominada por la operación de ordenamiento.

### Complejidad Espacial

- **Lista de claves:** $O(n)$ para almacenar tuplas (clave, índice)
- **Lista de orden:** $O(n)$ para la permutación resultante
- **Variables auxiliares:** $O(1)$

**Complejidad espacial total:** $O(n)$

---

## 4.2.4 Análisis de Corrección

### ¿El algoritmo voraz siempre encuentra la solución óptima?

**Respuesta:** [A COMPLETAR después de analizar los resultados de las pruebas]

### Argumentos Teóricos

[INCLUIR ANÁLISIS BASADO EN:]
- Propiedad de elección voraz
- Subestructura óptima
- Si se cumple o no el criterio de optimalidad

### Evidencia Experimental

Basándonos en los casos de prueba:

1. **Ejemplo 1 (F₁):** [COMPLETAR - comparar con fuerza bruta]
2. **Ejemplo 2 (F₂):** [COMPLETAR - comparar con fuerza bruta]
3. **Casos adicionales:** De los 4 casos diseñados, el algoritmo voraz encontró la solución óptima en [X] de ellos.

### Conclusión sobre Optimalidad

[COMPLETAR CON UNA DE ESTAS OPCIONES:]

**Opción A - Si es óptimo:**
El algoritmo voraz propuesto encuentra la solución óptima en todos los casos analizados. Esto sugiere que el criterio $\frac{ts_i}{p_i \cdot tr_i}$ captura efectivamente la urgencia relativa de los tablones...

**Opción B - Si NO es óptimo:**
El algoritmo voraz NO garantiza encontrar la solución óptima en todos los casos. 

**Contraejemplo:**
[Presentar aquí un caso concreto donde la solución voraz no coincide con la óptima, mostrando ambas soluciones y sus costos]

**Razón:** El criterio voraz toma decisiones locales sin considerar el impacto global en tablones posteriores...

---

## 4.2.5 Implementación

### Función Principal

```python
def roPV(f):
    """
    Algoritmo voraz para el plan de riego óptimo.
    
    Estrategia: ordenar los tablones por ts / (p * tr) (menor primero).
    
    Parámetros:
        f: lista de tuplas (ts, tr, p) representando los tablones
    
    Retorna:
        tupla (orden, costo_total) donde:
        - orden: lista con los índices de tablones en orden de riego
        - costo_total: costo total de la programación
    """
    # Calculamos la clave voraz para cada tablón
    claves = []
    for i, (ts, tr, p) in enumerate(f):
        clave = ts / (p * tr)  # Criterio voraz: menor urgencia relativa
        claves.append((clave, i))
    
    # Ordenamos por la clave (de menor a mayor)
    claves.sort(key=lambda x: x[0])
    
    # Obtenemos el orden de índices según el criterio voraz
    orden = [i for (_, i) in claves]
    
    # Calculamos el costo total usando la función auxiliar
    costo = costo_total(f, orden)
    
    return (orden, costo)
```

### Función Auxiliar para Cálculo de Costo

```python
def costo_total(finca, orden):
    """
    Calcula el costo total de riego dada una permutación.
    
    Parámetros:
        finca: lista de tuplas (ts, tr, p)
        orden: lista de índices representando el orden de riego
    
    Retorna:
        costo total según la fórmula CRF_Π
    """
    tiempo = 0  # Tiempo acumulado
    costo = 0   # Costo total acumulado
    
    for idx in orden:
        ts, tr, p = finca[idx]
        fin_riego = tiempo + tr  # Momento en que termina el riego
        retraso = max(0, fin_riego - ts)  # Días de retraso respecto a ts
        costo += p * retraso  # Penalización ponderada por prioridad
        tiempo = fin_riego  # Actualizamos el tiempo para el siguiente tablón
    
    return costo
```

### Notas de Implementación

1. **Manejo de división por cero:** En la práctica, asumimos que $p_i > 0$ y $tr_i > 0$ según la naturaleza del problema. Si fuera necesario, se podría agregar validación.

2. **Ordenamiento estable:** Python's `sort()` es estable, por lo que tablones con la misma clave mantienen su orden relativo original.

3. **Eficiencia:** La implementación evita cálculos redundantes y utiliza estructuras de datos simples.

---

## Referencias de Código

- Archivo: `src/voraz.py` (o la ruta correspondiente en tu proyecto)
- Funciones: `roPV()`, `costo_total()`