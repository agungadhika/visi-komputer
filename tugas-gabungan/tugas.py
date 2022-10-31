import cv2
from PIL import Image
from math import sin, cos

def tugas1():
    img = cv2.imread('/home/ikantongkol/Documents/Kuliah/visi-komputer/tugas-gabungan/kucing.jpeg')

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


def tugas2():
    CITRA = Image.open('/home/ikantongkol/Documents/Kuliah/visi-komputer/tugas-gabungan/index.jpeg')

    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]

    px = CITRA.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            R = 255 - px[x, y][0]
            G = 255 - px[x, y][1]
            B = 255 - px[x, y][2]
            px[x, y] = (R, G, B)

    CITRA.save('gambar_convert.jpg')

#masih belom bisa disini
def tugas3(derajat):
    CITRA = Image.open("/home/ikantongkol/Documents/Kuliah/visi-komputer/tugas-gabungan/index.jpeg")
    PIXEL = CITRA.load()

    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]
    citraBaru = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    pxBaru = citraBaru.load()

    x_tengah = ukuran_horizontal // 2
    y_tengah = ukuran_vertikal // 2

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            theta = derajat * 22/7 / 180

            x_baru = (cos(theta) * (x - x_tengah) - sin(theta)
                      * (y - y_tengah) + x_tengah)
            y_baru = (sin(theta) * (x - x_tengah) + cos(theta)
                      * (y - y_tengah) + y_tengah)

#tampilkan hasil perhitungan
#tampilkan x0y0 kemudian hasil perubahan
    
            if (x_baru >= ukuran_horizontal or y_baru >= ukuran_vertikal
                    or x_baru < 0 or y_baru < 0):
                pxBaru[x, y] = (0, 0, 0)
            else:
                pxBaru[x, y] = PIXEL[x_baru, y_baru]
    
        nama_setelah_disave = 'gambar_rotasi_' + str(derajat) + '.jpg'
        citraBaru.save(nama_setelah_disave)
    rotasi(45)
    rotasi(90)
    rotasi(180)

if __name__ == "__main__":
    tugas3()