[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/GxFB-nwe)

# Asignación: [Primer Proyecto ADA II]

**Fecha:** [23/10/2025]
**Curso:** [ADA II]

---

## 👥 Integrantes del Grupo

| Nombre Completo                 | Código   |Rol             |Correo Electrónico                         |
|---------------------------------|----------|----------      |-------------------------------------------|
| Juan José Valencia Jimenez      | 2359567  | [Líder]        | [juan.j.valencia@correounivalle.edu.co]   |
| Yulieth Tatiana Rengifo Rengifo | 2359748  | [Colaborador]  | [yulieth.rengifo@correounivalle.edu.co]   |
| Pedro José Lopez Quiroz         | 2359423  | [Colaborador]  | [pedro.lopez@correounivalle.edu.co]       |
| Anderson Gómez García         | 2266242  | [Colaborador]  | [gomez.anderson@correounivalle.edu.co]       |

---

## 📌 Descripción del Taller
El proyecto “Calculando el plan de riego óptimo de una finca” tiene como propósito aplicar diferentes estrategias de diseño de algoritmos —fuerza bruta, voraz y programación dinámica— para resolver un problema combinatorio real: determinar el orden óptimo en que deben regarse los tablones de una finca para minimizar el sufrimiento de los cultivos por falta de agua.

Cada tablón de la finca se caracteriza por su tiempo de supervivencia (días que puede estar sin riego), su tiempo de regado (días que tarda en regarse completamente) y su prioridad (de 1 a 4). Se dispone de un único sistema móvil de riego, por lo que el objetivo es encontrar una programación que reduzca al mínimo el costo total, definido como la penalización acumulada por regar los tablones después de su tiempo de supervivencia.

El proyecto consiste en desarrollar tres enfoques distintos:

Fuerza bruta (roFB): genera todas las permutaciones posibles del orden de riego, evalúa el costo total de cada una y selecciona la mejor. Aunque garantiza la solución óptima, presenta alta complejidad computacional.

Algoritmo voraz (roV): emplea una estrategia heurística que toma decisiones locales basadas en una regla definida por el grupo (por ejemplo, priorizar por razón entre prioridad y tiempo de riego). Su ventaja es la eficiencia, aunque puede no producir siempre la solución óptima.

Programación dinámica (roPD): formula el problema en términos de subproblemas y relaciones de recurrencia, aprovechando la subestructura óptima para construir una solución más eficiente que la fuerza bruta y más precisa que la heurística voraz.

El código debe implementarse en un lenguaje de programación que permita realizar pruebas unitarias, mediciones de tiempo y el uso de pipelines CI/CD con GitHub Actions. Además, se debe incluir un informe en formato Markdown con el análisis de complejidad de cada enfoque, la justificación teórica, los resultados experimentales y una comparación entre los métodos.

Objetivo general:
Desarrollar e implementar algoritmos basados en fuerza bruta, heurísticas voraces y programación dinámica para encontrar el plan de riego óptimo que minimice el costo de sufrimiento de los cultivos.

Objetivos específicos:

Aplicar y comparar distintas estrategias de diseño de algoritmos para un mismo problema combinatorio.

Analizar la complejidad temporal y espacial de cada enfoque.

Implementar pruebas unitarias y pipelines de integración continua.

Documentar y sustentar el proceso de desarrollo y los resultados obtenidos.

Este proyecto integra teoría y práctica en el análisis de algoritmos, promoviendo la comprensión profunda de la optimalidad, la eficiencia y la aplicabilidad de distintas estrategias de resolución de problemas.