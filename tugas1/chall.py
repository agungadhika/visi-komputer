#/usr/bin/python2
import cv2

img = cv2.imread('/media/ikantongkol/575E5BC04E0C3C04/Kuliah/Tugas/Tugas/SEMESTER 7/Visi Komputer/visi-komputer/tugas1/kucing.jpeg')

dimension = img.shape
height = img.shape[0] 
width = img.shape[1]
pixel = img.shape[2]
color_depth = 2 ** pixel

print("Tinggi: {}".format(height))
print("Lebar: {}".format(width))
print("Pixel: {}".format(pixel))
print('Ukuran gambar: {}'.format(dimension))
print('Ukuran : {} x {}'.format(height,width))
print('Kedalaman Warna: {}'.format(color_depth)) 

# cv2.imshow("Image",img)
# cv2.waitKey(0)