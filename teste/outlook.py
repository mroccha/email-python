
import pyautogui
import time

def bot():

    pyautogui.press('winleft')
    time.sleep(1)
    pyautogui.write('Outlook')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl','o')
    time.sleep(1)
    pyautogui.write('marianarocha1424@gmail.com')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write("Teste")
    pyautogui.press('tab')
    pyautogui.write('Olá teste!')
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(8)
    pyautogui.hotkey('alt','space')
    pyautogui.press('up')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('enter')


bot()



