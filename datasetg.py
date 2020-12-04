# Librerias utilizadas
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib import cm

# Definicion de variables para extraccion de datos en el dataset
a, b, c, d, f = 0, 1, 0, 1, 0
folder = ['marvel', 'star-wars', 'jurassic-world', 'harry-potter']
nuevo, datoshs, datoshstest, etiquetas = [], [], [], []
numero_etiqueta = 1
i = 0


# Modulo ls3 para extraccion de datos en carpeta que se requiera
def ls3(path):
    return [obj.name for obj in Path(path).iterdir() if obj.is_file()]


w, h = 0, 0

# Generacion caracteristicas mapa y etiquetas

while True:
    # Aumento de documento
    i += 1
    # Path de la imagen
    imagepath = './%s/' % folder[f] + '00' + '%d' % a + '%d' % b
    files = ls3('%s' % imagepath)
    # Recorre cada archivo de la carpeta seleccionada
    for file in files:
        # Guarda imagen
        imagen = cv.imread(imagepath + '/%s' % file)
        # Pasa imagen a escala de grises
        hsv = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)
        # Calculo de histograma de 16 x 4
        hist = cv.calcHist([hsv], [0, 1], None, [16, 4], [0, 180, 0, 256])

        # datos de s,v para histograma

        # Resultado de histograma en numpy array
        result = np.array(hist).flatten()
        # Lista que guarda los histogramas de todas las imagenes
        datoshs = np.append(datoshs, result)

        # Etiqueta imagen marvel como 1
        if (folder[f] == 'marvel'):
            etiquetas.append(1)
        # Etiqueta imagen star-wars como 2
        if (folder[f] == 'star-wars'):
            etiquetas.append(2)
        # Etiqueta imagen jurassic-world como 3
        if (folder[f] == 'jurassic-world'):
            etiquetas.append(3)
        # Etiqueta imagen harry-potter como 4
        if (folder[f] == 'harry-potter'):
            etiquetas.append(4)
    # Valores de cambio de path para extraer todos los datos
    if (i == 1):
        b = 5
    if (i == 2):
        a = 1
        b = 7
    if (i == 3):
        a = 0
        b = 1
        f = 1
    if (i == 4 or i == 7 or i == 9):
        b = 2
    if (i == 5):
        b = 3
    if (i == 6):
        f = 2
        a = 0
        b = 1
    if (i == 8):
        f = 3
        b = 1
    if (i == 10):
        break

# Reorganizacion de resultados en lista de 121 x 64
nuevo = np.reshape(datoshs, (121, 64))

etiquetas = np.array(etiquetas)

# Union caracteristicas con etiquetas en una sola matriz
nuevo = np.column_stack((nuevo, etiquetas))

# .CSV resultante
np.savetxt("lego_data.csv", nuevo, delimiter=",", fmt='%.1f')

'''
fig = plt.figure()

ax = fig.gca(projection='3d')
X = np.arange(0, 4, 1)
Y = np.arange(0, 16, 1)
X, Y = np.meshgrid(X, Y)
Z = hist

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title("Histograma 3D")
plt.xlabel("Saturación (0-3)")
plt.ylabel("Hue (0-15)")
plt.show()
'''
# plt.imshow(hist, interpolation='nearest')
# plt.show()

