import pyautogui
import keyboard
import imageio
from pynput.mouse import Listener

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
        print('cropping enabled')
        with Listener(on_click=on_click) as listener:
            listener.join()
        CROPPED=True
        print('Cropped Area is:')
        print(x_start,y_start, x_end, y_end)

    if keyboard.is_pressed('f2'):
        print('Start recording...')
        while True:           
            im = pyautogui.screenshot()
            if CROPPED:
                im =im.crop(box=(x_start*2,y_start*2, x_end*2, y_end*2))              
            Buff.append(im)
            if keyboard.is_pressed('f3'):
                print("Stopping...")
                STOP=True
                break
    if STOP:
        #print(x_start,y_start, x_end-x_start, y_end-y_start)

        break

gif = imageio.mimsave('screen.gif', Buff, 'GIF', duration=0.3)
