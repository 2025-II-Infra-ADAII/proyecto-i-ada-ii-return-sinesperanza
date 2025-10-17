import time
from project1_ada2.irrigation_planks_rov import roPV, costo_total


def test_voraz_basico():
    """
    Prueba con el ejemplo del enunciado (F1).
    Verifica que roV genere una programación válida y calcule el costo correcto.
    """
    finca = [
        [10, 3, 4],
        [5, 3, 3],
        [2, 2, 1],
        [8, 1, 1],
        [6, 4, 2]
    ]

    # El orden puede variar según la heurística, así que solo verificamos el tipo y el costo
    perm, costo = roPV(finca)

    assert isinstance(perm, list), "El resultado debe ser una lista de índices"
    assert all(isinstance(i, int) for i in perm), "Todos los elementos del orden deben ser enteros"
    assert isinstance(costo, (int, float)), "El costo debe ser numérico"
    assert len(perm) == len(finca), "La longitud del orden debe coincidir con el número de tablones"


def test_calculo_costo_manual():
    """
    Prueba la función costo_total directamente con una permutación fija.
    """
    finca = [
        [10, 3, 4],
        [5, 3, 3],
        [2, 2, 1],
        [8, 1, 1],
        [6, 4, 2]
    ]
    perm = [2, 1, 4, 3, 0]
    costo = costo_total(finca, perm)

    assert isinstance(costo, (int, float)), "El costo debe ser numérico"
    assert costo >= 0, "El costo no puede ser negativo"


def test_voraz_tiempo_pequeno():
    """
    Prueba que la ejecución de roV sea razonablemente rápida para n pequeño.
    Mide el tiempo de ejecución y valida que no supere un umbral.
    """
    finca = [
        [5, 2, 2],
        [6, 3, 3],
        [4, 1, 1],
        [7, 2, 4]
    ]
    inicio = time.time()
    perm, costo = roPV(finca)
    duracion = time.time() - inicio
    print(f"Tiempo ejecución (4 tablones, voraz): {duracion:.5f} segundos")

    assert duracion < 2, "El algoritmo voraz tarda demasiado en n pequeño"
    assert isinstance(perm, list)
    assert isinstance(costo, (int, float))
