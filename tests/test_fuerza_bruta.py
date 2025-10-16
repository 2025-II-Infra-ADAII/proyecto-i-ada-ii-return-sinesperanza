import time
from project1_ada2.irrigation_planks_fb import roFB, calcular_costo

def test_fuerza_bruta_basico():
    """
    Prueba con el ejemplo del enunciado (F1).
    Verifica que roFB encuentre la permutación y costo óptimos.
    """
    finca = [
        [10, 3, 4],
        [5, 3, 3],
        [2, 2, 1],
        [8, 1, 1],
        [6, 4, 2]
    ]

    esperado_orden = [2, 1, 3, 0, 4]
    esperado_costo = 14

    perm, costo = roFB(finca)

    assert perm == esperado_orden, f"Orden esperado {esperado_orden}, obtenido {perm}"
    assert costo == esperado_costo, f"Costo esperado {esperado_costo}, obtenido {costo}"


def test_calcular_costo_manual():
    """
    Prueba la función calcular_costo directamente con una permutación fija.
    """
    finca = [
        [10, 3, 4],
        [5, 3, 3],
        [2, 2, 1],
        [8, 1, 1],
        [6, 4, 2]
    ]
    perm = [2, 1, 3, 0, 4]
    costo = calcular_costo(finca, perm)
    assert costo == 14
    assert isinstance(costo, int)


def test_fuerza_bruta_tiempo_pequeno():
    """
    Prueba que la ejecución de roFB sea razonablemente rápida para n pequeño.
    Mide el tiempo de ejecución y valida que no supere un umbral.
    """
    finca = [
        [5, 2, 2],
        [6, 3, 3],
        [4, 1, 1],
        [7, 2, 4]
    ]
    inicio = time.time()
    perm, costo = roFB(finca)
    duracion = time.time() - inicio
    print(f"Tiempo ejecución (4 tablones): {duracion:.5f} segundos")

    assert duracion < 5, "El algoritmo de fuerza bruta tarda demasiado en n pequeño"
    assert isinstance(perm, list)
    assert isinstance(costo, (int, float))
