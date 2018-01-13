
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


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
    image = Image.new('1', (width, height))

    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)


def draw(red, green, blue, C, T):
    #    print("Red: " + str(r) + " Green: " + str(g) + " Blue: " + str(b))

    disp.clear()

    y = 0
    while True:
        x = 0
        while x < width:
            p = C[(y * width) + x]
            draw.point([x, y], 1)
            x += 1
            if (y * width) + x >= len(C):
                return
        y += 1

def paint():
    disp.image(image)
    disp.display()
    return

