# systems/security.py
class SecuritySystem:
    def __init__(self):
        self.is_armed = False

    def armSystem(self):
        self.is_armed = True
        print("Security system armed.")

    def disarmSystem(self):
        self.is_armed = False
        print("Security system disarmed.")

    def triggerAlarm(self):
        if self.is_armed:
            print("Alarm triggered!")
        else:
            print("System is not armed. Can't trigger alarm.")
