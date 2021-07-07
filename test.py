import argparse
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
import random
import sys


print("Starting...")
client = OpenRGBClient()
parser = argparse.ArgumentParser(description='RGB Switching program')
parser.add_argument("--off", help="turns lights off", action="store_true")
args = parser.parse_args()

print(args.off)

if args.off:
    client.clear()
    client.off()
    print("Turning lights off")
    sys.exit()

devs = client.devices

print(client.devices)

for dev in devs:
    print(dev.modes)
    print(dev.zones)
    print(dev.colors)

    r = lambda: random.randint(0,255)
    color = '#{:02x}{:02x}{:02x}'.format(r(), r(), r())
    dev.set_color(RGBColor.fromHEX(color))    
    dev.zones[0].set_color(RGBColor.fromHEX(color))
