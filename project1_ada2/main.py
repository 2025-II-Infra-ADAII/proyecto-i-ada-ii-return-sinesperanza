"""
Programa principal para el problema de riego óptimo.
Permite seleccionar archivos de entrada/salida y elegir el algoritmo a usar.
"""

import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import sys

# Importar módulos propios
from project1_ada2.io_utils import leer_finca, escribir_salida
from project1_ada2.irrigation_planks_fb import roFB
from project1_ada2.irrigation_planks_rov import roPV 

# TODO: Descomentar cuando estén implementados
# from project1_ada2.irrigation_planks_pd import roPD


def seleccionar_archivo_entrada():
    """
    Abre un file chooser para seleccionar el archivo de entrada.

    Returns:
        Path o None: Ruta del archivo seleccionado o None si se cancela
    """
    root = tk.Tk()
    root.withdraw()  # Ocultar ventana principal
    root.attributes('-topmost', True)  # Traer al frente

    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo de entrada",
        filetypes=[
            ("Archivos de texto", "*.txt"),
            ("Todos los archivos", "*.*")
        ],
        initialdir=Path.cwd() / "data"
    )

    root.destroy()

    return Path(archivo) if archivo else None


def seleccionar_archivo_salida():
    """
    Abre un file chooser para seleccionar dónde guardar el archivo de salida.

    Returns:
        Path o None: Ruta del archivo de salida o None si se cancela
    """
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    archivo = filedialog.asksaveasfilename(
        title="Guardar resultado como",
        defaultextension=".txt",
        filetypes=[
            ("Archivos de texto", "*.txt"),
            ("Todos los archivos", "*.*")
        ],
        initialdir=Path.cwd() / "data",
        initialfile="salida.txt"
    )

    root.destroy()

    return Path(archivo) if archivo else None


def mostrar_menu():
    """
    Muestra el menú de selección de algoritmo.

    Returns:
        int: Opción seleccionada (1, 2, 3) o 0 para salir
    """
    print("\n" + "=" * 60)
    print("  PROBLEMA DE RIEGO ÓPTIMO - Selección de Algoritmo")
    print("=" * 60)
    print("\nAlgoritmos disponibles:")
    print("  [1] Fuerza Bruta (FB)")
    print("  [2] Algoritmo Voraz (V)")
    print("  [3] Programación Dinámica (PD) - ⚠️ Próximamente")
    print("  [0] Salir")
    print("-" * 60)

    while True:
        try:
            opcion = int(input("\nSeleccione una opción (0-3): "))
            if 0 <= opcion <= 3:
                return opcion
            else:
                print("❌ Opción inválida. Por favor ingrese un número entre 0 y 3.")
        except ValueError:
            print("❌ Entrada inválida. Por favor ingrese un número.")


def ejecutar_algoritmo(opcion, finca):
    """
    Ejecuta el algoritmo seleccionado.

    Args:
        opcion (int): Número de algoritmo (1=FB, 2=V, 3=PD)
        finca (list): Lista de tablones

    Returns:
        tuple: (permutacion, costo) o None si hay error
    """
    print("\n⏳ Ejecutando algoritmo...")

    try:
        if opcion == 1:
            print("📊 Algoritmo: Fuerza Bruta")
            perm, costo = roFB(finca)
            return perm, costo

        elif opcion == 2:
            print("📊 Algoritmo: Voraz")
            print("❌ Este algoritmo aún no está implementado")
            perm, costo = roPV(finca)
            return perm, costo

        elif opcion == 3:
            print("📊 Algoritmo: Programación Dinámica")
            print("❌ Este algoritmo aún no está implementado")
            return None
            # TODO: Descomentar cuando esté listo
            # perm, costo = roPD(finca)
            # return perm, costo

    except Exception as e:
        print(f"❌ Error al ejecutar el algoritmo: {str(e)}")
        return None


def mostrar_resultado(perm, costo, finca):
    """
    Muestra el resultado de forma legible.

    Args:
        perm (list): Permutación (orden de riego)
        costo (int): Costo total
        finca (list): Datos de la finca
    """
    print("\n" + "=" * 60)
    print("  RESULTADO")
    print("=" * 60)
    print(f"✅ Costo total mínimo: {costo}")
    print(f"\n📋 Orden de riego de tablones:")
    print(f"   {' → '.join(map(str, perm))}")

    print(f"\n📊 Detalle de tablones:")
    print(f"{'Pos':<5} {'Tablón':<8} {'ts':<6} {'tr':<6} {'p':<6}")
    print("-" * 40)
    for i, idx in enumerate(perm):
        ts, tr, p = finca[idx]
        print(f"{i:<5} {idx:<8} {ts:<6} {tr:<6} {p:<6}")
    print("=" * 60)


def main():
    """
    Función principal del programa.
    """
    print("\n🌾 BIENVENIDO AL SISTEMA DE RIEGO ÓPTIMO 🌾")

    # 1️⃣ Seleccionar archivo de entrada
    print("\n📂 Paso 1: Seleccionar archivo de entrada")
    archivo_entrada = seleccionar_archivo_entrada()

    if not archivo_entrada:
        print("❌ No se seleccionó archivo de entrada. Programa cancelado.")
        sys.exit(0)

    print(f"✅ Archivo seleccionado: {archivo_entrada}")

    # 2️⃣ Leer finca
    try:
        print("\n📖 Leyendo archivo...")
        finca = leer_finca(archivo_entrada)
        print(f"✅ Finca cargada correctamente: {len(finca)} tablones")

        # Mostrar resumen de la finca
        print(f"\n📊 Resumen de la finca:")
        print(f"{'Tablón':<8} {'ts':<6} {'tr':<6} {'p':<6}")
        print("-" * 30)
        for i, (ts, tr, p) in enumerate(finca):
            print(f"{i:<8} {ts:<6} {tr:<6} {p:<6}")

    except Exception as e:
        print(f"❌ Error al leer el archivo: {str(e)}")
        sys.exit(1)

    # 3️⃣ Seleccionar algoritmo
    opcion = mostrar_menu()

    if opcion == 0:
        print("\n👋 Programa finalizado. ¡Hasta pronto!")
        sys.exit(0)

    if opcion in [3]:
        print("\n⚠️  Este algoritmo aún no está implementado.")
        print("Por favor, seleccione Fuerza Bruta o voraz (opción 1 o 2) por ahora.")
        sys.exit(0)

    # 4️⃣ Ejecutar algoritmo
    resultado = ejecutar_algoritmo(opcion, finca)

    if resultado is None:
        print("\n❌ No se pudo ejecutar el algoritmo.")
        sys.exit(1)

    perm, costo = resultado

    # 5️⃣ Mostrar resultado
    mostrar_resultado(perm, costo, finca)

    # 6️⃣ Guardar resultado
    print("\n💾 Paso 2: Guardar resultado")
    guardar = input("¿Desea guardar el resultado en un archivo? (s/n): ").lower()

    if guardar == 's':
        archivo_salida = seleccionar_archivo_salida()

        if archivo_salida:
            try:
                escribir_salida(archivo_salida, perm, costo)
                print(f"✅ Resultado guardado en: {archivo_salida}")
            except Exception as e:
                print(f"❌ Error al guardar: {str(e)}")
        else:
            print("❌ No se seleccionó archivo de salida.")

    print("\n✨ Proceso completado exitosamente.")
    print("👋 ¡Hasta pronto!\n")


if __name__ == "__main__":
    main()