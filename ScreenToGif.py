from PIL import ImageGrab
import numpy as np
import cv2 as cv
import time, pyautogui,keyboard, imageio
 
if keyboard.is_pressed('s'):
    buff = []
    while True:
        im = pyautogui.screenshot()
        img = cv.cvtColor(np.array(im), cv.COLOR_RGB2BGR)
        buff.append(img)
        time.sleep(0.1)
        if keyboard.is_pressed('x'):
            break
        
    gif = imageio.mimsave('screen.gif', buff, 'GIF', duration=0.1)

