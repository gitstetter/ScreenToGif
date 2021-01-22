from PIL import ImageGrab
import numpy as np
import cv2 as cv
import time, pyautogui, keyboard, imageio
 
stop=False
buff = []
while True:
    if keyboard.is_pressed('s'):
        print('starting')
        while True:
            im = pyautogui.screenshot()
            img = cv.cvtColor(np.array(im), cv.COLOR_RGB2BGR)
            buff.append(img)
            time.sleep(0.1)
            if keyboard.is_pressed('x'):
                print("stopping...")
                stop=True
                break
    if stop:
        break
    
gif = imageio.mimsave('screen.gif', buff, 'GIF', duration=0.3)
