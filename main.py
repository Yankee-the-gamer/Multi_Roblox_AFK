import subprocess
from win32 import win32gui
import time
from win32.lib import win32con
import sys
from pynput.mouse import Button, Controller




def find_all_windows(name):
    result = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == name:
            result.append(hwnd)
    win32gui.EnumWindows(winEnumHandler, None)
    return result

def autoclicker():
    mouse = Controller()

    while True:
        roblox = find_all_windows("Roblox")
        for i in roblox:
            mouse.position = (1267, 119)
            win32gui.ShowWindow(i, win32con.SW_MAXIMIZE)
            time.sleep(0.2)
            
            mouse.click(Button.left, 2)
            time.sleep(0.3)

            
            win32gui.ShowWindow(i, win32con.SW_MINIMIZE)
        time.sleep(300)
        


if __name__ == "__main__":
    

    cmd = win32gui.FindWindow(None, "Roblox")
    if cmd == 0:
        raise Exception("Roblox has to be running first for this to work")
    else:
        cmd = subprocess.run(["Handle.exe", "-a", "ROBLOX_singletonEvent"], shell=True, stdout = subprocess.PIPE)
        print(f"{cmd}")
        iSuckAtRegex = f"{cmd}".split("pid:")[1].split(': \\')[0]
        Pid_Hid = iSuckAtRegex.replace("type: Event", "").split()   
        cmd = subprocess.run(["Handle.exe", "-c", f"{Pid_Hid[1]}", "-p", f"{Pid_Hid[0]}"], text=True, shell=True, check=True, input='y',  stdout = subprocess.PIPE)


    print("Run the autoclicker now? y/n")
    choice = input().lower()
    if choice == "y":
        autoclicker()
    else:
        sys.exit()


=======
import subprocess
from win32 import win32gui
import time
from win32.lib import win32con
import sys
from pynput.mouse import Button, Controller




def find_all_windows(name):
    result = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == name:
            result.append(hwnd)
    win32gui.EnumWindows(winEnumHandler, None)
    return result

def autoclicker():
    mouse = Controller()

    while True:
        roblox = find_all_windows("Roblox")
        for i in roblox:
            mouse.position = (1267, 119)
            win32gui.ShowWindow(i, win32con.SW_MAXIMIZE)
            time.sleep(0.2)
            
            mouse.click(Button.left, 2)
            time.sleep(0.3)

            
            win32gui.ShowWindow(i, win32con.SW_MINIMIZE)
        time.sleep(300)
        


if __name__ == "__main__":
    

    cmd = win32gui.FindWindow(None, "Roblox")
    if cmd == 0:
        raise Exception("Roblox has to be running first for this to work")
    else:
        cmd = subprocess.run(["Handle.exe", "-a", "ROBLOX_singletonEvent"], shell=True, stdout = subprocess.PIPE)
        print(f"{cmd}")
        iSuckAtRegex = f"{cmd}".split("pid:")[1].split(': \\')[0]
        Pid_Hid = iSuckAtRegex.replace("type: Event", "").split()   
        cmd = subprocess.run(["Handle.exe", "-c", f"{Pid_Hid[1]}", "-p", f"{Pid_Hid[0]}"], text=True, shell=True, check=True, input='y',  stdout = subprocess.PIPE)


    print("Run the autoclicker now? y/n")
    choice = input().lower()
    if choice == "y":
        autoclicker()
    else:
        sys.exit()

