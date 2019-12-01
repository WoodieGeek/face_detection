from mtcnn import MTCNN
import cv2
import sys


image_name = sys.argv[1]
print(image_name)
# image_name = "bad_faces.jpg"

img = cv2.cvtColor(cv2.imread(image_name), cv2.COLOR_BGR2RGB)
detector = MTCNN()
detected = detector.detect_faces(img)
# detected = {}
print (detected)
print ("----------")
detected_faces = len(detected) 
print (detected_faces)

image = cv2.imread(image_name)
for face in detected:
    box = face['box']
    x, y, w, h = box
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv2.imshow("Face", image)
cv2.putText(image, str(detected_faces), (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 11, (255, 0, 0), 2)
cv2.imwrite("out.jpg", image)
# cv2.waitKey(0)

