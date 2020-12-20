import win32gui
import win32con
import win32api
from time import sleep
import ctypes
import pyautogui
import os
from fpdf import FPDF

####Print list of open window title, have user choose one
def selectWindowTitle():
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    
    titles = []
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)    

    print('\n****************\nAll Open Windows\n****************\n')
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(titles)))
    lIndex = int(input('Make your selection: '))
    return titles[lIndex]

####Grab the top left and bottom right coords of capture area
def getDimensions():
    print("\nMaintain focus on this script while performing the following:\n")
    print('Place cursor at top left corner of where you would like to take images and then press enter')
    input()
    coords = pyautogui.position()
    top_left_x = coords[0]
    top_left_y = coords[1]

    print('Place cursor at bottom right corner of where you would like to take images and then press enter')
    input()
    coords = pyautogui.position()
    bot_right_x = coords[0]
    bot_right_y = coords[1]

    left = top_left_x
    top = top_left_y
    width = bot_right_x - left
    height = bot_right_y - top

    return (left, top, width, height)

####Get Window name by title
windowName = selectWindowTitle()
####Get screenshot area dimensions
screenshotCoords = getDimensions()
####Get number of pages to capture
pages = int(input("How many pages should I capture? "))

####MAKE FOLDERNAME AND CREATE DIRECTORY
folderName = windowName.replace(" ", "_")
folderName = folderName.replace(":","--")
invalidCharacters = [' ','*','.','"',"'",'\\','/','[',']',':',';','|',',']
for c in invalidCharacters:
    folderName = folderName.replace(c,"-")

cmd = "mkdir " + folderName
print(cmd)
os.system(cmd)

####Get window and child for further use
hwndMain = win32gui.FindWindow(None, windowName)
hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)

####Countdown from 3 to 1, give user some time to change window focus
for i in range(3, 0, -1):
    print("Give focus to window you want to capture")
    print(str(i) + ' seconds remaining...')
    sleep(1.5)


imagelist = []

####Take a screenshot, flip the page, report the percentage, repeat
right_arrow = win32con.VK_RIGHT
for i in range(0, pages):
    pyautogui.screenshot(folderName + '/page'+ str(i) + '.png', region=screenshotCoords)
    imagelist.append(folderName + '/page' + str(i) + '.png')
    sleep(0.2)
    win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, right_arrow, 0)
    sleep(0.05)
    win32api.PostMessage(hwndChild, win32con.WM_KEYUP, right_arrow, 0)
    print("Taking screencaps...")
    percentage = (i/pages) * 100
    percentage = round(percentage,1)
    print(str(percentage) + '%')
    sleep(0.4)
    os.system("clear")
    os.system("cls")

pdf = FPDF()0
for image in imagelist:
    pdf.add_page()
    pdf.image(image,0,0,210,297)

print("Converting images into a pdf")

pdf.output(folderName + '/' + folderName + '.pdf', "F")

print("File: " + folderName + '/' + folderName + '.pdf was created.')


####Delete all the images
for image in imagelist:
    os.remove(image)
    print("Cleaning up images...")
    os.system("clear")
    os.system("cls")