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
- Solución voraz: $\Pi_{voraz} = \langle 1, 4, 0, 2, 3 \rangle$
- Costo voraz: **17**
- Solución óptima: $\Pi_{óptima} = \langle 2, 1, 3, 0, 4 \rangle$
- Costo óptimo: **14**
- **¿Es óptima?: NO ✗** (diferencia: +3)

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


---

### Casos de Prueba Adicionales

Se diseñaron 4 casos de prueba adicionales para verificar el comportamiento del algoritmo voraz:

---

#### Caso de Prueba 3 (F₃): Tablones con prioridades crecientes

**Entrada:**
```
F₃ = ⟨⟨8, 2, 1⟩, ⟨7, 2, 2⟩, ⟨6, 2, 3⟩, ⟨5, 2, 4⟩⟩
```

**Descripción:** Este caso prueba cómo se comporta el algoritmo cuando las prioridades aumentan uniformemente.

**Cálculo de claves voraz:**

| Tablón | $ts$ | $tr$ | $p$ | $\text{clave} = \frac{ts}{p \cdot tr}$ | Valor |
|--------|------|------|-----|----------------------------------------|-------|
| 0      | 8    | 2    | 1   | $\frac{8}{1 \times 2} = 4.0$          | 4.000 |
| 1      | 7    | 2    | 2   | $\frac{7}{2 \times 2} = 1.75$         | 1.750 |
| 2      | 6    | 2    | 3   | $\frac{6}{3 \times 2} = 1.0$          | 1.000 |
| 3      | 5    | 2    | 4   | $\frac{5}{4 \times 2} = 0.625$        | 0.625 |

**Solución Voraz:**
- Orden: $\Pi_{voraz} = \langle 3, 2, 1, 0 \rangle$ (ordenado por clave ascendente)
- Costo: **0**

**Tabla de cálculo:**

| Tablón ($\pi_j$) | $ts$ | $tr$ | $p$ | $t^*$ | $t^* + tr$ | Retraso | Penalización |
|------------------|------|------|-----|-------|------------|---------|--------------|
| 3                | 5    | 2    | 4   | 0     | 2          | 0       | 0            |
| 2                | 6    | 2    | 3   | 2     | 4          | 0       | 0            |
| 1                | 7    | 2    | 2   | 4     | 6          | 0       | 0            |
| 0                | 8    | 2    | 1   | 6     | 8          | 0       | 0            |

**Solución Óptima (Fuerza Bruta):**
- Orden: $\Pi_{óptima} = \langle 1, 3, 2, 0 \rangle$
- Costo: **0**

**Resultado:** ✅ **SÍ es óptima** (ambas soluciones tienen costo 0)

**Análisis:** Como todos los tablones tienen el mismo tiempo de regado ($tr=2$) y los tiempos de supervivencia disminuyen, cualquier orden que los riegue antes de sus límites logra costo 0.

---

#### Caso de Prueba 4 (F₄): Tablones con tiempos de supervivencia iguales

**Entrada:**
```
F₄ = ⟨⟨5, 1, 1⟩, ⟨5, 2, 2⟩, ⟨5, 3, 3⟩, ⟨5, 4, 4⟩⟩
```

**Descripción:** Todos los tablones tienen el mismo tiempo de supervivencia ($ts=5$), pero diferentes tiempos de regado y prioridades.

**Cálculo de claves voraz:**

| Tablón | $ts$ | $tr$ | $p$ | $\text{clave} = \frac{ts}{p \cdot tr}$ | Valor |
|--------|------|------|-----|----------------------------------------|-------|
| 0      | 5    | 1    | 1   | $\frac{5}{1 \times 1} = 5.0$          | 5.000 |
| 1      | 5    | 2    | 2   | $\frac{5}{2 \times 2} = 1.25$         | 1.250 |
| 2      | 5    | 3    | 3   | $\frac{5}{3 \times 3} = 0.556$        | 0.556 |
| 3      | 5    | 4    | 4   | $\frac{5}{4 \times 4} = 0.3125$       | 0.313 |

**Solución Voraz:**
- Orden: $\Pi_{voraz} = \langle 3, 2, 1, 0 \rangle$ (ordenado por clave ascendente)
- Costo: **19**

