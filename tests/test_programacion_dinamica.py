import time
from project1_ada2.irrigation_plants_pd import roPD, calcular_costo_tab


def test_programacion_dinamica_basico():
    """
    Prueba con el ejemplo del enunciado (F1).
    Verifica que roPD encuentre la permutación y costo óptimos.
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

    perm, costo = roPD(finca)

    assert perm == esperado_orden, f"Orden esperado {esperado_orden}, obtenido {perm}"
    assert costo == esperado_costo, f"Costo esperado {esperado_costo}, obtenido {costo}"


def test_calcular_costo_pd_manual():
    """
    Verifica que la función calcular_costo_tab calcule correctamente
    el costo para una permutación fija.
    """
    finca = [
        [10, 3, 4],
        [5, 3, 3],
        [2, 2, 1],
        [8, 1, 1],
        [6, 4, 2]
    ]
    perm = [2, 1, 3, 0, 4]
    costo = calcular_costo_tab(finca, perm)

    assert costo == 14, f"Costo incorrecto: esperado 14, obtenido {costo}"
    assert isinstance(costo, int)


def test_programacion_dinamica_equivalente_a_fuerza_bruta():
    """
    Verifica que roPD produzca el mismo resultado que roFB
    para una finca pequeña (n <= 6).
    """
    finca = [
        [7, 2, 3],
        [5, 1, 2],
        [6, 3, 1]
    ]

    # Resultado esperado obtenido previamente con roFB
    esperado_orden = [1, 0, 2]
    esperado_costo = 6

    perm, costo = roPD(finca) 

    assert perm == esperado_orden, f"Orden esperado {esperado_orden}, obtenido {perm}"
    assert costo == esperado_costo, f"Costo esperado {esperado_costo}, obtenido {costo}"


def test_programacion_dinamica_tiempo_pequeno():
    """
    Prueba de rendimiento: el algoritmo DP debe ser rápido para n pequeño.
    """
    finca = [
        [5, 2, 2],
        [6, 3, 3],
        [4, 1, 1],
        [7, 2, 4]
    ]

    inicio = time.time()
    perm, costo = roPD(finca)
    duracion = time.time() - inicio
    print(f"Tiempo ejecución DP (4 tablones): {duracion:.5f} segundos")

    assert duracion < 3, "El algoritmo DP tarda demasiado en n pequeño"
    assert isinstance(perm, list)
    assert isinstance(costo, (int, float))


def test_programacion_dinamica_tipo_salida():
    """
    Verifica que la salida de roPD tenga el formato correcto:
    una lista de índices y un número como costo.
    """
    finca = [
        [9, 2, 1],
        [5, 1, 3],
        [7, 3, 2]
    ]
    perm, costo = roPD(finca)

    assert isinstance(perm, list), "La permutación debe ser una lista"
    assert all(isinstance(i, int) for i in perm), "Todos los elementos del orden deben ser enteros"
    assert isinstance(costo, (int, float)), "El costo debe ser numérico"
