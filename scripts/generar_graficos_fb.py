"""
scripts/generar_graficos_fb.py

Script para generar TODOS los gráficos del análisis experimental de Fuerza Bruta.
Ejecutar UNA VEZ y listo.

Uso desde la raíz del proyecto:
    python scripts/generar_graficos_fb.py
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import time
import math

# Añadir rutas necesarias al path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'project1_ada2'))  # ← CARPETA DE TUS ALGORITMOS

print(f"📁 Proyecto: {PROJECT_ROOT}")
print(f"📁 Buscando algoritmos en: {os.path.join(PROJECT_ROOT, 'project1_ada2')}\n")

# Importar tus algoritmos
try:
    from irrigation_planks_fb import permute_yield, calcular_costo
    print("✅ Funciones importadas correctamente\n")
except ImportError as e:
    print(f"❌ Error al importar: {e}")
    print(f"⚠️  Verifica:")
    print(f"   1. Que estés en la raíz del proyecto")
    print(f"   2. Que el archivo irrigation_planks_fb.py exista en project1_ada2/")
    print(f"   3. Ejecuta: python scripts/generar_graficos_fb.py\n")
    sys.exit(1)


# ============================================================================
# GENERACIÓN DE DATOS DE PRUEBA
# ============================================================================

def generar_finca_aleatoria(n, seed=None):
    """Genera una finca aleatoria para pruebas"""
    if seed is not None:
        np.random.seed(seed)

    finca = []
    for _ in range(n):
        ts = np.random.randint(5, 15)   # Supervivencia: 5-15 días
        tr = np.random.randint(1, 5)    # Regado: 1-5 días
        p = np.random.randint(1, 5)     # Prioridad: 1-4
        finca.append([ts, tr, p])

    return finca


def roFB_simple(finca):
    """Versión simplificada de roFB para mediciones"""
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


# ============================================================================
# MEDICIÓN DE TIEMPOS
# ============================================================================

def medir_tiempos(tamanios, repeticiones=5):
    """Mide tiempos de ejecución"""
    resultados = {}

    print("="*70)
    print("⏱️  MIDIENDO TIEMPOS DE EJECUCIÓN")
    print("="*70)

    for n in tamanios:
        print(f"\n📊 n={n} (Permutaciones: {math.factorial(n):,})")
        tiempos = []

        for rep in range(repeticiones):
            finca = generar_finca_aleatoria(n, seed=rep)

            inicio = time.time()
            roFB_simple(finca)
            fin = time.time()

            tiempo = fin - inicio
            tiempos.append(tiempo)
            print(f"   Rep {rep+1}/{repeticiones}: {tiempo:.4f} seg")

        promedio = np.mean(tiempos)
        std = np.std(tiempos)

        resultados[n] = {
            'tiempos': tiempos,
            'promedio': promedio,
            'std': std
        }

        print(f"   ✅ Promedio: {promedio:.4f} ± {std:.4f} seg")

    return resultados


# ============================================================================
# GENERACIÓN DE GRÁFICOS
# ============================================================================

def crear_grafico_1_tiempo_lineal(resultados, carpeta_salida):
    """Gráfico 1: Tiempo vs n (escala lineal)"""
    plt.figure(figsize=(10, 6))

    ns = sorted(resultados.keys())
    promedios = [resultados[n]['promedio'] for n in ns]
    stds = [resultados[n]['std'] for n in ns]

    plt.errorbar(ns, promedios, yerr=stds,
                 marker='o', capsize=5, capthick=2,
                 linewidth=2.5, markersize=9,
                 color='#2E86AB', ecolor='#A23B72',
                 label='Tiempo promedio')

    plt.xlabel('Tamaño de entrada (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Tiempo de ejecución (segundos)', fontsize=12, fontweight='bold')
    plt.title('Fuerza Bruta: Tiempo de Ejecución vs. Tamaño',
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(fontsize=10)
    plt.tight_layout()

    ruta = os.path.join(carpeta_salida, 'grafico_tiempo_lineal_fb.png')
    plt.savefig(ruta, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Gráfico 1 guardado: {ruta}")


def crear_grafico_2_tiempo_log(resultados, carpeta_salida):
    """Gráfico 2: Tiempo vs n (escala logarítmica)"""
    plt.figure(figsize=(10, 6))

    ns = sorted(resultados.keys())
    promedios = [resultados[n]['promedio'] for n in ns]

    plt.plot(ns, promedios, marker='s', linewidth=2.5,
             markersize=10, color='#E63946',
             label='Tiempo experimental')

    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Tiempo (segundos, escala log)', fontsize=12, fontweight='bold')
    plt.title('Crecimiento Factorial del Tiempo',
              fontsize=14, fontweight='bold')
    plt.grid(True, which="both", alpha=0.3, linestyle='--')
    plt.legend(fontsize=10)
    plt.tight_layout()

    ruta = os.path.join(carpeta_salida, 'grafico_tiempo_log_fb.png')
    plt.savefig(ruta, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Gráfico 2 guardado: {ruta}")


def crear_grafico_3_teorico_vs_experimental(resultados, carpeta_salida):
    """Gráfico 3: Comparación teórica vs experimental"""
    plt.figure(figsize=(12, 7))

    ns = sorted(resultados.keys())
    promedios = [resultados[n]['promedio'] for n in ns]

    # Calcular curva teórica normalizada
    if promedios[0] > 0:
        k = promedios[0] / (math.factorial(ns[0]) * ns[0])
    else:
        k = 1e-9

    teoricos = [k * math.factorial(n) * n for n in ns]

    plt.plot(ns, promedios, marker='o', linewidth=2.5,
             markersize=10, color='#06AED5',
             label='Experimental (promedio)', zorder=3)

    plt.plot(ns, teoricos, linestyle='--', linewidth=2,
             color='#DD1C1A', alpha=0.8,
             label=r'Teórico: $O(n! \cdot n)$', zorder=2)

    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Tiempo (segundos, escala log)', fontsize=12, fontweight='bold')
    plt.title('Validación: Complejidad Teórica vs. Experimental',
              fontsize=14, fontweight='bold')
    plt.grid(True, which="both", alpha=0.3, linestyle='--')
    plt.legend(fontsize=11, loc='upper left')
    plt.tight_layout()

    ruta = os.path.join(carpeta_salida, 'grafico_teorico_vs_experimental_fb.png')
    plt.savefig(ruta, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Gráfico 3 guardado: {ruta}")


def crear_grafico_4_tabla_resultados(resultados, carpeta_salida):
    """Gráfico 4: Tabla visual con resultados"""
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.axis('tight')
    ax.axis('off')

    ns = sorted(resultados.keys())
    datos = []

    for n in ns:
        prom = resultados[n]['promedio']
        std = resultados[n]['std']
        factorial = math.factorial(n)
        ops = factorial * n

        datos.append([
            f"{n}",
            f"{factorial:,}",
            f"{ops:,}",
            f"{prom:.4f}",
            f"{std:.4f}"
        ])

    headers = ['n', 'n!', 'n! × n', 'Tiempo Prom. (s)', 'Desv. Est.']

    tabla = ax.table(cellText=datos, colLabels=headers,
                     cellLoc='center', loc='center',
                     colWidths=[0.08, 0.2, 0.25, 0.22, 0.18])

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1, 2.2)

    # Estilo encabezados
    for i in range(len(headers)):
        tabla[(0, i)].set_facecolor('#2E86AB')
        tabla[(0, i)].set_text_props(weight='bold', color='white')

    # Filas alternadas
    for i in range(1, len(datos) + 1):
        for j in range(len(headers)):
            color = '#E8F4F8' if i % 2 == 0 else '#FFFFFF'
            tabla[(i, j)].set_facecolor(color)

    plt.title('Resultados Experimentales - Fuerza Bruta',
              fontsize=14, fontweight='bold', pad=20)

    ruta = os.path.join(carpeta_salida, 'tabla_resultados_fb.png')
    plt.savefig(ruta, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Gráfico 4 guardado: {ruta}")


def crear_grafico_5_viabilidad(carpeta_salida):
    """Gráfico 5: Proyección de viabilidad práctica"""
    plt.figure(figsize=(12, 7))

    ns = range(1, 21)
    ops_por_minuto = 3e8

    tiempos_minutos = []
    for n in ns:
        ops = math.factorial(n) * n
        mins = ops / ops_por_minuto
        tiempos_minutos.append(mins)

    # Colores según viabilidad
    colores = []
    for t in tiempos_minutos:
        if t < 60:           # Menos de 1 hora
            colores.append('#06D6A0')
        elif t < 1440:       # Menos de 1 día
            colores.append('#FFD166')
        else:                # Más de 1 día
            colores.append('#EF476F')

    plt.bar(ns, tiempos_minutos, color=colores,
            edgecolor='black', linewidth=0.5)

    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Tiempo estimado (minutos, escala log)', fontsize=12, fontweight='bold')
    plt.title('Viabilidad Práctica del Algoritmo\n(Procesador: 3×10⁸ ops/min)',
              fontsize=14, fontweight='bold')
    plt.xticks(ns)
    plt.grid(True, axis='y', alpha=0.3, linestyle='--')

    # Leyenda
    from matplotlib.patches import Patch
    leyenda = [
        Patch(facecolor='#06D6A0', label='✅ Viable (< 1 hora)'),
        Patch(facecolor='#FFD166', label='⚠️ Límite (1h - 1 día)'),
        Patch(facecolor='#EF476F', label='❌ Inviable (> 1 día)')
    ]
    plt.legend(handles=leyenda, fontsize=10, loc='upper left')

    plt.tight_layout()

    ruta = os.path.join(carpeta_salida, 'grafico_viabilidad_fb.png')
    plt.savefig(ruta, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Gráfico 5 guardado: {ruta}")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Ejecuta todo el proceso de medición y generación de gráficos"""

    print("="*70)
    print("🎨 GENERADOR DE GRÁFICOS - FUERZA BRUTA")
    print("="*70)
    print()

    # Configurar carpeta de salida
    carpeta_imagenes = os.path.join(PROJECT_ROOT, 'docs', 'imagenes')
    os.makedirs(carpeta_imagenes, exist_ok=True)
    print(f"📁 Carpeta de salida: {carpeta_imagenes}\n")

    # Configuración
    print("⚙️  CONFIGURACIÓN DE PRUEBAS")
    print("-" * 70)
    tamanios = [5, 6, 7, 8, 9, 10]
    repeticiones = 5

    print(f"Tamaños a probar: {tamanios}")
    print(f"Repeticiones: {repeticiones}")
    print(f"Total ejecuciones: {len(tamanios) * repeticiones}")
    print(f"\n⏱️  Tiempo estimado: 3-5 minutos")
    print(f"⚠️  n=10 tarda ~30 seg por repetición\n")

    input("Presiona ENTER para iniciar...")
    print()

    # Medir tiempos
    resultados = medir_tiempos(tamanios, repeticiones)

    # Generar gráficos
    print("\n" + "="*70)
    print("📊 GENERANDO GRÁFICOS")
    print("="*70)
    print()

    crear_grafico_1_tiempo_lineal(resultados, carpeta_imagenes)
    crear_grafico_2_tiempo_log(resultados, carpeta_imagenes)
    crear_grafico_3_teorico_vs_experimental(resultados, carpeta_imagenes)
    crear_grafico_4_tabla_resultados(resultados, carpeta_imagenes)
    crear_grafico_5_viabilidad(carpeta_imagenes)

    # Resumen final
    print("\n" + "="*70)
    print("🎉 ¡PROCESO COMPLETADO!")
    print("="*70)
    print(f"\n📂 Archivos generados en: docs/imagenes/")
    print("\nGráficos creados:")
    print("  1️⃣  grafico_tiempo_lineal_fb.png")
    print("  2️⃣  grafico_tiempo_log_fb.png")
    print("  3️⃣  grafico_teorico_vs_experimental_fb.png")
    print("  4️⃣  tabla_resultados_fb.png")
    print("  5️⃣  grafico_viabilidad_fb.png")
    print("\n💡 Usa en tu Markdown:")
    print("   ![Descripción](imagenes/nombre_archivo.png)")
    print()


if __name__ == "__main__":
    main()