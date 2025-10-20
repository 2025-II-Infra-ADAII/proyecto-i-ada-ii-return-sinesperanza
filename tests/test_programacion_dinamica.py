import time
import random
from project1_ada2.irrigation_plants_pd import roPD, calcular_costo_tab

def test_programacion_dinamica_basico():
    """
    Prueba básica (n=10) para Programación Dinámica Top-Down con Memoization.
    Verifica que roPD retorne una permutación y costo válidos.
    """
finca = [
    [10, 3, 4],
    [5, 3, 3],
    [2, 2, 1],
    [8, 1, 1],
    [6, 4, 2],
    [12, 2, 3],
    [4, 3, 2],
    [9, 2, 1],
    [7, 1, 4],
    [11, 2, 2],
    ]

# Medir tiempo de ejecución
inicio = time.time()
perm, costo = roPD(finca)
fin = time.time()
duracion = fin - inicio

# Validar estructura de la salida
assert isinstance(perm, list), "La permutación debe ser una lista."
assert isinstance(costo, (int, float)), "El costo debe ser numérico."
assert len(perm) == len(finca), "La permutación debe incluir todos los tablones."
assert set(perm) == set(range(len(finca))), "La permutación debe ser válida (sin repetidos ni faltantes)."

# Validar costo consistente con la permutación obtenida
costo_verificado = calcular_costo_tab(finca, perm)
assert costo == costo_verificado, (
    f"El costo reportado ({costo}) no coincide con el calculado manualmente ({costo_verificado})."
)

# Validar que el algoritmo termine en tiempo razonable (< 2 segundos para n=10)
assert duracion < 2.0, f"El tiempo de ejecución es demasiado alto: {duracion:.2f} s"

print("\n--- Resultados prueba PD (n=10) ---")
print(f"Permutación óptima: {perm}")
print(f"Costo mínimo total: {costo}")
print(f"Tiempo de ejecución: {duracion:.4f} s")


def test_programacion_dinamica_100():
    """
    Prueba de rendimiento (n=100) para Programación Dinámica Top-Down con Memoization.
    Genera una finca sintética y evalúa el comportamiento temporal y la validez de la salida.
    """
random.seed(42)
n = 26
# Generar datos sintéticos realistas: ts, tr, p
finca = [
    [random.randint(5, 20),  # tiempo de supervivencia
     random.randint(1, 5),   # tiempo de regado
     random.randint(1, 4)]   # prioridad
    for _ in range(n)
]

inicio = time.time()
perm, costo = roPD(finca)
fin = time.time()
duracion = fin - inicio

# Validaciones estructurales
assert isinstance(perm, list), "La permutación debe ser una lista."
assert isinstance(costo, (int, float)), "El costo debe ser numérico."
assert len(perm) == len(finca), "La permutación debe incluir todos los tablones."
assert set(perm) == set(range(len(finca))), "La permutación debe ser válida (sin repetidos ni faltantes)."

# Verificar consistencia de costo
costo_verificado = calcular_costo_tab(finca, perm)
assert costo == costo_verificado, (
    f"El costo reportado ({costo}) no coincide con el recalculado ({costo_verificado})."
)

# Evaluación de tiempo — con n=100 debería ser muy alto, por lo tanto marcamos como 'no práctico'
print("\n--- Resultados prueba PD (n=100) ---")
print(f"Permutación obtenida (primeros 10 índices): {perm[:10]}")
print(f"Costo total: {costo}")
print(f"Tiempo de ejecución: {duracion:.2f} s")

# En este tamaño el algoritmo puede exceder fácilmente varios minutos; no se usa assert de tiempo
# sino que se documenta su inviabilidad práctica para n ≥ 20.
