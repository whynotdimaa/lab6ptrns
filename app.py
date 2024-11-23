# app.py
from fastapi import FastAPI
from facade import SmartHomeFacade

app = FastAPI()

smart_home = SmartHomeFacade()

@app.get("/security/arm")
def arm_security():
    smart_home.activateSecuritySystem()
    return {"status": "Security system armed."}

@app.get("/security/disarm")
def disarm_security():
    smart_home.deactivateSecuritySystem()
    return {"status": "Security system disarmed."}

@app.get("/climate/set/{temperature}")
def set_temperature(temperature: int):
    smart_home.setClimateControl(temperature)
    return {"status": f"Temperature set to {temperature}°C."}

@app.get("/lighting/{action}")
def control_lighting(action: str, brightness: int = None):
    if action == "on":
        smart_home.controlLighting("on")
    elif action == "off":
        smart_home.controlLighting("off")
    elif action == "set":
        smart_home.controlLighting("set", brightness)
    return {"status": f"Lighting action '{action}' executed."}

@app.get("/music/play")
def play_music():
    smart_home.playMusic()
    return {"status": "Music is playing."}

@app.get("/music/stop")
def stop_music():
    smart_home.stopMusic()
    return {"status": "Music stopped."}

@app.get("/energy/monitor")
def monitor_energy():
    smart_home.monitorEnergyUsage()
    return {"status": "Energy usage is being monitored."}

@app.get("/energy/optimize")
def optimize_energy():
    smart_home.optimizeEnergy()
    return {"status": "Energy optimization in progress."}


@app.get("/home")
def get_home():
    return {"message": "This is the home page"}


