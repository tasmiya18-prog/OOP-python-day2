# Parent class 1
class Camera:
    def _init_(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print(f"Camera Quality: {self.camera_quality}")

# Parent class 2
class MusicPlayer:
    def _init_(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print(f"Sound Quality: {self.sound_quality}")

# Child class inheriting from Camera and MusicPlayer
class SmartPhone(Camera, MusicPlayer):
    def _init_(self, brand, camera_quality, sound_quality):
        Camera._init_(self, camera_quality)  # Calling Camera constructor
        MusicPlayer._init_(self, sound_quality)  # Calling MusicPlayer constructor
        self.brand = brand

    def display_smartphone_details(self):
        print(f"Brand: {self.brand}")
        self.display_camera_details()
        self.display_music_details()

# Create an object of SmartPhone
smartphone = SmartPhone("Samsung", "48MP", "Dolby Atmos")

# Display smartphone details
smartphone.display_smartphone_details()
