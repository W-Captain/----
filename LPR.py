# 导入包
from hyperlpr import *
# 导入OpenCV库
import cv2
import time
import threading

t = 0


def cont():
    global t
    t = 1


"""cap = cv2.VideoCapture(0)  # 默认的摄像头
# 指定视频代码
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter('temp.avi', fourcc, 20.0, (640, 480))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        threading.Timer(5, cont).start()
        out.write(frame)
        cv2.imshow('frame', frame)
        # 等待按键q操作关闭摄像头
        if t == 1:
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()"""
cap = cv2.VideoCapture(0)
while(1):
 # get a frame
 ret, frame = cap.read()
 # show a frame
 #cv2.imshow("capture", frame)
 threading.Timer(2, cont).start()
 if t==1:
  cv2.imwrite("demo1.png", frame)
  break
cap.release()
cv2.destroyAllWindows()
# 读入图片
image = cv2.imread("demo1.png")
# 识别结果
print(HyperLPR_PlateRecogntion(image))
