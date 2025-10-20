import time
import random
from project1_ada2.irrigation_planks_rov import roPV, costo_total


# ---------------------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------------------
def medir_tiempo(func, *args):
    """Ejecuta una función y devuelve (resultado, duración_en_segundos)."""
    inicio = time.time()
    resultado = func(*args)
    fin = time.time()
    return resultado, fin - inicio


def imprimir_tiempo(nombre_algoritmo, n, duracion):
    """Imprime en formato uniforme el tiempo medido."""
    print(f"[{nombre_algoritmo}] -> {n} tablones: {duracion:.5f} segundos")


def generar_finca(n):
    """Genera una finca aleatoria con n tablones."""
    finca = []
    for _ in range(n):
        ts = random.randint(5, 1000)
        tr = random.randint(1, 10)
        p = random.randint(1, 4)
        finca.append([ts, tr, p])
    return finca


# ---------------------------------------------------------------------
# TEST 1: Caso básico del enunciado
# ---------------------------------------------------------------------
def test_voraz_basico():
    finca = [
        [10, 3, 4],
        [5, 3, 3],
        [2, 2, 1],
        [8, 1, 1],
        [6, 4, 2]
    ]

    (perm, costo), duracion = medir_tiempo(roPV, finca)
    imprimir_tiempo("Voraz - Básico", len(finca), duracion)

    assert isinstance(perm, list), "El resultado debe ser una lista de índices"
    assert all(isinstance(i, int) for i in perm), "Todos los elementos del orden deben ser enteros"
    assert isinstance(costo, (int, float)), "El costo debe ser numérico"
    assert len(perm) == len(finca), "La longitud del orden debe coincidir con el número de tablones"
    assert duracion < 1.0, "El algoritmo voraz tardó demasiado en un caso pequeño"


# ---------------------------------------------------------------------
# TEST 2: Validación del cálculo del costo
# ---------------------------------------------------------------------
def test_calculo_costo_manual():
    finca = [
        [10, 3, 4],
        [5, 3, 3],
        [2, 2, 1],
        [8, 1, 1],
        [6, 4, 2]
    ]
    perm = [2, 1, 4, 3, 0]

    costo, duracion = medir_tiempo(costo_total, finca, perm)
    imprimir_tiempo("Cálculo de costo", len(finca), duracion)

    assert isinstance(costo, (int, float)), "El costo debe ser numérico"
    assert costo >= 0, "El costo no puede ser negativo"
    assert duracion < 0.5, "El cálculo de costo fue demasiado lento"


# ---------------------------------------------------------------------
# TEST 3: Desempeño para n pequeño
# ---------------------------------------------------------------------
def test_voraz_tiempo_pequeno():
    finca = [
        [5, 2, 2],
        [6, 3, 3],
        [4, 1, 1],
        [7, 2, 4]
    ]

    (perm, costo), duracion = medir_tiempo(roPV, finca)
    imprimir_tiempo("Voraz - n pequeño", len(finca), duracion)

    assert duracion < 2, "El algoritmo voraz tarda demasiado en n pequeño"
    assert isinstance(perm, list)
    assert isinstance(costo, (int, float))


# ---------------------------------------------------------------------
# TEST 4: Rendimiento para n = 30,000
# ---------------------------------------------------------------------
def test_voraz_rendimiento_grande():
    n = 30000
    finca = generar_finca(n)

    (perm, costo), duracion = medir_tiempo(roPV, finca)
    imprimir_tiempo("Voraz - n grande", n, duracion)

    print(f"   Costo total obtenido: {costo}")

    assert isinstance(perm, list), "La permutación debe ser una lista"
    assert len(perm) == n, "La permutación debe tener la misma cantidad de tablones"
    assert all(isinstance(i, int) for i in perm), "Los índices deben ser enteros"
    assert isinstance(costo, (int, float)), "El costo debe ser numérico"
    assert costo >= 0, "El costo no puede ser negativo"

    # Tiempo límite ajustable según la máquina
    assert duracion < 10, f"El algoritmo tardó demasiado: {duracion:.2f}s"
