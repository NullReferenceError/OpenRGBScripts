from openrgb import OpenRGBClient

print("Turning off...")
client = OpenRGBClient()

client.clear()
client.off()
print("Turning lights off")
