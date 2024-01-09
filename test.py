#!/usr/bin/python
# -*- coding:utf-8 -*-

import SH1106
import time
import config
import traceback
import wait

from PIL import Image,ImageDraw,ImageFont

selectionPosition = 0
menuScreenPosition = 0
menuList = {"SMB", "FTP", "HTTP", "USB"}
menuPage = {"File Transfer", "Bad USB", "Wireless", "Recon", "Connect", "Settings"}

disp = SH1106.SH1106()
image1 = Image.new('1', (disp.width, disp.height), "WHITE")
draw = ImageDraw.Draw(image1)
font = ImageFont.truetype('Font.ttf', 20)
font10 = ImageFont.truetype('Font.ttf',13)



def drawBackground():
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    draw.line([(0,0),(127,0)], fill = 0)
    draw.line([(0,0),(0,63)], fill = 0)
    draw.line([(0,63),(127,63)], fill = 0)
    draw.line([(127,0),(127,63)], fill = 0)


def drawBorders():
    draw.line([(0,0),(127,0)], fill = 0)
    draw.line([(0,0),(0,63)], fill = 0)
    draw.line([(0,63),(127,63)], fill = 0)
    draw.line([(127,0),(127,63)], fill = 0)


def drawSelector():
    selector = "<="
    xPosition = 80
    
    if(selectionPosition == 0):
        draw.text((xPosition,2), selector, font = font10, fill = 0)
    elif(selectionPosition == 1):
        draw.text((xPosition,14), selector, font = font10, fill = 0)
    elif(selectionPosition == 2):
        draw.text((xPosition,26), selector, font = font10, fill = 0)
    elif(selectionPosition == 3):
        draw.text((xPosition,38), selector, font = font10, fill = 0)
    else:
        print("Error! Selector outside of range!")


def drawMenu():

    menuTextLocationY = 2
    for option in menuList:
        draw.text((30,menuTextLocationY), option, font = font10, fill = 0)
        menuTextLocationY += 12


def drawLogos():
    Himage2 = Image.new('1', (disp.width, disp.height), 255)  # 255: clear the frame
    bmp = Image.open('portahack.bmp')
    Himage2.paste(bmp, (0,5))
    
    # Himage2=Himage2.rotate(180)
    logoDraw = ImageDraw.Draw(Himage2)
    logoDraw.text((80,2), "Port", font = font10, fill = 0)
    logoDraw.text((80,14), " -A-", font = font10, fill = 0)
    logoDraw.text((80,26), "Hack", font = font10, fill = 0)
    
    disp.ShowImage(disp.getbuffer(Himage2))

    print("Image should be drawn")
    time.sleep(2)





try:
    print(disp.width, " ", disp.height)
    drawBackground()
    drawLogos()
    time.sleep(5)
    while(True):
        drawMenu()
        drawSelector()
        image1=image1.rotate(0)
        disp.ShowImage(disp.getbuffer(image1))
        

        if not(disp.RPI.digital_read(disp.RPI.GPIO_KEY_UP_PIN ) == 0):
            if not (selectionPosition == 0):
                selectionPosition -= 1
                drawSelector()
                time.sleep(0.25)
            else:
                selectionPosition = 3
                drawSelector()
                time.sleep(0.5)
        if not(disp.RPI.digital_read(disp.RPI.GPIO_KEY_DOWN_PIN ) == 0):
            if not (selectionPosition == 3):
                selectionPosition += 1
                drawSelector()
                time.sleep(0.25)
            else:
                selectionPosition = 0
                drawSelector()
                time.sleep(0.25)


        if not(disp.RPI.digital_read(disp.RPI.GPIO_KEY3_PIN ) == 0):
            print("Waiting")
            time.sleep(1)
            wait.main(disp)
            drawLogos()
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        font = ImageFont.truetype('Font.ttf', 20)
        font10 = ImageFont.truetype('Font.ttf',13)
        drawBorders()
        

except IOError as e:
    print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    disp.RPI.module_exit()
    exit()
