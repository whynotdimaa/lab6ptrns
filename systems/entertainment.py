# systems/entertainment.py
class EntertainmentSystem:
    def __init__(self):
        self.is_playing = False
        self.volume = 5

    def playMusic(self):
        self.is_playing = True
        print("Music is playing.")

    def stopMusic(self):
        self.is_playing = False
        print("Music stopped.")

    def setVolume(self, level):
        self.volume = level
        print(f"Volume set to {level}.")
