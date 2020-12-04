import cv2
import math
import glob
import numpy as np

'''
Code for analising Hu Moments
'''

# paths a las imagenes de yoda
yoda_path = glob.glob('./star-wars/0001/*.jpg')

huMoments = np.zeros((len(yoda_path), 7))  # array para almacenar momentos

x = 0

for f in yoda_path:
    image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)  # leer imagen en escala de grises
    _, im = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)  # binarizar la imagen
    moments = cv2.moments(im)  # momentos
    huMoments1 = cv2.HuMoments(moments)  # momentos de Hu

    # como son valores muy pequeños, se hace una transformación logarítmica
    for i in range(0, 7):
        huMoments1[i] = -1 * math.copysign(1.0, huMoments1[i]) * math.log10(abs(huMoments1[i]))
    huMoments1 = np.array(huMoments1).reshape(1, 7)
    huMoments[x, :] = huMoments1
    x += 1

print(huMoments)
# np.savetxt('yodaHu.csv', huMoments, delimiter=',', fmt='%.3f')


# Ahora se calculan para la misma imagen con transformaciones
imyoda = cv2.imread(yoda_path[0])

# percent by which the image is resized
scale_percent = 50

# 50% de las dimensiones de la imagen
width = int(imyoda.shape[1] * scale_percent / 100)
height = int(imyoda.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
resized = cv2.resize(imyoda, dsize)
# imagen rotada y reflejada
rotate = cv2.rotate(imyoda, cv2.ROTATE_90_CLOCKWISE)
flipHorizontal = cv2.flip(imyoda, 1)

yodaims = [imyoda, rotate, flipHorizontal, resized]

huMoments = np.zeros((len(yodaims), 7))
x = 0
for image in yodaims:

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, im = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    moments = cv2.moments(im)
    huMoments1 = cv2.HuMoments(moments)
    for i in range(0, 7):
        huMoments1[i] = -1 * math.copysign(1.0, huMoments1[i]) * math.log10(abs(huMoments1[i]))
    huMoments1 = np.array(huMoments1).reshape(1, 7)
    huMoments[x, :] = huMoments1
    x += 1

# print(huMoments)
# np.savetxt('yoda3R.csv', huMoments, delimiter=',', fmt='%.3f')
