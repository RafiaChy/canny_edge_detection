import cv2
img = cv2.imread('lena.jpg', 1)
canny = cv2.Canny(img, 50, 100)
cv2.imshow('Image', img)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()