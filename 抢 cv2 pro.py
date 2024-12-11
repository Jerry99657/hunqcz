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
btm0=btm('00.png',(300,1266,1400,180))#,(400,1266,1200,180)
print(0,btm0)
while not btm0:
    print(0,btm0)
    pya.click(802,813)
    btm1=btm('01.png',(380,1000,320,140))
    while not btm1:
        print(1,btm1)
        time.sleep(0.1)
        btm1=btm('01.png',(380,1000,320,140))
    print(1,btm1)
    pya.click(1170,809)
    btm0=btm('00.png',(300,1266,1400,180))#(400,1276,1200,160)
    btm2=btm('02.png',(332,1095,1360,235))
    btm3=btm('03.png',(548,1058,200,500)) #
    #btm3=btm('02.png',(374,1241,1300,220))
    while not btm0 and not btm2 or btm3: #0和1识别不成功，等待1s
        print(0, btm0)
        print(2, btm2)
        print(3, btm3)
        if btm3:
            pya.click(802, 813)
            btm1=btm('01.png',(380,1000,320,140))
            while not btm1:
                print(1, btm1)
                time.sleep(0.1)
                btm1=btm('01.png',(380,1000,320,140))
            pya.click(1170, 809)
            btm0=btm('00.png',(300,1266,1400,180))#400,1276,1200,160
            while not btm0:
                time.sleep(0.1)
                btm0=btm('00.png',(300,1266,1400,180))#400,1276,1200,160
            for l in list:
                print(l[0])
                btm4 = btm('000.png', l[0])
                if btm4:
                    pya.click(l[1][0], l[1][1])
                    time.sleep(0.1)
                    pya.click(l[2][0], l[2][1])
                    pya.click(2127, 1065)
                    time.sleep(0.1)
                    pya.click(2127, 1065)
                    time.sleep(0.1)
                    pya.click(2127, 1065)
                    btm5 = btm('10.png', (885, 204, 70, 60))
                    while not btm5:
                        time.sleep(0.1)
                        btm5 = btm('10.png', (885, 204, 70, 60))
                    pya.click(l[1][0], l[1][1])
                    time.sleep(0.1)
                    pya.click(l[2][0], l[2][1])
            # pya.click(810, 1315)
            # time.sleep(0.1)
            # pya.click(810, 1385)
            # pya.click(2131, 984)
            # os.kill(pid, signal.SIGTERM)
        else:
            time.sleep(0.1)
            print(0,btm0)
            print(2,btm2)
            print(3, btm3)
            btm0 = btm('00.png', (300,1266,1400,180))
            btm2 = btm('02.png', (332, 1095, 1360, 235))
            btm3=btm('03.png', (548,1058,200,500))
    x,y=pya.position()
    if 1780<x<2450 and 310<y<550:
        os.kill(pid,signal.SIGTERM)  #鼠标移动到这里停止程序
print(0,btm0)
for l in list:
    print(l[0])
    btm4=btm('000.png',l[0])
    if  btm4:
        pya.click(l[1][0],l[1][1])
        time.sleep(0.1)
        pya.click(l[2][0],l[2][1])
        pya.click(2127, 1065)
        time.sleep(0.1)
        pya.click(2127, 1065)
        time.sleep(0.1)
        pya.click(2127, 1065)
        btm5=btm('10.png',(885,204,70,60))
        while not btm5:
            time.sleep(0.1)
            btm5 = btm('10.png', (885, 204, 70, 60))
        pya.click(l[1][0], l[1][1])
        time.sleep(0.1)
        pya.click(l[2][0], l[2][1])
# pya.click(810,1315)
# time.sleep(0.1)
# pya.click(810,1385)
# pya.click(2127,1065)
# time.sleep(0.3)
# pya.click(2127,1065)


