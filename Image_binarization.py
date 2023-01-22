import cv2
import numpy as np

img = cv2.imread("image1.jpg", 0)
# img cv2.imread('lena_square_half.png", a)
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 10)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 10)

cv2.imshow("Image", img)

cv2.imwrite("Mean.jpg", th1)

cv2.imwrite("Gaussian.jpg", th2)
cv2.imshow("Mean.jpg", th1)

cv2.imshow("Gaussian.jpg", th2)

cv2.waitKey(0)

cv2.destroyAllwindows()
