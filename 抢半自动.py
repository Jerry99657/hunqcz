import pyautogui as pya
import time
pya.PAUSE = 0.01
btm=pya.locateOnScreen('00.png', confidence=0.9)
while not btm:
    time.sleep(0.1)
    btm = pya.locateOnScreen('00.png', confidence=0.9)
pya.click(810,1315)
time.sleep(0.1)
pya.click(810,1385)
pya.click(2127,1065)
time.sleep(0.1)
pya.click(2127,1065)
time.sleep(0.1)
pya.click(2127,1065)