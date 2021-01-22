import pyautogui
import keyboard
import imageio

STOPP=False
Buff = []
while True:
    if keyboard.is_pressed('s'):
        print('starting')
        while True:
            im = pyautogui.screenshot()
            Buff.append(im)
            if keyboard.is_pressed('x'):
                print("stopping...")
                STOP=True
                break
    if STOPP:
        break

gif = imageio.mimsave('screen.gif', Buff, 'GIF', duration=0.3)
