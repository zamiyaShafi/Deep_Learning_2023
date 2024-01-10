import tensorflow as tf

from mtcnn import MTCNN
import cv2



detector=MTCNN()

img=cv2.imread('images/yumna.jpg')

output=detector.detect_faces(img)
print(output)