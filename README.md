# Help Therapod Remember!

**Help Therapod Remember!** is a retro-inspired, Python-based, GUI-driven guessing game where you help **Therapod**, a quirky, animated caricature inspired by a physical thesis project, remember a secret word. Based on themes like animals, technology, and mythology, players receive increasingly helpful clues to guide their guesses.

---

## 🛠️ New & Updated Features (2025 Edition)

- **🚀 Enhanced Layout:**
  - Fully resizable interface with dynamic grid layout using `tkinter.grid()`
  - Intelligent frame resizing for the status log and bottom panel

- **🎨 Theme-Based Background Tinting:**
  - Each theme sets a unique vertical gradient background using `create_gradient_image()`
  - Background updates dynamically based on selected theme

- **🖼️ Improved Therapod Display:**
  - Therapod caricature is centered in a fixed 330x270 canvas
  - Now includes a bold black pixel-style border around the yellow frame
  - Therapod label added underneath, styled in retro header font

- **🧠 Cleaner Status Feedback:**
  - Left-aligned, consistent feedback log
  - Text tagged by type (guesses, scores, clues) with clear fonts and colors

- **🎧 Audio Feedback:**
  - Plays win/lose/guess/start sound effects
  - Volume slider + mute button integrated

- **📜 Game Flow Improvements:**
  - Auto-focuses guess input box after game start
  - Victory message now shows time, category, and leaderboard rank
  - Right frame no longer stretches Therapod when resizing

---

## Original Features (Carried Over)

- **Multiple Themes:**
  Select from dozens of categories like animals, planets, mythology, and languages.

- **Clue System:**
  Every word includes vague and helpful clues revealed progressively.

- **Stopwatch:**
  Stylized like a 7-segment digital timer, shows time taken during gameplay.

- **Leaderboard:**
  Stores your name, theme, time, and guesses in a JSON file. Filterable by theme.

- **Retro UI Design:**
  Styled with pixel borders, low-res display aesthetics, and custom font "Press Start 2P".

- **Background Music:**
  Plays looping bg_music.wav, with added feedback sfx for different game events.

---

## Installation

### 1. Clone the Project
```bash
git clone https://github.com/Aksol-Jade/Help-Therapod-Remember-
cd Help-Therapod-Remember-
```

### 2. Install Dependencies
```bash
pip install pygame pillow fuzzywuzzy python-Levenshtein
```

### 3. Set Up Assets
- Place emotion GIFs (`happy.gif`, `sad.gif`, etc.) inside `/face`
- Add `bg_music.wav`, `start.wav`, `guess.wav`, `win.wav`, `lose.wav` inside `/sounds`
- Install **Press Start 2P** font from [fontmeme.com](https://fontmeme.com/fonts/press-start-2p-font/) and place it into `C:/Windows/Fonts`
- Download WordNet manually:
  https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet.zip → Extract to:
  `C:/Users/<YourUser>/AppData/Roaming/nltk_data/corpora`

---

## Running the Game
```bash
python RA4.py
```

1. App window opens maximized
2. Enter your name
3. Select a theme
4. Click "Start Game"
5. Use hints to guess the word!

---

## File Structure
```
Help-Therapod-Remember/
├── RA4.py                 # Main game + GUI logic
├── clue_data.py          # Theme definitions + THEME_COLORS
├── face/                 # Animated emotion GIFs
├── sounds/               # Background music + feedback SFX
├── leaderboard.json      # Auto-generated player stats
├── README.md             # Project documentation
```

---

## Future Ideas
- LLM integration with LangChain for AI-generated hints
- More emotion GIFs or animations based on player performance
- Optional TTS output using Piper

---

## License
MIT License — See `LICENSE` file.

---

*Created by the THERAPOD (FALCORe) Group Booth Game Project — 2025.*