**Tabla de cálculo:**

| Tablón ($\pi_j$) | $ts$ | $tr$ | $p$ | $t^*$ | $t^* + tr$ | Retraso | Penalización |
|------------------|------|------|-----|-------|------------|---------|--------------|
| 3                | 5    | 4    | 4   | 0     | 4          | 0       | 0            |
| 2                | 5    | 3    | 3   | 4     | 7          | 2       | 6            |
| 1                | 5    | 2    | 2   | 7     | 9          | 4       | 8            |
| 0                | 5    | 1    | 1   | 9     | 10         | 5       | 5            |

**Costo total:** $0 + 6 + 8 + 5 = 19$

**Solución Óptima (Fuerza Bruta):**
- Orden: $\Pi_{óptima} = \langle 0, 3, 1, 2 \rangle$
- Costo: **19**

**Resultado:** ✅ **SÍ es óptima** (ambas soluciones tienen costo 19)

**Análisis:** Aunque las permutaciones son diferentes, ambas logran el mismo costo óptimo. Esto demuestra que puede haber múltiples soluciones óptimas.

---

#### Caso de Prueba 5 (F₅): Tablones con tiempos de regado iguales

**Entrada:**
```
F₅ = ⟨⟨10, 3, 1⟩, ⟨8, 3, 2⟩, ⟨6, 3, 3⟩, ⟨4, 3, 4⟩⟩
```

**Descripción:** Todos los tablones tienen el mismo tiempo de regado ($tr=3$), con tiempos de supervivencia decrecientes y prioridades crecientes.

**Cálculo de claves voraz:**

| Tablón | $ts$ | $tr$ | $p$ | $\text{clave} = \frac{ts}{p \cdot tr}$ | Valor |
|--------|------|------|-----|----------------------------------------|-------|
| 0      | 10   | 3    | 1   | $\frac{10}{1 \times 3} = 3.333$       | 3.333 |
| 1      | 8    | 3    | 2   | $\frac{8}{2 \times 3} = 1.333$        | 1.333 |
| 2      | 6    | 3    | 3   | $\frac{6}{3 \times 3} = 0.667$        | 0.667 |
| 3      | 4    | 3    | 4   | $\frac{4}{4 \times 3} = 0.333$        | 0.333 |

**Solución Voraz:**
- Orden: $\Pi_{voraz} = \langle 3, 2, 1, 0 \rangle$ (ordenado por clave ascendente)
- Costo: **4**

**Tabla de cálculo:**

| Tablón ($\pi_j$) | $ts$ | $tr$ | $p$ | $t^*$ | $t^* + tr$ | Retraso | Penalización |
|------------------|------|------|-----|-------|------------|---------|--------------|
| 3                | 4    | 3    | 4   | 0     | 3          | 0       | 0            |
| 2                | 6    | 3    | 3   | 3     | 6          | 0       | 0            |
| 1                | 8    | 3    | 2   | 6     | 9          | 1       | 2            |
| 0                | 10   | 3    | 1   | 9     | 12         | 2       | 2            |

**Costo total:** $0 + 0 + 2 + 2 = 4$

**Solución Óptima (Fuerza Bruta):**
- Orden: $\Pi_{óptima} = \langle 3, 2, 1, 0 \rangle$
- Costo: **4**

**Resultado:** ✅ **SÍ es óptima** (soluciones idénticas)

**Análisis:** El algoritmo voraz encontró exactamente la solución óptima. Con tiempos de regado iguales, ordenar por urgencia ponderada funciona correctamente.

---

#### Caso de Prueba 6 (F₆): Caso extremo

**Entrada:**
```
F₆ = ⟨⟨20, 5, 1⟩, ⟨3, 1, 4⟩, ⟨15, 3, 2⟩⟩
```

**Descripción:** Caso diseñado con contrastes fuertes: un tablón muy urgente ($ts=3$) con alta prioridad, versus tablones con mayor tiempo de supervivencia.

**Cálculo de claves voraz:**

