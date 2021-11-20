from PIL import Image, ImageDraw
import  qrcode

img = qrcode.make("https://youtu.be/ly5nJgRutYY")
img.save("QrImg.jpg")

img2 = qrcode.make("Paras is a good boy")
img2.save("QrImg2.jpg")

img3 = qrcode.make("Opencvvv/lena.jpg")
img3.save("QrImg3.jpg")


import cv2

d = cv2.QRCodeDetector()
d2 = cv2.QRCodeDetector()
d3 = cv2.QRCodeDetector()

print(d.detectAndDecode(cv2.imread("QrImg.jpg")))
print(d.detectAndDecode(cv2.imread("QrImg2.jpg")))
print(d.detectAndDecode(cv2.imread("QrImg3.jpg")))

