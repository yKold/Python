import pyautogui
valor = 1
while valor <= 1015:
    pyautogui.sleep(2)
    pyautogui.click(x=458, y=992)
    pyautogui.write(str(valor))
    pyautogui.press("enter")
    valor += 1

    pyautogui.sleep(2)
    pyautogui.click(x=1462, y=998)
    pyautogui.write(str(valor))
    pyautogui.press("enter")
    valor += 1