| Tablón | $ts$ | $tr$ | $p$ | $\text{clave} = \frac{ts}{p \cdot tr}$ | Valor |
|--------|------|------|-----|----------------------------------------|-------|
| 0      | 20   | 5    | 1   | $\frac{20}{1 \times 5} = 4.0$         | 4.000 |
| 1      | 3    | 1    | 4   | $\frac{3}{4 \times 1} = 0.75$         | 0.750 |
| 2      | 15   | 3    | 2   | $\frac{15}{2 \times 3} = 2.5$         | 2.500 |

**Solución Voraz:**
- Orden: $\Pi_{voraz} = \langle 1, 2, 0 \rangle$ (ordenado por clave ascendente)
- Costo: **0**

**Tabla de cálculo:**

| Tablón ($\pi_j$) | $ts$ | $tr$ | $p$ | $t^*$ | $t^* + tr$ | Retraso | Penalización |
|------------------|------|------|-----|-------|------------|---------|--------------|
| 1                | 3    | 1    | 4   | 0     | 1          | 0       | 0            |
| 2                | 15   | 3    | 2   | 1     | 4          | 0       | 0            |
| 0                | 20   | 5    | 1   | 4     | 9          | 0       | 0            |

**Costo total:** $0 + 0 + 0 = 0$

**Solución Óptima (Fuerza Bruta):**
- Orden: $\Pi_{óptima} = \langle 1, 0, 2 \rangle$
- Costo: **0**

**Resultado:** ✅ **SÍ es óptima** (ambas soluciones tienen costo 0)

**Análisis:** Múltiples ordenamientos logran costo 0. El tablón 1 debe ir primero (muy urgente), pero el orden de 0 y 2 es flexible ya que ambos tienen suficiente tiempo de supervivencia.

---

### Tabla Resumen de Resultados

| Caso | Tamaño (n) | Solución Voraz (Π) | Costo Voraz | Solución Óptima (Π) | Costo Óptimo | ¿Es Óptima? |
|------|------------|-------------------|-------------|---------------------|--------------|-------------|
| F₁   | 5          | ⟨1,4,0,2,3⟩       | 17          | ⟨2,1,3,0,4⟩         | 14           | NO ✗        |
| F₂   | 5          | ⟨1,0,4,2,3⟩       | 23          | ⟨2,1,3,0,4⟩         | 14           | NO ✗        |
| F₃   | 4          | ⟨3,2,1,0⟩         | 0           | ⟨1,3,2,0⟩           | 0            | SÍ ✓        |
| F₄   | 4          | ⟨3,2,1,0⟩         | 19          | ⟨0,3,1,2⟩           | 19           | SÍ ✓        |
| F₅   | 4          | ⟨3,2,1,0⟩         | 4           | ⟨3,2,1,0⟩           | 4            | SÍ ✓        |
| F₆   | 3          | ⟨1,2,0⟩           | 0           | ⟨1,0,2⟩             | 0            | SÍ ✓        |

---

### Análisis de Resultados

**Observaciones clave:**

1. **Casos óptimos (4/6):** F₃, F₄, F₅, F₆
   - El algoritmo voraz funciona bien cuando hay patrones claros o cuando múltiples soluciones son óptimas

2. **Casos NO óptimos (2/6):** F₁, F₂
   - Ambos involucran tablones con bajo $ts$ pero baja prioridad
   - El criterio voraz subestima la urgencia extrema de estos tablones

3. **Patrón del fallo:**
   - Ocurre cuando hay tablones con $ts$ muy bajo (urgente) pero $p$ bajo (baja prioridad)
   - El denominador $p \cdot tr$ hace que estos tablones tengan clave alta, postergándolos
   - La postergación causa que superen su $ts$, acumulando penalizaciones

4. **Peor caso:** F₂ con diferencia de +9 (64% peor que el óptimo)

**Conclusión:** El algoritmo voraz es efectivo en muchos casos prácticos, pero no garantiza optimalidad cuando existen trade-offs complejos entre urgencia y prioridad.

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

**Respuesta:** NO SIEMPRE encuentra la solución óptima (depende del problema y del criterio voraz)
¿Por qué?

Toma decisiones locales (elige lo mejor en cada paso)
No reconsidera decisiones pasadas
Puede quedarse en una solución "buena" pero no óptima

### Argumentos Teóricos

