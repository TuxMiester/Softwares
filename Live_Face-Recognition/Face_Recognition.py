import cv2
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Images/Aish2.jpg')

cv2.imshow('Clever Programmer Face Detector', img)


print("Code Completed")