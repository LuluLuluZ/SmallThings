from time import sleep
import pyautogui

pyautogui.PAUSE = 2


def daily_login():
    friend()
    guild()
    clocklibrary()
    jjc_image()
    mission()


def guild():
    pyautogui.press('J')
    pyautogui.press('L')
    for i in range(0, 10):
        print('M')
        sleep(1)
    pyautogui.press('C')

    pyautogui.press('E')
    pyautogui.press('N')
    sleep(20)
    pyautogui.press('C')
    pyautogui.press('C')
    pyautogui.press('O')

    pyautogui.press('P')


def friend():
    pass


def clocklibrary():
    pass


def mission():
    pyautogui.press('I')
    for i in range(0, 5):
        pyautogui.press('R')

    pyautogui.press('P')


def info():
    pyautogui.press('A')
    pyautogui.press('D')
    pyautogui.press('T')
    for i in range(0, 5):
        pyautogui.press('F')
        for i in range(0, 10):
            pyautogui.press('E')
        sleep(150)


def jjc_image():
    pyautogui.press('O')
    pyautogui.press('H')
    for i in range(0, 5):
        pyautogui.press('M')
        sleep(3)
        pyautogui.press('P')
        sleep(3)
    pyautogui.press('P')
    pyautogui.press('S')
    pyautogui.press('V')
    pyautogui.press('S')
    pyautogui.press('W')