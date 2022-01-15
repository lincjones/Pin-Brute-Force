import pyautogui
import string
import time
time.sleep(3)
from random import choice
chars = string.digits
random =  ''.join(choice(chars) for _ in range(4))
msg = random
n = 9999
for i in range(0,int(n)):
  chars = string.digits
  random =  ''.join(choice(chars) for _ in range(4))
  msg = random
  pyautogui.typewrite(str(msg))
  pyautogui.press('enter')