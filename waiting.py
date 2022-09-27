import math
import time
import threading
import os,time, signal

from PIL import Image, ImageDraw, ImageFont

from demo_opts import get_device
from luma.core.render import canvas

pid = os.getpid()

color = (255,0,0)
width = 3
i = 0

font_size = 20
font2_size = 15

font = ImageFont.truetype("FreeMono.ttf", font_size)
font2 = ImageFont.truetype("FreeMono.ttf", font2_size)

def stop():
    time.sleep(15)
    os.kill(pid,signal.SIGKILL)
    
t1 = threading.Thread(target=stop) #Make Thread
t1.start() #Start Thread

def posn(angle, arm_length):
    dx = int(math.cos(math.radians(angle)) * arm_length)
    dy = int(math.sin(math.radians(angle)) * arm_length)
    return (dx, dy)


def main():
    global i
    while True:
        with canvas(device) as draw:
            margin = 4

            cx = 30
            cy = min(device.height, 64) / 2

            left = cx - cy
            right = cx + cy

            draw.text((14, cy - 8), 'Bluetooth',color,font = font)
            draw.text((36,cy+20), 'Waiting', color, font = font2)
            
            if(i == 5) :
                i = 0
                
            if(i == 0) :
                draw.rectangle((20,cy+40,40,cy+45), outline =(255,0,0), width = 1)
                draw.rectangle((45,cy+40,65,cy+45), outline =(255,0,0), width = 1)
                draw.rectangle((70,cy+40,90,cy+45), outline =(255,0,0), width = 1)
                draw.rectangle((95,cy+40,115,cy+45), outline =(255,0,0), width = 1)
                time.sleep(1)
            elif(i == 1) :
                draw.rectangle((20,cy+40,40,cy+45), outline =(255,0,0), width = 3)
                draw.rectangle((45,cy+40,65,cy+45), outline =(255,0,0), width = 1)
                draw.rectangle((70,cy+40,90,cy+45), outline =(255,0,0), width = 1)
                draw.rectangle((95,cy+40,115,cy+45), outline =(255,0,0), width = 1)
                time.sleep(1)
            elif(i == 2) :
                draw.rectangle((20,cy+40,40,cy+45), outline =(255,0,0), width = 3)
                draw.rectangle((45,cy+40,65,cy+45), outline =(255,0,0), width = 3)
                draw.rectangle((70,cy+40,90,cy+45), outline =(255,0,0), width = 1)
                draw.rectangle((95,cy+40,115,cy+45), outline =(255,0,0), width = 1)
                time.sleep(1)
            elif(i == 3) :
                draw.rectangle((20,cy+40,40,cy+45), outline =(255,0,0), width = 3)
                draw.rectangle((45,cy+40,65,cy+45), outline =(255,0,0), width = 3)
                draw.rectangle((70,cy+40,90,cy+45), outline =(255,0,0), width = 3)
                draw.rectangle((95,cy+40,115,cy+45), outline =(255,0,0), width = 1)
                time.sleep(1)
            elif(i == 4) :
                draw.rectangle((20,cy+40,40,cy+45), outline =(255,0,0), width = 3)
                draw.rectangle((45,cy+40,65,cy+45), outline =(255,0,0), width = 3)
                draw.rectangle((70,cy+40,90,cy+45), outline =(255,0,0), width = 3)
                draw.rectangle((95,cy+40,115,cy+45), outline =(255,0,0), width = 3)
                time.sleep(1)
            
        i = i + 1
        time.sleep(0.5)


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass