import pyautogui as pya
import time
import os
import signal
import cv2
import numpy as np
pid = os.getpid()
pya.PAUSE = 0.01
def btm(x,y):
    src=pya.screenshot(region=y)
    src_gray=cv2.cvtColor(np.array(src),cv2.COLOR_RGB2GRAY)
    tem=cv2.imread(x,0)
    res=cv2.matchTemplate(src_gray,tem,cv2.TM_CCOEFF_NORMED)
    loc=np.where(res>=0.9)
    if loc[0].size==0:
        return False
    else:
        return True
list=[[(540,1280,180,140),[625,1315],[625,1387]],[(720,1280,180,140),[807,1315],[807,1387]],
      [(900,1280,180,140),[988,1315],[988,1387]],[(1080,1280,180,140),[1171,1315],[1171,1387]],
      [(1260,1280,180,140),[1352,1315],[1352,1387]],[(1440,1280,180,140),[1535,1315],[1535,1387]]]
btm00=btm('000.png',(379,985,1200,550))
while not btm00:
    print(1,btm00)
    time.sleep(0.1)
    btm00 = btm('000.png', (379,985,1200,550))
for l in list:
    btm0=btm('000.png',l[0])
    if btm0:
        print(0,btm0)
        pya.click(l[1][0],l[1][1])
        time.sleep(0.1)
        pya.click(l[2][0],l[2][1])
        pya.click(2127, 1065)
        time.sleep(0.1)
        pya.click(2127, 1065)
        time.sleep(0.1)
        pya.click(2127, 1065)
        btm1=btm('10.png',(885,204,70,60))
        while not btm1:
            print(11,btm1)
            time.sleep(0.01)
            btm1 = btm('10.png', (885, 204, 70, 60))
        pya.click(l[1][0], l[1][1])
        time.sleep(0.1)
        pya.click(l[2][0], l[2][1])





















