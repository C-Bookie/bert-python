import colorsys

from phue import Bridge


def init():
    global light
    global b

    b = Bridge('192.168.0.170')
    b.connect()

    # Get the bridge state (This returns the full dictionary that you can explore)
    print(b.get_api())

    lights = b.lights

    # Print light names
    for l in lights:
        if l.name == "Cal's light":
            light = l
            print("light found")
            break

    if light is None:
        raise Exception("no light found")
    light.transitiontime = 10
    light.on = True


def draw(red, green, blue, C, T):
    global light
    colour = colorsys.rgb_to_hsv(red, green, blue)
    print(colour)
    light.hue = colour[0] * 65535
    light.brightness = colour[2] * 254
    light.saturation = colour[1] * 254