Para que un algoritmo voraz garantice encontrar la solución óptima, debe cumplir dos propiedades fundamentales: **propiedad de elección voraz** y **subestructura óptima**.

#### 1. Propiedad de Elección Voraz

**Definición:** Una solución óptima global puede construirse tomando decisiones locales óptimas (voraces).

**Análisis para nuestro criterio:**

Nuestro algoritmo ordena por $\frac{ts_i}{p_i \cdot tr_i}$ asumiendo que regar primero los tablones con menor razón minimiza el costo global. Sin embargo, este criterio **toma decisiones miopes** que no consideran el impacto completo en el resto de la secuencia.

**Problema:** El criterio no considera que:
- Retrasar un tablón de baja prioridad puede ser aceptable si permite atender uno de alta prioridad a tiempo
- Un tablón con $ts$ muy bajo (urgente) pero baja prioridad puede acumular penalizaciones significativas si se posterga demasiado
- La interacción entre tiempos de regado consecutivos crea efectos no lineales en las penalizaciones

Por lo tanto, **NO se cumple la propiedad de elección voraz** para este criterio, como lo demuestran los casos F₁ y F₂.

#### 2. Subestructura Óptima

**Definición:** Una solución óptima al problema contiene soluciones óptimas a sus subproblemas.

**Análisis:**

El problema de riego **SÍ tiene subestructura óptima**: si $\Pi^* = \langle \pi_0, \pi_1, ..., \pi_{n-1} \rangle$ es óptima, entonces $\Pi' = \langle \pi_1, ..., \pi_{n-1} \rangle$ debe ser óptima para el subproblema de regar los $n-1$ tablones restantes, iniciando en el tiempo $t_{\pi_0}^* + tr_{\pi_0}$.

**¿Por qué?** Si existiera una mejor forma de ordenar los $n-1$ tablones restantes, podríamos combinarla con $\pi_0$ y obtener una solución mejor que $\Pi^*$, contradiciendo que $\Pi^*$ es óptima.

Esta propiedad se cumple, lo que hace al problema adecuado para **programación dinámica**, pero no garantiza que **un criterio voraz específico** encuentre el óptimo.

#### 3. Por qué el Criterio Voraz Falla

**Limitación fundamental:** El criterio $\frac{ts_i}{p_i \cdot tr_i}$ asume que la urgencia relativa es independiente del orden global, pero en realidad:

1. **Dependencia temporal:** El tiempo disponible para cada tablón depende de cuánto tiempo consumieron los tablones previos
2. **Efectos acumulativos:** Decisiones tempranas afectan las penalizaciones de todos los tablones posteriores
3. **No monotonicidad:** Un tablón "menos urgente" según el criterio puede volverse crítico si se retrasa lo suficiente

**Ejemplo del fallo (Caso F₁):**
- **Tablón 2:** $ts=2$, $tr=2$, $p=1$ → clave = $\frac{2}{1 \times 2} = 1.0$
- **Tablón 1:** $ts=5$, $tr=3$, $p=3$ → clave = $\frac{5}{3 \times 3} = 0.556$

El voraz elige el Tablón 1 primero (clave menor = 0.556). Pero el Tablón 2 es **extremadamente urgente** ($ts=2$ muy bajo). Aunque tiene baja prioridad, si se posterga demasiado acumula retraso significativo.

**En la solución óptima:** Se riega el Tablón 2 primero ($\pi_0 = 2$), evitando que supere su $ts=2$, a pesar de tener menor "urgencia ponderada" según el criterio voraz.

#### 4. Conclusión Teórica

El algoritmo voraz propuesto **no garantiza optimalidad** porque:
- ✗ No cumple la propiedad de elección voraz
- ✓ Sí cumple subestructura óptima (útil para programación dinámica)
- ✗ El criterio local no captura las interdependencias temporales del problema

Sin embargo, es una **heurística eficiente** que:
- Tiene complejidad $O(n \log n)$ (muy rápida)
- Produce soluciones de buena calidad en el 66.7% de los casos analizados
- La diferencia promedio con el óptimo es relativamente pequeña (6 unidades)
- Es útil como aproximación inicial o cuando $n$ es muy grande para métodos exactos

