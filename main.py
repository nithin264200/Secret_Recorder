from PIL import ImageGrab
import datetime
import numpy as np
import cv2
from win32api import GetSystemMetrics

w= GetSystemMetrics(0)
h= GetSystemMetrics(1)
recorded_time= datetime.datetime.now().strftime('%Y-%M-%D %H-%M-%S')
#print(recorded_time)
file = f'{recorded_time}.mp4'
fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
captured_video=cv2.VideoWriter('output.mp4',fourcc,20.0,(w,h))
webcam= cv2.VideoCapture(0)
while True:
    img=ImageGrab.grab(bbox=(0,0,w,h))
    img_np=np.array(img)
    img_final=cv2.cvtColor(img_np,cv2.COLOR_BGRA2RGB)

    _, frame= webcam.read()
    fr_height, fr_width,_  =frame.shape
    img_final[0:fr_height,0:fr_width,:]=frame[0:fr_height,0:fr_width,:]

    #cv2.imshow('webcam',frame)
    #cv2.displayOverlay(captured_video)

    cv2.imshow('Secret recorder', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10)==ord('q'):
        break

