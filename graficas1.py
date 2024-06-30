import matplotlib.pyplot as plt
import numpy as np


rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Punto 1: Gráfico de dispersión
plt.scatter(matematicas, ciencias, color='blue')
plt.title('Relación entre las calificaciones de Matemáticas y Ciencias')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Calificacicaciones de Ciencias')

plt.show()

# se guarda la grafica como archivo png
plt.savefig('punto1_grafica_dispersion.png', dpi=300)


# Punto 2: Gráfico barras de error
prom_matematicas = np.mean(matematicas)
prom_ciencias = np.mean(ciencias)
prom_literatura = np.mean(literatura)

x = ['Matemáticas', 'Ciencias', 'Literatura']
y = [prom_matematicas, prom_ciencias, prom_literatura]
y_err = [np.mean(errores_matematicas), np.mean(
    errores_ciencias), np.mean(errores_literatura)]

plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=5, color='blue')
a = plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=5, color='blue')
plt.title('Calificaciones promedio con barras de errror')
plt.xlabel('Materias')
plt.ylabel('Calificaciones promedio')
plt.legend(handles=[a], labels=['Promedio'], loc='upper left')

plt.show()

# Guardar la gráfica como imagen PNG con el nombre específico
plt.savefig('punto2_grafico_barras_error.png', dpi=300)


# Punto 3: Histograma
plt.hist(matematicas, bins=10)
plt.title('Distribución de las calificaciones de Matemáticas')
plt.xlabel('Calificaciones de Matematicas')
plt.ylabel('Frecuencia')

plt.show()

# Guardar la gráfica como imagen PNG con el nombre específico
plt.savefig('punto3_histograma.png', dpi=300)
