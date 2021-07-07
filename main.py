import time
import pyautogui
def sendmessage():
    time.sleep(0.01)
    text=open('spam.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
while True:
    sendmessage()