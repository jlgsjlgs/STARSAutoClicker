import pyautogui
import time

try: 
    while True:
        pyautogui.click(1141,935)
        time.sleep(1)
        pyautogui.click(335,635)
        time.sleep(1)
        pyautogui.click(330,681)
        time.sleep(2.5)
except KeyboardInterrupt:
    sys.exit(0)

