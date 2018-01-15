
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import math

import RPi.GPIO as GPIO


def init():
    global disp
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=24)
    disp.begin()
    disp.clear()
    disp.display()

    global width
    width= disp.width
    global height
    height = disp.height
    global image


    global font
    font = ImageFont.load_default()

#    global pixels
#    pixels = image.load()
#    draw.rectangle((0,0,width,height), outline=0, fill=0)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    GPIO.output(6, GPIO.LOW)    #red led
    GPIO.output(12, GPIO.LOW)   #blue
    GPIO.output(13, GPIO.LOW)   #green

    global ledB
    ledB = GPIO.PWM(12, 50)
    ledB.start(10)

    global ledG
    ledG = GPIO.PWM(13, 50)
    ledG.start(10)



def draw(red, green, blue, C, T):
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)

    size = 4
    subWidth = width/size

    x=0
    y = 0
    while (y * subWidth) + x < len(C):
        x = 0
        while x < subWidth:
            p = 1 if C[(y * subWidth) + x] > T/2 else 0
#            box(x, y, size, p)
            draw.rectangle((x*size, y*size, (x*size)+size, (y*size)+size), outline=0, fill=p)
            x += 1
        y += 1
    dp = 10**2

    draw.text((0, y*size+5), "R:" + str(math.floor(red*dp)/dp) + " G:" + str(math.floor(green*dp)/dp) + " B:" + str(math.floor(blue*dp)/dp), font=font, fill=255)
    paint(image)
    del draw

#    print("Red: " + str(red) + " Green: " + str(green) + " Blue: " + str(blue))
    GPIO.output(6,  GPIO.LOW if red == 0 else GPIO.HIGH)
    ledG.ChangeDutyCycle(green*10)
    ledB.ChangeDutyCycle(blue*10)


def box(x, y, s, p):
    py=0
    while py < s:
        px=0
        while px < s:
#            pixels[(x*s)+px, (y*s)+py] = p
            px+=1
        py+=1

def paint(newImage):
    disp.clear()
    disp.image(newImage)
    disp.display()

def kill():
    p.stop()
    del disp
    GPIO.cleanup()

