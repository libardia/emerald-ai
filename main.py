import pyautogui as gui
import time

if __name__ == '__main__':
    result = gui.locateOnWindow('img/logo.png', 'mGBA - 0.9.3')
    print(result)
