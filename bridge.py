# bridge.py
class RemoteControl:
    def __init__(self, appliance):
        self.appliance = appliance

    def turn_on(self):
        self.appliance.start()

    def turn_off(self):
        self.appliance.stop()

class Appliance:
    def start(self):
        pass

    def stop(self):
        pass

class Fan(Appliance):
    def start(self):
        print("Fan is turned on.")

    def stop(self):
        print("Fan is turned off.")

class Light(Appliance):
    def start(self):
        print("Light is turned on.")

    def stop(self):
        print("Light is turned off.")
