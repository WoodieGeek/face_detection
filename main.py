from mtcnn import MTCNN
import cv2
import sys
from PIL import Image, ImageDraw, ImageFont


def GetFaces(image_name):
    img = cv2.cvtColor(cv2.imread(image_name), cv2.COLOR_BGR2RGB)
    detector = MTCNN()
    detected = detector.detect_faces(img)
    return detected

def SetFaceCount(count):
    height, width = image.shape[:2]
    bot = 100;
    img = Image.new('RGB', (width, height + bot))
    img2 = Image.new('RGB', (width, bot), "white")
    img1 = Image.open('out.jpg')

    img.paste(img1, (0, 0))
    img.paste(img2, (0, height))



    font = ImageFont.truetype('arial.ttf', size=100)
    draw = ImageDraw.Draw(img)
    draw.text((width // 2, height), str(count), font=font, fill="black")
     
    img.show()
    # img.save("result_merge.jpg")




image_name = sys.argv[1]

detected = {}
detected = GetFaces(image_name)

print (detected)
print ("----------")
detected_faces = len(detected) 
print (detected_faces)

image = cv2.imread(image_name)

for face in detected:
    box = face['box']
    x, y, w, h = box
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

height, width = image.shape[:2]
image = cv2.resize(image, (1000, 600))
# cv2.putText(image, str(detected_faces), (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 11, (255, 0, 0), 2)
cv2.imwrite("out.jpg", image)
SetFaceCount(detected_faces)

