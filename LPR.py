# 导入包
from hyperlpr import *
# 导入OpenCV库
import cv2
import time
import threading
import serial

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
while (1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    # cv2.imshow("capture", frame)
    threading.Timer(2, cont).start()
    if t == 1:
        cv2.imwrite("demo1.png", frame)
        break
cap.release()
cv2.destroyAllWindows()
# 读入图片
image = cv2.imread("demo1.png")
# 识别结果
qqq = HyperLPR_PlateRecogntion(image)
if qqq:
    strt = qqq[0][0][1:7]
    print(strt)
##arduino
ser = serial.Serial('com3', 9600)
print(ser)
# ser.open()  # 打开串口
print(ser.is_open)  # 检验串口是否打开
result = ser.write("kuan".encode("utf-8"))
print("写总字节数:", result)
str = ser.readline()
print(str)
demo1 = b"kuan"
ser.write(demo1)
if strt == "D0B250":
    time.sleep(1)
    tem = b'5'
    ser.write(tem)
    print("ok")
