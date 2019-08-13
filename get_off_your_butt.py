import ctypes
import time

#create textbox function
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

#run every 30 minutes for an 8-hour day
i = 0
for i in range(0,15):
    time.sleep(1800)
    Mbox('Hey You!', 'Get off your butt and move', 0)
    i = i + 1