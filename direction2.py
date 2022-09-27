import sys
import threading
import os,time, signal
import RPi.GPIO as GPIO

from pathlib import Path
from demo_opts import get_device


from PIL import Image

pid = os.getpid()
      
GPIO.setmode(GPIO.BCM)

#GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():  
    img_path = str(Path(__file__).resolve().parent.joinpath('images', '1.png'))
    pic = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - pic.width) // 2, 0)
  
    background.paste(pic, posn)
    device.display(background.convert(device.mode))
    time.sleep(60)
    
    img_path = str(Path(__file__).resolve().parent.joinpath('images', '8.png'))
    pic = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - pic.width) // 2, 0)
  
    background.paste(pic, posn)
    device.display(background.convert(device.mode))
    time.sleep(5)
    
    img_path = str(Path(__file__).resolve().parent.joinpath('images', '2.png'))
    pic = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - pic.width) // 2, 0)
  
    background.paste(pic, posn)
    device.display(background.convert(device.mode))
    time.sleep(10)
    
    img_path = str(Path(__file__).resolve().parent.joinpath('images', '13.png'))
    pic = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - pic.width) // 2, 0)
  
    background.paste(pic, posn)
    device.display(background.convert(device.mode))
    time.sleep(10)
    
        
#def stop():
#    time.sleep(10)
#    os.kill(pid,signal.SIGKILL)
    
#t1 = threading.Thread(target=stop) #Make Thread
#t1.start() #Start Thread

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass