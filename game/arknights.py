import os
from time import sleep
import pyautogui


pyautogui.PAUSE = 2


def show_win():
    os.chdir('/Applications')
    os.system('open NemuPlayer.app')


def get_material():
    show_win()
    while 1:
        sleep(5)
        pyautogui.press('A')
        sleep(2)
        pyautogui.press('B')
        sleep(120)
        pyautogui.press('B')


def clear_base():
    pyautogui.press('O')
    pyautogui.press('L')
    pyautogui.press('P')
    pyautogui.press('M')
    pyautogui.press('G')

    choose_five()

    pyautogui.press('C')

    pyautogui.press('O')
    pyautogui.press('M')
    pyautogui.press('G')
    choose_five()

    pyautogui.press('C')



def choose_five():
    pyautogui.press('N')
    pyautogui.press('Q')
    pyautogui.press('R')
    pyautogui.press('S')
    pyautogui.press('T')

    pyautogui.press('A')
    pyautogui.press('C')
    pyautogui.press('C')


def clear_mission():
    pyautogui.press('D')

    pyautogui.press('E')
    for i in range(0, 30):
        pyautogui.press('G')

    pyautogui.press('F')
    for j in range(0, 15):
        pyautogui.press('G')

    pyautogui.press('C')


def clear_shop():
    pyautogui.press('H')
    pyautogui.press('I')
    pyautogui.press('F')

    pyautogui.press('C')


def recruit():
    pyautogui.press('J')
    pyautogui.press('K')
    pyautogui.press('M')

    pyautogui.press('K')
    for i in range(0, 9):
        pyautogui.press('N')
    pyautogui.press('O')

    pyautogui.press('L')
    pyautogui.press('M')
    pyautogui.press('L')
    for i in range(0, 9):
        pyautogui.press('N')
    pyautogui.press('O')

    pyautogui.press('C')


def daily():
    show_win()
    clear_shop()
    recruit()
    clear_base()
    clear_mission()