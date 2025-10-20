def costo_total(finca, orden): #Funcion auxiliar para calcular el costo total dada una permutación
    tiempo = 0
    costo = 0
    for idx in orden:
        ts, tr, p = finca[idx]
        fin_riego = tiempo + tr
        retraso = max(0, fin_riego - ts)
        costo += p * retraso
        tiempo = fin_riego
    return costo



def roPV(f):
    """Algoritmo voraz para el plan de riego óptimo.
        Estrategia: ordenar los tablones por ts / (p * tr) (menor primero).
    
    Parámetros:
        finca: lista de tuplas (ts, tr, p)
    
    Retorna:
        (orden, costo_total)"""
    
    # Calculamos la clave voraz para cada tablón
    claves = []
    for i, (ts, tr, p) in enumerate(f):
        clave = ts / (p * tr)
        claves.append((clave, i))
    
    # Ordenamos por la clave (de menor a mayor)
    claves.sort(key=lambda x: x[0])
    
    # Obtenemos el orden de índices según el criterio voraz
    orden = [i for (_, i) in claves]
    
    # Calculamos el costo total usando la función auxiliar
    costo = costo_total(f, orden)
    
    return (orden, costo)




if __name__ == "__main__":
    roPV()