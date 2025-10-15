def permute_yield(nums):
    """
    Generador que produce todas las permutaciones posibles de nums.
    Implementado con backtracking in-place, sin usar itertools.
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
    Calcula el costo total CRFΠ para una permutación dada.
    finca: lista de listas [[ts, tr, p], ...]
    perm: lista con el orden de riego (índices)
    """
    tiempos_inicio = [0] * len(finca)
    for j in range(1, len(perm)):
        anterior = perm[j - 1]
        tiempos_inicio[j] = tiempos_inicio[j - 1] + finca[anterior][1]  # tr anterior

    costo_total = 0
    for idx_perm, i in enumerate(perm):
        ts, tr, p = finca[i]
        fin_riego = tiempos_inicio[idx_perm] + tr
        penalizacion = p * max(0, fin_riego - ts)
        costo_total += penalizacion

    return costo_total


def roFB(finca):
    """
    Algoritmo de fuerza bruta para el riego óptimo.
    Genera todas las permutaciones posibles de los tablones y elige la de menor costo.
    Retorna: (mejor_perm, mejor_costo)
    """
    n = len(finca)
    indices = list(range(n))
    mejor_perm = None
    mejor_costo = float('inf')

    for perm in permute_yield(indices):
        costo = calcular_costo(finca, perm)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_perm = perm[:]

    return mejor_perm, mejor_costo


def leer_finca(nombre_archivo):
    """
    Lee el archivo de entrada.
    Formato:
        n
        ts0,tr0,p0
        ts1,tr1,p1
        ...
    Retorna una lista de listas [[ts, tr, p], ...]
    """
    finca = []
    with open(nombre_archivo, "r") as f:
        lineas = [line.strip() for line in f.readlines() if line.strip()]
        n = int(lineas[0])
        for linea in lineas[1:n+1]:
            ts, tr, p = map(int, linea.split(","))
            finca.append([ts, tr, p])
    return finca


def escribir_salida(nombre_archivo, perm, costo):
    """
    Escribe el archivo de salida en formato:
        costo
        pi0
        pi1
        ...
    """
    with open(nombre_archivo, "w") as f:
        f.write(str(costo) + "\n")
        for i in perm:
            f.write(str(i) + "\n")



if __name__ == "__main__":
    # 🔹 Ejemplo de uso
    entrada = "entrada.txt"
    salida = "salida.txt"

    # 1️⃣ Leer finca
    finca = leer_finca(entrada)

    # 2️⃣ Ejecutar fuerza bruta
    mejor_perm, mejor_costo = roFB(finca)

    # 3️⃣ Escribir resultado
    escribir_salida(salida, mejor_perm, mejor_costo)

    print("✅ Proceso completado.")
    print("Mejor orden de riego:", mejor_perm)
    print("Costo mínimo total:", mejor_costo)
    print(f"Resultado guardado en '{salida}'")