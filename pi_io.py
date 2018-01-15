
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import math


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


def draw(red, green, blue, C, T):
#    print("Red: " + str(r) + " Green: " + str(g) + " Blue: " + str(b))
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)

    size = 4
    subWidth = width/size

    x=0
    y = 0
    while (y * subWidth) + x < len(C):
        x = 0
        while x < subWidth:
            p = C[(y * subWidth) + x] > T/2 if 1 else 0
#            box(x, y, size, p)
            draw.rectangle((x*size, y*size, (x*size)+size, (y*size)+size), outline=0, fill=p)
            x += 1
        y += 1
    dp = 10^2


    draw.text((0, y*size+5), "R:" + str(math.floor(red*dp)/dp) + " G:" + str(math.floor(green*dp)/dp) + " B:" + str(math.floor(blue*dp)/dp), font=font, fill=255)
    paint(image)
    del draw


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

