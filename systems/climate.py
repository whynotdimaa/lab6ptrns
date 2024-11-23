# systems/climate_.py
class ClimateSystem:
    def __init__(self):
        self.temperature = 22  # default temperature in Celsius

    def setTemperature(self, targetTemp):
        self.temperature = targetTemp
        print(f"Temperature set to {targetTemp}°C.")

    def turnOnHeater(self):
        print("Heater is on.")

    def turnOnAC(self):
        print("Air conditioning is on.")
