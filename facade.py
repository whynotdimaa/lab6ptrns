# facade.py
from systems.lighting import LightingSystem
from systems.security import SecuritySystem
from systems.climate import ClimateSystem
from systems.entertainment import EntertainmentSystem
from systems.energy import EnergyManager
from utils.settings import SettingsManager


class SmartHomeFacade:
    def __init__(self):
        self.lighting_system = LightingSystem()
        self.security_system = SecuritySystem()
        self.climate_system = ClimateSystem()
        self.entertainment_system = EntertainmentSystem()
        self.energy_manager = EnergyManager()
        self.settings_manager = SettingsManager()

    def activateSecuritySystem(self):
        self.security_system.armSystem()

    def deactivateSecuritySystem(self):
        self.security_system.disarmSystem()

    def setClimate(self, temperature):
        self.climate.setTemperature(temperature)

    def controlLighting(self, action, brightness=None):
        if action == "on":
            self.lighting_system.turnOnLights()
        elif action == "off":
            self.lighting_system.turnOffLights()
        elif action == "set":
            self.lighting_system.setBrightness(brightness)

    def playMusic(self):
        self.entertainment_system.playMusic()

    def stopMusic(self):
        self.entertainment_system.stopMusic()

    def monitorEnergyUsage(self):
        self.energy_manager.monitorUsage()

    def optimizeEnergy(self):
        self.energy_manager.optimizeEnergy()

    def setSettings(self, temperature, lighting_preset):
        self.settings_manager.setPreferredTemperature(temperature)
        self.settings_manager.setLightingPreset(lighting_preset)
