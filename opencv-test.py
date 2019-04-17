import sys
import cv2
import importlib

importlib.reload(sys)

#@author__ = 'ricardo'
#date__ = '2019/4/17'
#人脸检测小实验

# 待检测的图片路径
imagepath = r'./spurs.jpg'

pathf = 'D:/Softs/opencv-github/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml'


# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
face_cascade = cv2.CascadeClassifier(pathf)

# 读取图片
image = cv2.imread(imagepath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 探测图片中的人脸
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("发现{0}个人脸!".format(len(faces)))

for (x, y, w, h) in faces:
    # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)

    cv2.circle(image, ((x + x + w) // 2, (y + y + h) // 2), w // 2, (0, 255, 0), 2)

cv2.imshow("Find Faces!", image)
cv2.waitKey(0)
