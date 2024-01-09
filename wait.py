import SH1106
import config
import time
from gpiozero import CPUTemperature

from PIL import Image,ImageDraw,ImageFont

def main(disp):
    deepSleep = False
    disp.clear()
    time.sleep(1)
    counter = 0
    while(True):
        if not(disp.RPI.digital_read(disp.RPI.GPIO_KEY3_PIN ) == 0):
            time.sleep(1)
            break
        # Deep sleep
        if not (deepSleep):
            counter +=1
        if(counter > 100000000) or (deepSleep == True):
            print("Deep sleep triggered")
            time.sleep(45)
            deepSleep = True
        else:
            print(CPUTemperature().temperature)
            time.sleep(6)

