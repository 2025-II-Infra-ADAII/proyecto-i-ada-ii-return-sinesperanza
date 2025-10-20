"""
scripts/generar_graficos_pd.py

Script para generar TODOS los gráficos del análisis experimental del algoritmo
de Programación Dinámica (roPD).

Uso desde la raíz del proyecto:
    python scripts/generar_graficos_pd.py
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import time
import math

# ============================================================================
# CONFIGURACIÓN DE RUTAS
# ============================================================================

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'project1_ada2'))

print(f"📁 Proyecto: {PROJECT_ROOT}")
print(f"📁 Buscando algoritmos en: {os.path.join(PROJECT_ROOT, 'project1_ada2')}\n")

try:
    from irrigation_plants_pd import roPD
    print("✅ Función 'roPD' importada correctamente\n")
except ImportError as e:
    print(f"❌ Error al importar: {e}")
    sys.exit(1)


# ============================================================================
# GENERACIÓN DE DATOS DE PRUEBA
# ============================================================================

def generar_finca_aleatoria(n, seed=None):
    """Genera una finca aleatoria para pruebas"""
    if seed is not None:
        np.random.seed(seed)
    finca = [[np.random.randint(5, 15),
              np.random.randint(1, 5),
              np.random.randint(1, 5)] for _ in range(n)]
    return finca


# ============================================================================
# MEDICIÓN DE TIEMPOS
# ============================================================================

def medir_tiempos(tamanios, repeticiones=5):
    """Mide tiempos de ejecución del algoritmo de Programación Dinámica"""
    resultados = {}

    print("=" * 70)
    print("⏱️  MIDIENDO TIEMPOS DE EJECUCIÓN (PROGRAMACIÓN DINÁMICA)")
    print("=" * 70)

    for n in tamanios:
        print(f"\n📊 n={n}")
        tiempos = []

        for rep in range(repeticiones):
            finca = generar_finca_aleatoria(n, seed=rep)
            inicio = time.perf_counter()
            roPD(finca)
            fin = time.perf_counter()
            tiempo = fin - inicio
            tiempos.append(tiempo)
            print(f"   Rep {rep+1}/{repeticiones}: {tiempo:.6f} seg")

        promedio = np.mean(tiempos)
        std = np.std(tiempos)
        resultados[n] = {'tiempos': tiempos, 'promedio': promedio, 'std': std}
        print(f"   ✅ Promedio: {promedio:.6f} ± {std:.6f} seg")

    return resultados


# ============================================================================
# GRÁFICOS
# ============================================================================

def crear_grafico_teorico_vs_experimental(resultados, carpeta_salida):
    """Gráfico comparativo (teórico O(n·2ⁿ) vs experimental)"""
    plt.figure(figsize=(12, 7))

    ns = sorted(resultados.keys())
    promedios = [resultados[n]['promedio'] for n in ns]

    # Modelo teórico O(n * 2^n)
    teorico = [n * (2 ** n) for n in ns]

    # Normalización desde el punto medio
    idx_central = len(ns) // 2
    factor_normalizacion = promedios[idx_central] / teorico[idx_central]
    teorico_normalizado = [t * factor_normalizacion for t in teorico]

    plt.plot(ns, promedios, 'o-b', linewidth=2, markersize=8, label='Experimental (segundos)', zorder=3)
    plt.plot(ns, teorico_normalizado, '-', color='lightcoral', linewidth=2.5,
             label=r'Teórico (O($n·2^n$)) normalizado', zorder=2)

    plt.yscale('log')
    plt.xlabel('Tamaño del problema (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Tiempo (s, escala logarítmica)', fontsize=12, fontweight='bold')
    plt.title('Comparación Solapada: Costo Teórico vs. Tiempo Experimental (Programación Dinámica)',
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.tight_layout()

    ruta = os.path.join(carpeta_salida, 'grafico_teorico_vs_experimental_pd.png')
    plt.savefig(ruta, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Gráfico comparativo guardado: {ruta}")


def crear_grafico_tiempo_lineal(resultados, carpeta_salida):
    """Gráfico: Tiempo vs n (escala lineal)"""
    plt.figure(figsize=(10, 6))
    ns = sorted(resultados.keys())
    promedios = [resultados[n]['promedio'] for n in ns]
    stds = [resultados[n]['std'] for n in ns]

    plt.errorbar(ns, promedios, yerr=stds, marker='o', capsize=5,
                 linewidth=2.5, color='#118AB2', ecolor='#073B4C', label='Tiempo promedio')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.title('Programación Dinámica: Tiempo de Ejecución vs. Tamaño (Lineal)')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend()
    plt.tight_layout()

    ruta = os.path.join(carpeta_salida, 'grafico_tiempo_lineal_pd.png')
    plt.savefig(ruta, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Gráfico lineal guardado: {ruta}")


def crear_grafico_tiempo_log(resultados, carpeta_salida):
    """Gráfico: Tiempo vs n (escala logarítmica)"""
    plt.figure(figsize=(10, 6))
    ns = sorted(resultados.keys())
    promedios = [resultados[n]['promedio'] for n in ns]

    plt.plot(ns, promedios, 's-', linewidth=2.5, markersize=9, color='#FFD166', label='Tiempo experimental')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (s, escala log)')
    plt.title('Crecimiento del Algoritmo de Programación Dinámica (Escala Logarítmica)')
    plt.grid(True, which="both", linestyle='--', alpha=0.3)
    plt.legend()
    plt.tight_layout()

    ruta = os.path.join(carpeta_salida, 'grafico_tiempo_log_pd.png')
    plt.savefig(ruta, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Gráfico logarítmico guardado: {ruta}")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    print("=" * 70)
    print("🎨 GENERADOR DE GRÁFICOS - PROGRAMACIÓN DINÁMICA")
    print("=" * 70)

    carpeta_imagenes = os.path.join(PROJECT_ROOT, 'docs', 'imagenes')
    os.makedirs(carpeta_imagenes, exist_ok=True)
    print(f"📁 Carpeta de salida: {carpeta_imagenes}\n")

    # 🔧 Valores razonables para PD (evitar explosión exponencial)
    tamanios = [5, 6, 7, 8, 9, 10, 11]
    repeticiones = 5

    print("⚙️  CONFIGURACIÓN DE PRUEBAS")
    print(f"Tamaños: {tamanios}")
    print(f"Repeticiones: {repeticiones}\n")
    input("Presiona ENTER para iniciar...\n")

    resultados = medir_tiempos(tamanios, repeticiones)

    print("\n📊 Generando gráficos...\n")
    crear_grafico_tiempo_lineal(resultados, carpeta_imagenes)
    crear_grafico_tiempo_log(resultados, carpeta_imagenes)
    crear_grafico_teorico_vs_experimental(resultados, carpeta_imagenes)

    print("\n🎉 ¡Proceso completado!")
    print("Archivos generados en docs/imagenes/")
    print("  • grafico_tiempo_lineal_pd.png")
    print("  • grafico_tiempo_log_pd.png")
    print("  • grafico_teorico_vs_experimental_pd.png")


if __name__ == "__main__":
    main()
