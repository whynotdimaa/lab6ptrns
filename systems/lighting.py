# systems/lighting.py
class LightingSystem:
    def __init__(self):
        self.lights_on = False
        self.brightness = 0

    def turnOnLights(self):
        self.lights_on = True
        print("Lights are on.")

    def turnOffLights(self):
        self.lights_on = False
        print("Lights are off.")

    def setBrightness(self, level):
        self.brightness = level
        print(f"Brightness set to {level}.")
