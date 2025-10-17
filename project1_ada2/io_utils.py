"""
Módulo de utilidades para lectura y escritura de archivos.
Maneja el formato de entrada/salida del problema de riego óptimo.
"""


def leer_finca(ruta_archivo):
    """
    Lee el archivo de entrada y retorna la finca como lista de listas.

    Formato esperado:
        n
        ts0,tr0,p0
        ts1,tr1,p1
        ...
        ts(n-1),tr(n-1),p(n-1)

    Args:
        ruta_archivo (str o Path): Ruta al archivo de entrada

    Returns:
        list: Lista de listas [[ts, tr, p], ...] representando cada tablón

    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si el formato del archivo es incorrecto
    """
    try:
        with open(ruta_archivo, "r") as f:
            lineas = [line.strip() for line in f.readlines() if line.strip()]

        if len(lineas) == 0:
            raise ValueError("El archivo está vacío")

        n = int(lineas[0])

        if len(lineas) < n + 1:
            raise ValueError(f"Se esperaban {n} tablones pero solo hay {len(lineas) - 1} líneas")

        finca = []
        for i, linea in enumerate(lineas[1:n + 1], start=1):
            try:
                valores = linea.split(",")
                if len(valores) != 3:
                    raise ValueError(f"Línea {i + 1}: se esperaban 3 valores separados por comas")

                ts, tr, p = map(int, valores)

                # Validaciones básicas
                if ts < 0 or tr < 0 or p < 1 or p > 4:
                    raise ValueError(f"Línea {i + 1}: valores fuera de rango (ts≥0, tr≥0, 1≤p≤4)")

                finca.append([ts, tr, p])
            except ValueError as e:
                raise ValueError(f"Error en línea {i + 1}: {str(e)}")

        return finca

    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
    except Exception as e:
        raise Exception(f"Error al leer el archivo: {str(e)}")


def escribir_salida(ruta_archivo, perm, costo):
    """
    Escribe el resultado en el archivo de salida.

    Formato de salida:
        Costo
        pi0
        pi1
        ...
        pi(n-1)

    Args:
        ruta_archivo (str o Path): Ruta al archivo de salida
        perm (list): Lista con el orden de riego (índices de tablones)
        costo (int/float): Costo total de la solución

    Raises:
        IOError: Si no se puede escribir el archivo
    """
    try:
        with open(ruta_archivo, "w") as f:
            f.write(str(costo) + "\n")
            for indice in perm:
                f.write(str(indice) + "\n")
    except Exception as e:
        raise IOError(f"Error al escribir el archivo de salida: {str(e)}")


def validar_finca(finca):
    """
    Valida que la estructura de la finca sea correcta.

    Args:
        finca (list): Lista de listas [[ts, tr, p], ...]

    Returns:
        bool: True si es válida

    Raises:
        ValueError: Si la estructura es inválida
    """
    if not isinstance(finca, list) or len(finca) == 0:
        raise ValueError("La finca debe ser una lista no vacía")

    for i, tablon in enumerate(finca):
        if not isinstance(tablon, list) or len(tablon) != 3:
            raise ValueError(f"Tablón {i}: debe ser una lista de 3 elementos [ts, tr, p]")

        ts, tr, p = tablon
        if not all(isinstance(x, int) for x in tablon):
            raise ValueError(f"Tablón {i}: todos los valores deben ser enteros")

        if ts < 0 or tr < 0:
            raise ValueError(f"Tablón {i}: ts y tr deben ser no negativos")

        if p < 1 or p > 4:
            raise ValueError(f"Tablón {i}: prioridad p debe estar entre 1 y 4")

    return True