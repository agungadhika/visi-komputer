from PIL import Image
import cv2
import matplotlib.pyplot as plt

CITRA = Image.open('/home/ikantongkol/Documents/Kuliah/visi-komputer/tugas2/cat.jpeg')

ukuran_horizontal = CITRA.size[0]
ukuran_vertikal = CITRA.size[1]

PIXEL = CITRA.load()

for x in range(ukuran_horizontal):
    for y in range(ukuran_vertikal):
        R = 255 - PIXEL[x, y][0]
        G = 255 - PIXEL[x, y][1]
        B = 255 - PIXEL[x, y][2]
        PIXEL[x, y] = (R, G, B)
histogram = cv2.calcHist(PIXEL[x, y])
plt.plot(histogram, color='k')
plt.show()


CITRA.save('gambar_negatif.jpg')