"""
Script simplificado para obtener los datos de evidencia experimental
"""

from itertools import permutations

def costo_total(finca, orden):
    tiempo = 0
    costo = 0
    for idx in orden:
        ts, tr, p = finca[idx]
        fin_riego = tiempo + tr
        retraso = max(0, fin_riego - ts)
        costo += p * retraso
        tiempo = fin_riego
    return costo

def roFB(finca):
    """Fuerza Bruta"""
    n = len(finca)
    mejor_orden = None
    mejor_costo = float('inf')
    
    for perm in permutations(range(n)):
        costo = costo_total(finca, list(perm))
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_orden = list(perm)
    
    return mejor_orden, mejor_costo

def roPV(f):
    """Algoritmo Voraz"""
    claves = []
    for i, (ts, tr, p) in enumerate(f):
        clave = ts / (p * tr)
        claves.append((clave, i))
    
    claves.sort(key=lambda x: x[0])
    orden = [i for (_, i) in claves]
    costo = costo_total(f, orden)
    
    return orden, costo

def comparar_caso(finca, nombre):
    """Compara voraz vs fuerza bruta para un caso"""
    print(f"\n{'='*70}")
    print(f"CASO: {nombre}")
    print(f"{'='*70}")
    
    # Voraz
    orden_v, costo_v = roPV(finca)
    print(f"VORAZ:        Π = ⟨{','.join(map(str, orden_v))}⟩  Costo = {costo_v}")
    
    # Fuerza Bruta
    orden_fb, costo_fb = roFB(finca)
    print(f"FUERZA BRUTA: Π = ⟨{','.join(map(str, orden_fb))}⟩  Costo = {costo_fb}")
    
    # Comparación
    es_optima = (costo_v == costo_fb)
    diferencia = costo_v - costo_fb
    
    if es_optima:
        print(f"✅ ES ÓPTIMA")
    else:
        print(f"❌ NO ES ÓPTIMA (diferencia: +{diferencia})")
    
    return {
        'nombre': nombre,
        'n': len(finca),
        'voraz': {'orden': orden_v, 'costo': costo_v},
        'optima': {'orden': orden_fb, 'costo': costo_fb},
        'es_optima': es_optima,
        'diferencia': diferencia
    }

# CASOS DE PRUEBA
casos = [
    ([(10, 3, 4), (5, 3, 3), (2, 2, 1), (8, 1, 1), (6, 4, 2)], "F₁"),
    ([(9, 3, 4), (5, 3, 3), (2, 2, 1), (8, 1, 1), (6, 4, 2)], "F₂"),
    ([(8, 2, 1), (7, 2, 2), (6, 2, 3), (5, 2, 4)], "F₃"),
    ([(5, 1, 1), (5, 2, 2), (5, 3, 3), (5, 4, 4)], "F₄"),
    ([(10, 3, 1), (8, 3, 2), (6, 3, 3), (4, 3, 4)], "F₅"),
    ([(20, 5, 1), (3, 1, 4), (15, 3, 2)], "F₆"),
]

if __name__ == "__main__":
    print("\n" + "="*70)
    print("COMPARACIÓN VORAZ VS FUERZA BRUTA")
    print("="*70)
    
    resultados = []
    for finca, nombre in casos:
        resultado = comparar_caso(finca, nombre)
        resultados.append(resultado)
    
    # TABLA RESUMEN MARKDOWN
    print("\n\n" + "="*70)
    print("TABLA PARA COPIAR EN MARKDOWN:")
    print("="*70 + "\n")
    
    print("| Caso | n | Π (Voraz) | Costo Voraz | Π (Óptima) | Costo Óptimo | ¿Óptima? |")
    print("|------|---|-----------|-------------|------------|--------------|----------|")
    
    for r in resultados:
        v_orden = f"⟨{','.join(map(str, r['voraz']['orden']))}⟩"
        o_orden = f"⟨{','.join(map(str, r['optima']['orden']))}⟩"
        es_opt = "SÍ ✓" if r['es_optima'] else "NO ✗"
        
        print(f"| {r['nombre']:<4} | {r['n']} | {v_orden:<9} | {r['voraz']['costo']:<11} | {o_orden:<10} | {r['optima']['costo']:<12} | {es_opt:<8} |")
    
    # ESTADÍSTICAS
    print("\n\n" + "="*70)
    print("ESTADÍSTICAS:")
    print("="*70)
    
    optimas = sum(1 for r in resultados if r['es_optima'])
    no_optimas = len(resultados) - optimas
    
    print(f"✅ Casos óptimos: {optimas}/{len(resultados)} ({100*optimas/len(resultados):.1f}%)")
    print(f"❌ Casos NO óptimos: {no_optimas}/{len(resultados)} ({100*no_optimas/len(resultados):.1f}%)")
    
    if no_optimas > 0:
        diferencias = [r['diferencia'] for r in resultados if not r['es_optima']]
        print(f"📊 Diferencia promedio: {sum(diferencias)/len(diferencias):.2f}")
        print(f"📊 Diferencia máxima: {max(diferencias)}")
        
        print("\nCasos donde NO es óptima:")
        for r in resultados:
            if not r['es_optima']:
                print(f"  - {r['nombre']}: voraz={r['voraz']['costo']}, óptimo={r['optima']['costo']} (diferencia: +{r['diferencia']})")