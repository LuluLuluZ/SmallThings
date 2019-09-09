from time import sleep
import pyautogui
from game.arknights import show_win

pyautogui.PAUSE = 0.5


def producer_daily():
    show_win()
    friend()
    jjc()
    guild()


def friend():
    pyautogui.press('A')


def jjc():
    pyautogui.press('A')
    choose_three_cards()

    pyautogui.press('A')
    pyautogui.press('A')
    pyautogui.press('A')


def choose_three_cards():
    pyautogui.press('A')
    pyautogui.press('B')
    sleep(3)
    pyautogui.press('B')

    pyautogui.press('A')
    pyautogui.press('B')
    sleep(3)
    pyautogui.press('B')

    pyautogui.press('B')
    pyautogui.press('C')
    pyautogui.press('D')
    pyautogui.press('E')
    for i in range(0, 4):
        pyautogui.press('F')
        sleep(1)

    pyautogui.press('G')


def go_to_meet():
    pass


def guild():
    pyautogui.press('A')
    pyautogui.press('I')
    pyautogui.press('G')
    pyautogui.press('J')

    pyautogui.press('C')
    pyautogui.press('K')

    pyautogui.press('J')
    pyautogui.press('J')