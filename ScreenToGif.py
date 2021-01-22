"""
Opencv python 003 screen recording and save as Gif picture
By Linyoubiao
2020-03-19
"""
from PIL import ImageGrab
import numpy as np
import cv2 as cv
import imageio
import time, pyautogui,keyboard
 
if keyboard.is_pressed('s'):
    buff = []
    i=0
    while i<10:
        im = pyautogui.screenshot()
        img = cv.cvtColor(np.array(im), cv.COLOR_RGB2BGR)
        buff.append(img)
        time.sleep(0.1)
        #if keyboard.is_pressed('x'):
        #    break
        i+=1
        
    gif = imageio.mimsave('screen.gif', buff, 'GIF', duration=0.1)

