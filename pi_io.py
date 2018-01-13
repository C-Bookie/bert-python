
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

    global pixels
    pixels = image.load()
#    draw = ImageDraw.Draw(image)
#    draw.rectangle((0,0,width,height), outline=0, fill=0)


def draw(red, green, blue, C, T):
    #    print("Red: " + str(r) + " Green: " + str(g) + " Blue: " + str(b))

    size = 4
    subWidth = width/size

    disp.clear()

    y = 0
    while True:
        x = 0
        while x < subWidth:
#            p = C[(y * subWidth) + x] > T/2 if 1 else 0
            p = (x+y)%2
            box(x, y, size, p)
#            draw.point([x, y], 1)
            x += 1
            if (y * subWidth) + x >= len(C):
                return
        y += 1

def box(x, y, s, p):
    py=0
    while py < s:
        px=0
        while px < s:
            pixels[x+px, y+py] = p
            px+=1
        py+=1

def paint():
    disp.image(image)
    disp.display()
    return

