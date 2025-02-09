import pyautogui
import time

def click_at(x, y):
    pyautogui.click(x, y)

def write_text(x, y, text):
    pyautogui.click(x, y)
    pyautogui.write(text, interval=0.1)

pyautogui.hotkey('winleft', '3')
time.sleep(2)
click_at(154, 76)
pyautogui.write("https://elevenlabs.io/app/sign-up", interval=0.1)
pyautogui.press("enter")
time.sleep(5)
write_text(351, 602, "your_email@example.com")
write_text(351, 700, "your_secure_password")
click_at(218, 818)
time.sleep(1)
click_at(545, 888)