### Evidencia Experimental

Basándonos en los casos de prueba ejecutados, comparamos las soluciones del algoritmo voraz con las soluciones óptimas obtenidas mediante fuerza bruta:

#### Resumen de Resultados

| Caso | n | Π (Voraz) | Costo Voraz | Π (Óptima) | Costo Óptimo | ¿Óptima? |
|------|---|-----------|-------------|------------|--------------|----------|
| F₁   | 5 | ⟨1,4,0,2,3⟩ | 17 | ⟨2,1,3,0,4⟩ | 14 | NO ✗ |
| F₂   | 5 | ⟨1,0,4,2,3⟩ | 23 | ⟨2,1,3,0,4⟩ | 14 | NO ✗ |
| F₃   | 4 | ⟨3,2,1,0⟩ | 0 | ⟨1,3,2,0⟩ | 0 | SÍ ✓ |
| F₄   | 4 | ⟨3,2,1,0⟩ | 19 | ⟨0,3,1,2⟩ | 19 | SÍ ✓ |
| F₅   | 4 | ⟨3,2,1,0⟩ | 4 | ⟨3,2,1,0⟩ | 4 | SÍ ✓ |
| F₆   | 3 | ⟨1,2,0⟩ | 0 | ⟨1,0,2⟩ | 0 | SÍ ✓ |

#### Análisis por Caso

##### 1. Ejemplo 1 (F₁)

**Entrada:** $F_1 = \langle \langle 10,3,4 \rangle, \langle 5,3,3 \rangle, \langle 2,2,1 \rangle, \langle 8,1,1 \rangle, \langle 6,4,2 \rangle \rangle$

**Solución Voraz:**
- Permutación: $\Pi_{voraz} = \langle 1, 4, 0, 2, 3 \rangle$
- Costo: $CRF_{voraz} = 17$


---

##### 2. Ejemplo 2 (F₂)

**Entrada:** $F_2 = \langle \langle 9,3,4 \rangle, \langle 5,3,3 \rangle, \langle 2,2,1 \rangle, \langle 8,1,1 \rangle, \langle 6,4,2 \rangle \rangle$

**Solución Voraz:**
- Permutación: $\Pi_{voraz} = \langle 1, 0, 4, 2, 3 \rangle$
- Costo: $CRF_{voraz} = 23$


---

##### 3. Caso de Prueba 3 (F₃): Prioridades Crecientes

**Entrada:** $F_3 = \langle \langle 8,2,1 \rangle, \langle 7,2,2 \rangle, \langle 6,2,3 \rangle, \langle 5,2,4 \rangle \rangle$

**Solución Voraz:**
- Permutación: $\Pi_{voraz} = \langle 3, 2, 1, 0 \rangle$
- Costo: $CRF_{voraz} = 0$

**Solución Óptima (Fuerza Bruta):**
- Permutación: $\Pi_{óptima} = \langle 1, 3, 2, 0 \rangle$
- Costo: $CRF_{óptima} = 0$

**Resultado:** SÍ es óptima (ambas soluciones tienen costo 0)

---

##### 4. Caso de Prueba 4 (F₄): Tiempos de Supervivencia Iguales

**Entrada:** $F_4 = \langle \langle 5,1,1 \rangle, \langle 5,2,2 \rangle, \langle 5,3,3 \rangle, \langle 5,4,4 \rangle \rangle$

**Solución Voraz:**
- Permutación: $\Pi_{voraz} = \langle 3, 2, 1, 0 \rangle$
- Costo: $CRF_{voraz} = 19$

**Solución Óptima (Fuerza Bruta):**
- Permutación: $\Pi_{óptima} = \langle 0, 3, 1, 2 \rangle$
- Costo: $CRF_{óptima} = 19$

**Resultado:** SÍ es óptima (ambas soluciones tienen costo 19)

---

##### 5. Caso de Prueba 5 (F₅): Tiempos de Regado Iguales

**Entrada:** $F_5 = \langle \langle 10,3,1 \rangle, \langle 8,3,2 \rangle, \langle 6,3,3 \rangle, \langle 4,3,4 \rangle \rangle$

