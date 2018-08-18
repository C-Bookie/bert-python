
import sys

text=""
line=0

def init():
    return

def draw(r, g, b, C, T):
    global text
    global line

    text="Red: " + str(r) + " Green: " + str(g) + " Blue: " + str(b) + "\n"

    size = 4
    width = 128

    x = 0
    y = 0
    while (y * width) + x < len(C):
        x = 0
        while x < width:
            p = C[(y * width) + x] > T / 2 if 1 else 0
            text+="#" if p else " "
            x += 1
        text+="\n"
        line+=1
        y += 1

    paint()

def paint():
    global line
    global text
    while line>0:
        text="\033[F"+text
        line-=1
    sys.stdout.write(text)
