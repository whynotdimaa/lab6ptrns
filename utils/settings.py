# systems/settings_manager.py
class SettingsManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SettingsManager, cls).__new__(cls)
        return cls._instance

    def setPreferredTemperature(self, temp):
        self.preferred_temperature = temp
        print(f"Preferred temperature set to {temp}°C.")

    def setLightingPreset(self, preset):
        self.lighting_preset = preset
        print(f"Lighting preset set to {preset}.")
