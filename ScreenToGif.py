import logging

import imageio
import keyboard
import pyautogui
from pynput.mouse import Listener

logging.basicConfig(format='%(asctime)s | %(levelname)s | Line: %(lineno)s | %(message)s',level=logging.INFO)

def on_click(x, y, button, pressed):
    if pressed:
        global x_start, y_start
        x_start = x
        y_start = y
    if not pressed:
        global x_end, y_end
        x_end = x
        y_end = y
        return False


CROPPED=False
STOP=False
Buff = []

while True:
    if keyboard.is_pressed('f1'):
        logging.info('Cropping enabled')
        with Listener(on_click=on_click) as listener:
            listener.join()
        CROPPED=True
        logging.info(f'Cropped Area is: {x_start},{y_start}, {x_end}, {y_end}')


    if keyboard.is_pressed('f2'):
        logging.info('Start recording...')
        while True:           
            im = pyautogui.screenshot()
            if CROPPED:
                im =im.crop(box=(x_start*2,y_start*2, x_end*2, y_end*2))              
            Buff.append(im)
            if keyboard.is_pressed('f3'):
                logging.info("Stopping...")
                STOP=True
                break
    if STOP:
        break

gif = imageio.mimsave('screen.gif', Buff, 'GIF', duration=0.2)
