from functools import lru_cache
from pathlib import Path


def calcular_costo_tab(finca, perm):
    """
    Calcula el costo total CRFΠ para una permutación dada.
    (Se usa solo para verificar resultados)
    """
    tiempos_inicio = [0] * len(finca)
    for j in range(1, len(perm)):
        anterior = perm[j - 1]
        tiempos_inicio[j] = tiempos_inicio[j - 1] + finca[anterior][1]

    costo_total = 0
    for idx_perm, i in enumerate(perm):
        ts, tr, p = finca[i]
        fin_riego = tiempos_inicio[idx_perm] + tr
        penalizacion = p * max(0, fin_riego - ts)
        costo_total += penalizacion

    return costo_total


def roPD(finca):
    """
    Programación Dinámica (Top-Down con Memoization)
    para resolver el problema del riego óptimo.

    Utiliza DP sobre subconjuntos (bitmask DP).
    Retorna: (mejor_perm, mejor_costo)
    """
    n = len(finca)

    
    # Función recursiva con cache
    @lru_cache(maxsize=None)
    def dp(mask, tiempo_actual):
        """
        Devuelve el costo mínimo posible para regar
        los tablones no incluidos en 'mask', iniciando desde 'tiempo_actual'.
        """
        if mask == (1 << n) - 1:
            return 0  # Todos regados

        mejor_costo = float('inf')

        for i in range(n):
            if not (mask & (1 << i)):  # Si el tablón i aún no fue regado
                ts, tr, p = finca[i]
                fin_riego = tiempo_actual + tr
                penalizacion = p * max(0, fin_riego - ts)
                costo_restante = dp(mask | (1 << i), tiempo_actual + tr)
                costo_total = penalizacion + costo_restante
                mejor_costo = min(mejor_costo, costo_total)

        return mejor_costo


    # Reconstrucción del orden óptimo
    def reconstruir(mask, tiempo_actual):
        if mask == (1 << n) - 1:
            return []

        mejor_i = None
        mejor_costo = float('inf')

        for i in range(n):
            if not (mask & (1 << i)):
                ts, tr, p = finca[i]
                fin_riego = tiempo_actual + tr
                penalizacion = p * max(0, fin_riego - ts)
                costo_restante = dp(mask | (1 << i), tiempo_actual + tr)
                costo_total = penalizacion + costo_restante

                if costo_total < mejor_costo:
                    mejor_costo = costo_total
                    mejor_i = i

        return [mejor_i] + reconstruir(mask | (1 << mejor_i), tiempo_actual + finca[mejor_i][1])

   
    # Resultado final
    mejor_costo = dp(0, 0)
    mejor_perm = reconstruir(0, 0)

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
        for linea in lineas[1:n + 1]:
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


def obtener_ruta_archivo(nombre_archivo, directorio="data"):
    """
    Obtiene la ruta completa de un archivo en el directorio especificado.
    """
    directorio_actual = Path(__file__).parent
    ruta_archivo = directorio_actual.parent / directorio / nombre_archivo
    return ruta_archivo


if __name__ == "__main__":
    # Ejemplo de uso
    entrada = obtener_ruta_archivo("entrada.txt")
    salida = obtener_ruta_archivo("salida_pd.txt")

    if not entrada.exists():
        print(f"Error: No se encontró el archivo {entrada}")
        print("Asegúrate de que el archivo entrada.txt esté en la carpeta 'data'")
        exit(1)

    #Leer finca
    finca = leer_finca(entrada)

    #Ejecutar programación dinámica
    mejor_perm, mejor_costo = roPD(finca)

    #Escribir resultado
    escribir_salida(salida, mejor_perm, mejor_costo)

    print("Proceso completado (Programación Dinámica Top-Down).")
    print("Mejor orden de riego:", mejor_perm)
    print("Costo mínimo total:", mejor_costo)
    print(f"Resultado guardado en '{salida}'")
