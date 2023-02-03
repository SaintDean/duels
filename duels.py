import numpy as np
import pyautogui
import time

time.sleep(np.random.uniform(1.5,1.8))

while 1:
    pyautogui.moveTo(754,790, duration=0.9)
    pyautogui.leftClick() #Click Duels
    time.sleep(np.random.uniform(1,1.5))
    pyautogui.moveTo(1086,550, duration=0.8)
    pyautogui.leftClick() #Pick Enemy
    time.sleep(np.random.uniform(1.2,1.6))
    pyautogui.moveTo(897,709, duration=0.7)
    pyautogui.leftClick() #Click Attack
    time.sleep(np.random.uniform(1.8,2.5))
    pyautogui.press('Enter')
    time.sleep(np.random.uniform(1.5,2.3))
    pyautogui.moveTo(951,675, duration=1)
    pyautogui.leftClick()
    time.sleep(np.random.uniform(602,605))

