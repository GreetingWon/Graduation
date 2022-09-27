import subprocess,time, os
import RPi.GPIO as GPIO
import threading
import os,time, signal

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)
#cmd = "python3 waiting.py -d ssd1351 -i spi --width 128 --height 128"
#blue = subprocess.Popen(cmd , stdout = subprocess.PIPE, shell = True).wait()
wait = subprocess.call("python3 waiting.py -d ssd1351 -i spi --width 128 --height 128", shell = True)
time.sleep(0.5)
os.system('kill -9 `pgrep -f waiting`')

def checkButton():
    try:
        while True:
            if GPIO.input(5) == GPIO.HIGH:
                os.system('kill -9 `pgrep -f direction`')
                camera = subprocess.call("python3 picamera_video.py -d ssd1351 -i spi --width 128 --height 128", shell = True)
                os.system('kill -9 `pgrep -f picamera_video`')
                direction = subprocess.call("python3 direction2.py -d ssd1351 -i spi --width 128 --height 128", shell = True)
                os.system('kill -9 `pgrep -f direction`')
                
                
    except KeyboardInterrupt:
        GPIO.cleanup()
    
t1 = threading.Thread(target=checkButton) #Make Thread
t1.start() #Start Thread

print("Hello")
direction = subprocess.call("python3 direction.py -d ssd1351 -i spi --width 128 --height 128", shell = True)
time.sleep(0.1)
        

