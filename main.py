# coding: utf-8
import argparse
import pyautogui
import csv
from pyhooked import Hook, MouseEvent, KeyboardEvent

actions = []

class ActionRepeater:

    actions = []

    def __init__(self, info_file="temp.csv"):
        self.info_file = info_file
    
    def write(self, useKeyboard=False):
        def __writeFile__(self, filename):
            pass
        
        def __hook__(self, HookEvent):
            pass

        def __isClick__(self, tpl_twoActions):
            pass

        def __isDbClick__(self, tpl_fourActions):
            pass
        
        pass

    def repeat(self, count):
        def __readFile__(self, filename):
            pass
        pass

def writer(logfile):
    global actions
    
    def hook_mouse(args):
        if isinstance(args, MouseEvent):
            coords = pyautogui.position()
            mouse_x = coords[0]
            mouse_y = coords[1]

            actions.append(
                {
                    'mouse_x': mouse_x,
                    'mouse_y': mouse_y,
                    'event_type': args.event_type
                 }
            )

            len_actions = len(actions)
            
            if len_actions % 2 == 0:
                last = actions.pop()
                print(last)
                prelast = actions.pop()
                print(prelast)

                if last['mouse_x'] == prelast['mouse_x']:
                    if last['mouse_y'] == prelast['mouse_y']:
                        print("Click found")
                        actions.append(
                            {
                                'mouse_x' : last['mouse_x'],
                                'mouse_y' : last['mouse_y'],
                                'action' : 'click'
                            }
                        )
            
            
        if isinstance(args, KeyboardEvent):
            if args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                hk.stop()

    hk = Hook()
    hk.handler = hook_mouse
    hk.hook(mouse=True)
    print(actions)
    
    with open(logfile, 'w') as csvfile:
        fieldnames = ['mouse_x', 'mouse_y', 'action']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'mouse_x': '0', 'mouse_y': '50', 'action':'click'})
        writer.writerow({'mouse_x': '10', 'mouse_y': '220', 'action':'dbclick'})
        writer.writerow({'mouse_x': '500', 'mouse_y': '450', 'action':'click'})
    

def clicker(logfile):
    with open(logfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mouse_x = int(row['mouse_x'])
            mouse_y = int(row['mouse_y'])
            action = row['action']
            pyautogui.moveTo(mouse_x, mouse_y, duration=0.5)
            
            if row['action'] == 'click':
                pyautogui.click()
            elif row['action'] == 'dbclick':
                pyautogui.doubleClick()

def argsInit():
    argparser = argparse.ArgumentParser(
        description="")
    group = argparser.add_mutually_exclusive_group()
    group.add_argument(
        "-c", "--count",
        type=int,
        default=1,
        help="Means how many times to repeat. Min value = 1 and Max value = Inf")
    group.add_argument(
        "-w", "--write",
        action="store_true",
        help="Add it if you want to write actions")

    argparser.add_argument(
        "-f", "--filename",
        type=str,
        default="temp.csv",
        help="Name of file to write")
    argparser.add_argument(
        "-k", "--keyboard",
        action="store_true",
        help="Use it if you want to catch the keyboard events")
    #add subparsers
    return argparser.parse_args()

if __name__ == "__main__":
    logfile = "log.csv"
    args = argsInit()
    print(args)
    """if args.write:
        writer(logfile)
    else:
        clicker(logfile)
"""
