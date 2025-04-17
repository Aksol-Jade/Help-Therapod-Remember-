# sound_manager.py
import pygame
import os

class SoundManager:
    def __init__(self):
        # Initialize the mixer; you may adjust frequency/buffer if needed.
        pygame.mixer.init()
        self.sounds = {}
        self.load_all_sounds()

    def load_all_sounds(self):
        """Preload all sound effects into a dictionary."""
        self.sounds["start"] = self.load_sound("sounds/start.wav")
        self.sounds["win"]   = self.load_sound("sounds/win.wav")
        self.sounds["lose"]  = self.load_sound("sounds/lose.wav")
        self.sounds["guess"] = self.load_sound("sounds/guess.wav")

    def load_sound(self, filename):
        """Load a sound file if it exists; return None if not found."""
        if os.path.exists(filename):
            try:
                return pygame.mixer.Sound(filename)
            except Exception as e:
                print(f"Error loading sound {filename}: {e}")
                return None
        else:
            print(f"Sound file {filename} not found.")
            return None

    def play_sound(self, key):
        """Play a sound by its key if available."""
        sound = self.sounds.get(key)
        if sound:
            sound.play()
        else:
            print(f"No sound loaded for key '{key}'.")

    def play_start_sound(self):
        """Play the start sound."""
        self.play_sound("start")

    def play_win_sound(self):
        """Play the win sound (e.g., dun dun dun)."""
        self.play_sound("win")

    def play_lose_sound(self):
        """Play the lose sound (e.g., a buzz)."""
        self.play_sound("lose")

    def play_guess_sound(self):
        """Play a sound when a guess is entered."""
        self.play_sound("guess")

# For testing purposes:
if __name__ == "__main__":
    pygame.init()
    sm = SoundManager()
    print("Playing start sound...")
    sm.play_start_sound()
    pygame.time.delay(1000)
    print("Playing win sound...")
    sm.play_win_sound()
    pygame.time.delay(1000)
    print("Playing lose sound...")
    sm.play_lose_sound()
    pygame.time.delay(1000)
    print("Playing guess sound...")
    sm.play_guess_sound()
    pygame.time.delay(1000)
    pygame.quit()
