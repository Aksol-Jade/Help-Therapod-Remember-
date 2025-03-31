# NOTE
 Appreciate 2025, THERAPOD(FALCORe) group booth game. 

 ------
https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet.zip
Use this link to get WordNet and add to C:\Users\<YourUser>\AppData\Roaming\nltk_data\corpora

The above is a bypass way to install wordnet as it is a large file even when zipped

--------
https://fontmeme.com/fonts/press-start-2p-font/
This is a necessary font for the design. Install and place into C:/Windows/Fonts and install

--------
bg_music.wav must be placed in the same dir as the project. The original .wav file is not included as it's size is too large.

# Help Therapod Remember!

**Reverse Akinator** is a Python-based, GUI-driven guessing game inspired by the classic Akinator. In this game, players guess a secret word related to a selected theme. The game provides vague and helpful clues, tracks guesses, measures time with a 7‑segment–style stopwatch, and maintains a leaderboard that ranks players based on the number of guesses and elapsed time.

## Features

- **Multiple Themes:**  
  Choose from various themes (animals, fruits, countries, instruments, planets, colors, sports, jobs, and more newly added themes like vehicles, mythology, technology, and languages).

- **Clues System:**  
  Each word in the game comes with three unique vague clues and three helpful clues to guide your guesses.

- **GUI Interface:**  
  Built with Tkinter, the game includes:
  - A header with game title and subtitle.
  - A player name input (required before starting).
  - Top controls including theme selection, start button, volume slider, and mute/unmute button.
  - A status display area for showing guess feedback.
  - A custom right-panel featuring a cat-themed (Therapod) box for animated GIFs.
  - A 7‑segment style stopwatch.
  - A leaderboard that updates with each game, with an option to filter by theme.

- **Animated Feedback:**  
  Animated GIFs reflect the game state and emotional responses (e.g., "surprise", "happy").

- **Background Music:**  
  Background music (bg_music.wav) plays on loop with volume and mute controls.

- **Persistent Leaderboard:**  
  Game results (player name, number of guesses, time taken, and theme) are stored in a JSON file and can be filtered by theme.

## Installation

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/reverse-akinator.git
   cd reverse-akinator
   ```

2. **Install Dependencies:**  
   Ensure you have Python 3.10 or later. Install required packages using pip:
   ```bash
   pip install pygame pillow fuzzywuzzy python-Levenshtein
   ```
   (If fuzzywuzzy or python-Levenshtein is not required for your version, adjust accordingly.)

3. **Set Up Assets:**  
   - Place your animated GIF files for the emotions (named `angry.gif`, `fear.gif`, `happy.gif`, `love.gif`, `sad.gif`, `surprise.gif`) inside a folder named `face` in the project directory.
   - Ensure the background music file `bg_music.wav` is in the project directory.
   - Verify that your `clue_data.py` (or `themes_and_clues.py`) file is present with the themes and clues.

## Usage

To run the game, simply execute:

```bash
python RA_GUI.py
```

When the application starts:
- The window will open maximized (bordered).
- Enter your name in the provided field.
- Select a theme from the dropdown.
- Adjust the volume and mute/unmute using the controls on the top right.
- Click "Start Game" to begin.
- Use the status display for clues and feedback.
- The stopwatch will record your time, and the leaderboard will update at the end of the game.

## File Structure

```
reverse-akinator/
├── RA_GUI.py             # Main GUI script
├── game_logic.py         # Contains scoring functions and clue retrieval functions
├── clue_data.py          # Themes and clues definitions
├── TTSpeech.py           # (Optional) Text-to-speech integration using Piper
├── face/                 # Folder containing animated GIFs for each emotion
│   ├── angry.gif
│   ├── fear.gif
│   ├── happy.gif
│   ├── love.gif
│   ├── sad.gif
│   └── surprise.gif
├── bg_music.wav          # Background music file
└── leaderboard.json      # JSON file storing leaderboard data (generated at runtime)
```

## Customization

- **Themes & Clues:**  
  You can modify or expand `clue_data.py` to add new themes and update clues.

- **Background Music:**  
  Replace `bg_music.wav` with your desired track (ensure it’s in a supported format).

- **GUI Layout & Styling:**  
  The GUI is built using Tkinter. Feel free to adjust colors, fonts, and layout in `RA_GUI.py` to suit your design preferences.

## Troubleshooting

- **GIF Loading/Animation Issues:**  
  Ensure the GIF files are named correctly and located in the `face` folder. Adjust animation delays in `RA_GUI.py` if needed.

- **Background Music Issues:**  
  If you encounter errors loading `bg_music.wav`, verify the file format (must be a standard PCM WAV or OGG file).

- **Dependency Errors:**  
  Make sure all required packages are installed. Use `pip install -r requirements.txt` if you create one.

## Future Improvements

- Integrate advanced TTS using the TTSpeech.py module.
- Enhance animations or add additional interactive elements.
- Add more detailed player statistics and game modes.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this README to better match your project details and style. Enjoy developing Reverse Akinator!
