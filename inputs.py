from pynput.keyboard import Controller as kController, Key
import time

CONTROLLER = kController()
DEFAULT_HOLD = 0.02
DEFAULT_WAIT = 0.02

BUTTONS = {
    'start': Key.enter,
    'select': Key.backspace,
    'a': 'x',
    'b': 'z',
    'l': 'a',
    'r': 's',
    'up': Key.up,
    'down': Key.down,
    'left': Key.left,
    'right': Key.right
}

def press(key: Key, hold: float = DEFAULT_HOLD, wait: float = DEFAULT_WAIT):
    CONTROLLER.press(key)
    time.sleep(hold)
    CONTROLLER.release(key)
    time.sleep(wait)

def play(list: str):
    commands = []
    command = []
    with open(f'lists/{list}.in') as listfile:
        for line in listfile:
            line = line.strip()
            if len(line) > 0 and not line.startswith('//'):
                if line.startswith('x'):
                    for _ in range(int(line[1:])):
                        commands.append(command)
                else:
                    command = line.split(',')
                    commands.append(command)
    for command in commands:
        print(command)
        cl = len(command)
        if command[0] in BUTTONS:
            button = None
            wait = DEFAULT_WAIT
            hold = DEFAULT_HOLD
            button = BUTTONS[command[0]]
            if cl >= 2 and command[1] != '':
                wait = float(command[1])
            if cl >= 3 and command[2] != '':
                hold = float(command[2])
            press(button, hold, wait)
        else:
            time.sleep(float(command[0]))

    # commands = json.load(open(f'lists/{list}.json'))
    # for command in commands:
    #     if 'button' not in command and 'wait' in command:
    #         time.sleep(command['wait'])
    #     elif 'button' in command:
    #         button = BUTTONS[command['button']]
    #         hold = command['hold'] if 'hold' in command else DEFAULT_HOLD
    #         wait = command['wait'] if 'wait' in command else DEFAULT_WAIT
    #         press(button, hold, wait)
