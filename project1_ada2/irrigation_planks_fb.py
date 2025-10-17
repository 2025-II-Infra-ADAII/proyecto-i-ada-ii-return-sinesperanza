"""
Algoritmo de Fuerza Bruta para el problema de riego óptimo.
Genera todas las permutaciones posibles y selecciona la de menor costo.
"""


def permute_yield(nums):
    """
    Generador que produce todas las permutaciones posibles de nums.
    Implementado con backtracking in-place, sin usar itertools.

    Args:
        nums (list): Lista de elementos a permutar

    Yields:
        list: Cada permutación como lista

    Complejidad: O(n!) permutaciones, O(n) espacio recursivo
    """

    def backtrack(start=0):
        if start == len(nums):
            yield nums[:]
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                yield from backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

    yield from backtrack()


def calcular_costo(finca, perm):
    """
    Calcula el costo total CRF_Π para una permutación dada.

    Fórmula:
        - t*_πj = t*_π(j-1) + tr_π(j-1)  para j > 0
        - CRF_Π[i] = p_i · max(0, (t*_i + tr_i) - ts_i)
        - CRF_Π = Σ CRF_Π[i]

    Args:
        finca (list): Lista de tablones [[ts, tr, p], ...]
        perm (list): Permutación (orden de riego) como lista de índices

    Returns:
        int: Costo total de la permutación

    Complejidad: O(n)
    """
    n = len(finca)
    tiempos_inicio = [0] * n

    # Calcular tiempos de inicio para cada tablón según la permutación
    for j in range(1, n):
        idx_anterior = perm[j - 1]
        tr_anterior = finca[idx_anterior][1]
        tiempos_inicio[j] = tiempos_inicio[j - 1] + tr_anterior

    # Calcular costo total
    costo_total = 0
    for j, idx_tablon in enumerate(perm):
        ts, tr, p = finca[idx_tablon]
        tiempo_inicio = tiempos_inicio[j]
        tiempo_fin_riego = tiempo_inicio + tr

        # Penalización = prioridad × días de retraso (si hay retraso)
        retraso = max(0, tiempo_fin_riego - ts)
        penalizacion = p * retraso
        costo_total += penalizacion

    return costo_total


def roFB(finca):
    """
    Algoritmo de Fuerza Bruta para el problema de riego óptimo.
    Genera todas las permutaciones posibles de los tablones y elige la de menor costo.

    Args:
        finca (list): Lista de tablones [[ts, tr, p], ...]
                     donde ts = tiempo supervivencia
                           tr = tiempo regado
                           p = prioridad (1-4)

    Returns:
        tuple: (mejor_permutacion, mejor_costo)
               - mejor_permutacion: lista de índices en orden óptimo
               - mejor_costo: costo mínimo encontrado

    Complejidad temporal: O(n! × n) - genera n! permutaciones y calcula costo O(n) cada una
    Complejidad espacial: O(n) - almacena permutación actual y mejor

    Ejemplo:
        >>> finca = [[10, 3, 4], [5, 3, 3], [2, 2, 1]]
        >>> perm, costo = roFB(finca)
        >>> print(f"Orden: {perm}, Costo: {costo}")
    """
    n = len(finca)
    indices = list(range(n))

    mejor_perm = None
    mejor_costo = float('inf')

    # Generar todas las permutaciones y evaluar cada una
    for perm in permute_yield(indices):
        costo = calcular_costo(finca, perm)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_perm = perm[:]  # Copiar la permutación

    return mejor_perm, mejor_costo


# ============================================================================
# PRUEBA DIRECTA (opcional, para testing rápido sin el menú principal)
# ============================================================================
if __name__ == "__main__":
    # Ejemplo del PDF (F1)
    finca_ejemplo = [
        [10, 3, 4],  # Tablón 0: ts=10, tr=3, p=4
        [5, 3, 3],  # Tablón 1: ts=5, tr=3, p=3
        [2, 2, 1],  # Tablón 2: ts=2, tr=2, p=1
        [8, 1, 1],  # Tablón 3: ts=8, tr=1, p=1
        [6, 4, 2]  # Tablón 4: ts=6, tr=4, p=2
    ]

    print("🔍 Probando Fuerza Bruta con ejemplo del PDF...")
    print(f"Finca: {len(finca_ejemplo)} tablones")

    mejor_perm, mejor_costo = roFB(finca_ejemplo)

    print(f"\n✅ Resultado:")
    print(f"   Orden óptimo: {mejor_perm}")
    print(f"   Costo mínimo: {mejor_costo}")
    print(f"\n   (Se espera: orden=[2, 1, 3, 0, 4], costo=14)")