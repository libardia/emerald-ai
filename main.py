import pyautogui as gui
from pynput.keyboard import Controller as kController, Key
import subprocess
import time
import inputs
from threading import Thread

if __name__ == '__main__':
    # Start the emulator
    emulator = Thread(target=lambda: subprocess.run(['bin/emulator/mGBA.exe', 'bin/rom/emerald.zip']))
    emulator.start()

    t = 6
    print(f'Starting in {t} seconds...')
    time.sleep(t)

    inputs.play('start')

    # End
    print('Done.')
    emulator.join()
