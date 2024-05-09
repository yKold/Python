import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=718, y=357)
pyautogui.write("Eu consegui fazer!")
pyautogui.press("space")
pyautogui.click(x=728, y=455)
pyautogui.write("123456789")
pyautogui.press("enter")
time.sleep(3)

import pandas

tabela = pandas.read_csv("JornadaPython\produtos.csv")