**Solución Voraz:**
- Permutación: $\Pi_{voraz} = \langle 3, 2, 1, 0 \rangle$
- Costo: $CRF_{voraz} = 4$

**Solución Óptima (Fuerza Bruta):**
- Permutación: $\Pi_{óptima} = \langle 3, 2, 1, 0 \rangle$
- Costo: $CRF_{óptima} = 4$

**Resultado:** SÍ es óptima (soluciones idénticas)

---

##### 6. Caso de Prueba 6 (F₆): Caso Extremo

**Entrada:** $F_6 = \langle \langle 20,5,1 \rangle, \langle 3,1,4 \rangle, \langle 15,3,2 \rangle \rangle$

**Solución Voraz:**
- Permutación: $\Pi_{voraz} = \langle 1, 2, 0 \rangle$
- Costo: $CRF_{voraz} = 0$

**Solución Óptima (Fuerza Bruta):**
- Permutación: $\Pi_{óptima} = \langle 1, 0, 2 \rangle$
- Costo: $CRF_{óptima} = 0$

**Resultado:** SÍ es óptima (ambas soluciones tienen costo 0)

---

#### Estadísticas Generales

De los **6 casos de prueba** analizados:
- ✅ Casos donde el voraz es óptimo: **4/6** (66.7%)
- ❌ Casos donde el voraz NO es óptimo: **2/6** (33.3%)
- 📊 Diferencia promedio cuando no es óptimo: **6.0** unidades de costo
- 📊 Diferencia máxima: **9** unidades de costo (Caso F₂)

### Conclusión sobre Optimalidad

**El algoritmo voraz propuesto NO garantiza encontrar la solución óptima en todos los casos.**

Basándonos en la evidencia experimental:
- El algoritmo encontró la solución óptima en 4 de 6 casos (66.7%)
- Falló en 2 casos (F₁ y F₂), con diferencias de +3 y +9 respectivamente

### Contraejemplo Concreto

**Caso F₁:** Demuestra que el criterio voraz no siempre es óptimo

**Entrada:**
$F_1 = \langle \langle 10,3,4 \rangle, \langle 5,3,3 \rangle, \langle 2,2,1 \rangle, \langle 8,1,1 \rangle, \langle 6,4,2 \rangle \rangle$

**Solución Voraz:**
- Orden: $\Pi_{voraz} = \langle 1, 4, 0, 2, 3 \rangle$
- Costo: **17**

**Solución Óptima:**
- Orden: $\Pi_{óptima} = \langle 2, 1, 3, 0, 4 \rangle$
- Costo: **14**

**Diferencia:** El algoritmo voraz produce una solución **3 unidades más costosa** (21.4% peor) que el óptimo.

### Análisis del Fallo

El criterio voraz $\frac{ts_i}{p_i \cdot tr_i}$ toma decisiones locales que no consideran el impacto global en la secuencia completa:

1. **Tablón 2** ($\langle 2,2,1 \rangle$): 
   - Tiene muy bajo $ts=2$ (urgente)
   - Pero tiene baja prioridad $p=1$ (bajo impacto)
   - El voraz lo posterga mucho, acumulando penalización

2. **En la solución óptima**: Se riega el tablón 2 **primero** ($\pi_0 = 2$), evitando que sufra retrasos a pesar de su baja prioridad, porque su urgencia extrema ($ts=2$) lo hace crítico.

3. **Error del criterio**: Al ponderar por $p \cdot tr$ en el denominador, el algoritmo subestima la urgencia de tablones con baja prioridad pero tiempo de supervivencia muy corto.

### Razón Teórica del Fallo

El problema de riego óptimo **no cumple la propiedad de elección voraz** para este criterio porque:

- Las penalizaciones son **acumulativas y dependientes del tiempo**: un tablón que se riega tarde afecta a todos los posteriores
- El criterio **no captura las interdependencias temporales**: decidir regar un tablón antes afecta los tiempos de inicio de todos los siguientes
- Existen **trade-offs complejos**: a veces es mejor atender primero un tablón "menos urgente" según la métrica local para optimizar el costo global

Por lo tanto, el algoritmo voraz es una **heurística eficiente** pero no óptima.

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

- Funciones: `roPV()`, `costo_total()`