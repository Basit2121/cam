import pyautogui
import time
pyautogui.FAILSAFE=False
first = None
while first is None:
    first = pyautogui.locateOnScreen('first.png', grayscale=True, confidence=0.8)
    if first is not None:
        first = pyautogui.center(first)
        pyautogui.leftClick(first)
        time.sleep(0.5)
        pyautogui.leftClick(first)
    else:
        print('Looking For Start...')
time.sleep(2)
second = None
while second is None:
    second = pyautogui.locateOnScreen('second.png', grayscale=True, confidence=0.8)
    if second is not None:
        second = pyautogui.center(second)
        pyautogui.leftClick(second)
        time.sleep(0.5)
        pyautogui.leftClick(second)
    else:
        print('Looking For Start...')
time.sleep(2)
third = None
while third is None:
    third = pyautogui.locateOnScreen('third.png', grayscale=True, confidence=0.8)
    if third is not None:
        third = pyautogui.center(third)
        pyautogui.leftClick(third)
        time.sleep(0.5)
        pyautogui.leftClick(third)
    else:
        print('Looking For Start...')