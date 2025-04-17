# RA_GUI.py
import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import json
import os
import pygame
from PIL import Image, ImageTk, ImageDraw, ImageColor
from game_logic import (
    similarity_score,
    get_vague_clue,
    get_helpful_clue,
    get_response_from_score,
)
from clue_data import THEMES, THEME_COLORS
from sound_manager import SoundManager  # Import our sound manager subscript

# Font definitions (using Courier New as fallback; install your retro font if available)
retro_font = ("Press Start 2P", 9)
retro_font_large = ("Press Start 2P", 14)
retro_font_header = ("Press Start 2P", 22)

# Color variables
GRADIENT_TOP = "#ffecd2"
GRADIENT_BOTTOM = "#fcb69f"
BG_COLOR = "#ffffff"
HEADER_BG = "#f7f7f7"
HEADER_FG = "#ff6f61"
TEXT_FG = "#333333"
BUTTON_BG = "#ff6f61"
BUTTON_FG = "#ffffff"

# For most UI boxes
POKEMON_BOX_BG = "#F8E8C0"
POKEMON_BORDER_COLOR = "#000000"

# For the Therapod (GIF) panel, we now use a pure yellow background.
CAT_BG = "yellow"

LEADERBOARD_FILE = "leaderboard.json"

def create_gradient_image(width, height, color1, color2):
    base = Image.new("RGB", (width, height), color1)
    top_r, top_g, top_b = ImageColor.getrgb(color1)
    bot_r, bot_g, bot_b = ImageColor.getrgb(color2)
    gradient = Image.new("RGB", (width, height), color1)
    draw = ImageDraw.Draw(gradient)
    for y in range(height):
        ratio = y / height
        r = int(top_r + (bot_r - top_r) * ratio)
        g = int(top_g + (bot_g - top_g) * ratio)
        b = int(top_b + (bot_b - top_b) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return ImageTk.PhotoImage(gradient)

# Initialize pygame mixer (background music handled separately)
pygame.mixer.init()

class ReverseAkinatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.state("zoomed")
        self.title("Help Therapod Remember!")
        self.configure(bg=BG_COLOR)
        self.resizable(True, True)
        
        # Background music setup.
        self.current_volume = 0.5
        self.is_muted = False
        try:
            pygame.mixer.music.load("sounds/bg_music.wav")
            pygame.mixer.music.play(-1)  # Loop indefinitely
            pygame.mixer.music.set_volume(self.current_volume)
        except Exception as e:
            print("Error loading background music:", e)
        
        # Create the background gradient.
        self.bg_image = create_gradient_image(self.winfo_width(), self.winfo_height(), GRADIENT_TOP, GRADIENT_BOTTOM)
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Game variables.
        self.guesses = 0
        self.best_guess = ("", 0)
        self.target_word = ""
        self.theme = ""
        self.player_name = ""
        self.current_emotion = "surprise"
        self.start_time = None
        
        # Animated GIF data.
        self.emotion_frames = {}
        self.cached_frames = {}
        self.resized_emotion_frames = []
        self.current_frame_index = 0
        self.animation_job = None
        
        self.load_emotion_images()
        
        # Initialize sound manager.
        self.sound_manager = SoundManager()
        
        self.create_widgets()
        self.bind("<Configure>", self.on_window_resize)
        self.start_game()
    
    def load_emotion_images(self):
        emotions = ["angry", "fear", "happy", "love", "sad", "surprise"]
        for emotion in emotions:
            try:
                im = Image.open(f"face/{emotion}.gif")
            except Exception as e:
                print(f"Error loading {emotion}.gif: {e}")
                continue
            frames = []
            try:
                while True:
                    frame = im.copy().convert("RGBA")
                    frames.append(frame)
                    im.seek(len(frames))
            except EOFError:
                pass
            self.emotion_frames[emotion] = frames
   
    def create_widgets(self):
        # Main grid: header, main UI, bottom stats.
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        # Header Frame.
        self.header_frame = tk.Frame(self, bg=HEADER_BG, highlightthickness=4, highlightbackground=POKEMON_BORDER_COLOR)
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20,10))
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.title_label = tk.Label(self.header_frame, text="Help Therapod Remember!",
                                    font=retro_font_header, bg=HEADER_BG, fg=HEADER_FG)
        self.title_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.subtitle_label = tk.Label(self.header_frame,
                                       text="Can you help Therapod remember the word he is looking for?",
                                       font=retro_font, bg=HEADER_BG, fg=TEXT_FG)
        self.subtitle_label.grid(row=1, column=0, sticky="w", padx=10, pady=(0,10))
        
        # Main Game UI Frame.
        self.main_frame = tk.Frame(self, bg=BG_COLOR)
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=3)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Left Panel.
        self.left_frame = tk.Frame(self.main_frame, bg=POKEMON_BOX_BG,
                                   highlightthickness=4, highlightbackground=POKEMON_BORDER_COLOR)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0,10))
        self.left_frame.grid_rowconfigure(2, weight=4)  # status box taller
        self.left_frame.grid_rowconfigure(3, weight=1)  # guess box expands
        self.left_frame.grid_columnconfigure(0, weight=1)
        
        # Name Entry.
        self.name_frame = tk.Frame(self.left_frame, bg=POKEMON_BOX_BG)
        self.name_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        self.name_frame.grid_columnconfigure(1, weight=1)
        self.name_label = tk.Label(self.name_frame, text="Enter Name:", font=retro_font,
                                   bg=POKEMON_BOX_BG, fg=TEXT_FG)
        self.name_label.grid(row=0, column=0, sticky="w", padx=5)
        self.name_entry = tk.Entry(self.name_frame, font=retro_font,
                                   highlightthickness=2, highlightbackground=POKEMON_BORDER_COLOR,
                                   bg="#FFFFFF")
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5)
        
        # Top Controls: Group theme selection and Start Game, then divider, then volume controls.
        self.top_controls = tk.Frame(self.left_frame, bg=POKEMON_BOX_BG)
        self.top_controls.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        # Configure columns:
        # Column 0: Theme label.
        # Column 1: Theme dropdown.
        # Column 2: Start Game button.
        # Column 3: Divider.
        # Column 4: Volume slider.
        # Column 5: Mute button.
        self.top_controls.grid_columnconfigure(0, weight=0)
        self.top_controls.grid_columnconfigure(1, weight=1)
        self.top_controls.grid_columnconfigure(2, weight=0)
        self.top_controls.grid_columnconfigure(3, weight=0)
        self.top_controls.grid_columnconfigure(4, weight=1)
        self.top_controls.grid_columnconfigure(5, weight=0)
        
        # Group 1: Theme selection and Start Game.
        self.theme_label = tk.Label(self.top_controls, text="Select a Theme:", font=retro_font,
                                    bg=POKEMON_BOX_BG, fg=TEXT_FG)
        self.theme_label.grid(row=0, column=0, sticky="w", padx=(5,2))
        self.theme_var = tk.StringVar(self)
        self.theme_var.set(list(THEMES.keys())[0])
        self.theme_menu = ttk.OptionMenu(self.top_controls, self.theme_var, list(THEMES.keys())[0], *THEMES.keys())
        self.theme_menu.grid(row=0, column=1, sticky="w", padx=(0,5))
        self.start_button = ttk.Button(self.top_controls, text="Start Game", command=self.start_game)
        self.start_button.grid(row=0, column=2, padx=5)
        
        # Divider.
        divider = tk.Frame(self.top_controls, bg=POKEMON_BORDER_COLOR, width=2, height=20)
        divider.grid(row=0, column=3, padx=10)
        
        # Group 2: Volume controls.
        self.volume_slider = tk.Scale(self.top_controls, from_=0, to=100, orient=tk.HORIZONTAL,
                                      command=self.update_volume, bg=POKEMON_BOX_BG, fg=TEXT_FG,
                                      font=retro_font, sliderlength=20)
        self.volume_slider.set(50)
        self.volume_slider.grid(row=0, column=4, sticky="ew", padx=5)
        self.mute_button = ttk.Button(self.top_controls, text="Mute", command=self.toggle_mute)
        self.mute_button.grid(row=0, column=5, padx=5)
        
        # Status Display Box.
        self.status_text = tk.Text(self.left_frame, fg=TEXT_FG, font=retro_font,
                                    wrap=tk.WORD, height=10,
                                    highlightthickness=4, highlightbackground=POKEMON_BORDER_COLOR,
                                    bg="#FDF5E6")
        self.status_text.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        
        # Guess Frame.
        self.guess_frame = tk.Frame(self.left_frame, bg=POKEMON_BOX_BG,
                                    highlightthickness=4, highlightbackground=POKEMON_BORDER_COLOR)
        self.guess_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        self.guess_frame.grid_columnconfigure(1, weight=1)
        guess_label = tk.Label(self.guess_frame, text="Your Guess:", font=retro_font,
                               bg=POKEMON_BOX_BG, fg=TEXT_FG)
        guess_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.guess_entry = tk.Entry(self.guess_frame, font=retro_font,
                                    highlightthickness=3, highlightbackground=POKEMON_BORDER_COLOR,
                                    bg="#FFFFFF")
        self.guess_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.guess_entry.bind("<Return>", self.process_guess)
        self.guess_entry.focus_set()
        self.submit_button = ttk.Button(self.left_frame, text="Submit Guess", command=self.process_guess)
        self.submit_button.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        
        # Status Text Tags.
        # Updated text styles for better clarity
        self.status_text.tag_config("header", foreground="#F39C12", font=("Press Start 2P", 11, "bold"))
        self.status_text.tag_config("guess", foreground="#34495E", font=("Press Start 2P", 9, "bold"))
        self.status_text.tag_config("score", foreground="#2980B9", font=("Press Start 2P", 8, "italic"))
        self.status_text.tag_config("response", foreground="#D35400", font=("Press Start 2P", 9))
        self.status_text.tag_config("vague", foreground="#16A085", font=("Press Start 2P", 9, "italic"))
        self.status_text.tag_config("helpful", foreground="#8E44AD", font=("Press Start 2P", 9, "bold"))
        self.status_text.tag_config("correct", foreground="#27AE60", font=("Press Start 2P", 11, "bold"))
        self.status_text.tag_config("error", foreground="#C0392B", font=("Press Start 2P", 9, "bold"))
        
        # Right Panel: Therapod-style GIF Box.
        self.right_frame = tk.Frame(self.main_frame, bg=POKEMON_BOX_BG,
                                    highlightthickness=4, highlightbackground=POKEMON_BORDER_COLOR)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.right_frame.grid_propagate(False)
        self.cat_canvas = tk.Canvas(self.right_frame, bg=CAT_BG,
                                    highlightthickness=0, width=330, height=270)
        self.cat_canvas.pack(anchor="center", pady=10) 
        self.therapod_label = tk.Label(self.right_frame,
            text="'Can you help Therapod?'",
            font=retro_font_large,
            bg=POKEMON_BOX_BG,
            fg=HEADER_FG,
            wraplength=300,    # Limits label width before wrapping
            justify="center")
        self.therapod_label.pack(pady=(5, 10))
        # Draw a thick retro pixelated border.
        self.cat_canvas.create_rectangle(2, 2, 328, 268, outline="black", width=6)
        # Extra pixel accents for a detailed look.
        for x in range(10, 290, 20):
            self.cat_canvas.create_rectangle(x, 215, x+10, 220, fill=POKEMON_BORDER_COLOR, outline=POKEMON_BORDER_COLOR)
        for y in range(30, 210, 20):
            self.cat_canvas.create_rectangle(0, y, 5, y+5, fill=POKEMON_BORDER_COLOR, outline=POKEMON_BORDER_COLOR)
            self.cat_canvas.create_rectangle(295, y, 300, y+5, fill=POKEMON_BORDER_COLOR, outline=POKEMON_BORDER_COLOR)
        # Draw ears.
        self.cat_canvas.create_polygon(40, 10, 60, 0, 80, 10,
                                       fill=CAT_BG, outline=POKEMON_BORDER_COLOR, width=2)
        self.cat_canvas.create_polygon(220, 10, 240, 0, 260, 10,
                                       fill=CAT_BG, outline=POKEMON_BORDER_COLOR, width=2)
        # Draw feet.
        self.cat_canvas.create_oval(10, 190, 70, 230, fill="white", outline=POKEMON_BORDER_COLOR, width=2)
        self.cat_canvas.create_oval(230, 190, 290, 230, fill="white", outline=POKEMON_BORDER_COLOR, width=2)
        # Center the GIF.
        self.gif_label = tk.Label(self.cat_canvas, bg=CAT_BG)
        self.cat_canvas.create_window(150, 120, window=self.gif_label)
        
        # Bottom Frame: Stopwatch and Leaderboard.
        self.bottom_frame = tk.Frame(self, bg=BG_COLOR)
        self.bottom_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=4)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_rowconfigure(2, weight=0)
        
        # Stopwatch Panel.
        self.stopwatch_frame = tk.Frame(self.bottom_frame, bg=POKEMON_BOX_BG,
                                        highlightthickness=4, highlightbackground=POKEMON_BORDER_COLOR)
        self.stopwatch_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.stopwatch_label = tk.Label(self.stopwatch_frame, text="00:00:00", font=("Courier New", 30, "bold"),
                                        bg="black", fg="red")
        self.stopwatch_label.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Leaderboard Panel.
        self.leaderboard_frame = tk.Frame(self.bottom_frame, bg=POKEMON_BOX_BG,
                                          highlightthickness=4, highlightbackground=POKEMON_BORDER_COLOR)
        self.leaderboard_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.leaderboard_frame.grid_columnconfigure(0, weight=1)
        self.leaderboard_title = tk.Label(self.leaderboard_frame, text="Leaderboard", font=retro_font_large,
                                          bg=POKEMON_BOX_BG, fg=HEADER_FG)
        self.leaderboard_title.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.filter_frame = tk.Frame(self.leaderboard_frame, bg=POKEMON_BOX_BG)
        self.filter_frame.grid(row=1, column=0, sticky="ew", padx=10)
        self.filter_frame.grid_columnconfigure(0, weight=1)
        self.filter_frame.grid_columnconfigure(1, weight=1)
        self.filter_label = tk.Label(self.filter_frame, text="Filter by Theme:", font=retro_font,
                                     bg=POKEMON_BOX_BG, fg=TEXT_FG)
        self.filter_label.grid(row=0, column=0, sticky="w", padx=5)
        self.leaderboard_filter_var = tk.StringVar(self)
        self.leaderboard_filter_var.set("All")
        filter_options = ["All"] + list(THEMES.keys())
        self.leaderboard_filter = ttk.OptionMenu(self.filter_frame, self.leaderboard_filter_var, *filter_options,
                                                 command=lambda _: self.update_leaderboard_display())
        self.leaderboard_filter.grid(row=0, column=1, sticky="ew", padx=5)
        self.leaderboard_text = tk.Text(self.leaderboard_frame, fg=TEXT_FG, font=retro_font,
                                        height=10, state="disabled", wrap=tk.WORD,
                                        highlightthickness=4, highlightbackground=POKEMON_BORDER_COLOR,
                                        bg="#FDF5E6")
        self.leaderboard_text.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.leaderboard_frame.grid_rowconfigure(2, weight=1)
        
        self.start_animation("surprise")
        self.start_feedback = tk.Label(self, text="Game Started! Get Ready to Play!",
                                       font=retro_font_large, fg=HEADER_FG, bg=BG_COLOR)
        self.start_feedback.place(relx=0.5, rely=0.5, anchor="center")
        self.start_feedback.lower()
        
    def update_volume(self, value):
        vol = int(value) / 100.0
        self.current_volume = vol
        if not self.is_muted:
            pygame.mixer.music.set_volume(vol)
            
    def toggle_mute(self):
        if self.is_muted:
            self.is_muted = False
            pygame.mixer.music.set_volume(self.current_volume)
            self.mute_button.config(text="Mute")
        else:
            self.is_muted = True
            pygame.mixer.music.set_volume(0)
            self.mute_button.config(text="Unmute")
            
    def update_stopwatch(self):
        if self.start_time is None:
            return
        elapsed = int(time.time() - self.start_time)
        hrs = elapsed // 3600
        mins = (elapsed % 3600) // 60
        secs = elapsed % 60
        time_str = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        self.stopwatch_label.config(text=time_str)
        self.after(1000, self.update_stopwatch)
        
    def update_leaderboard_display(self):
        leaderboard = []
        # Ensure the filter menu always includes "All"
        filter_options = ["All"] + list(THEMES.keys())
        menu = self.leaderboard_filter["menu"]
        menu.delete(0, "end")
        for option in filter_options:
            menu.add_command(label=option, command=lambda value=option: (self.leaderboard_filter_var.set(value), self.update_leaderboard_display()))

        if os.path.exists(LEADERBOARD_FILE):
            with open(LEADERBOARD_FILE, "r") as f:
                try:
                    leaderboard = json.load(f)
                except Exception:
                    leaderboard = []
        selected_theme = self.leaderboard_filter_var.get()
        if selected_theme != "All":
            leaderboard = [entry for entry in leaderboard if entry["theme"] == selected_theme]
        leaderboard.sort(key=lambda x: (x["guesses"], x["time"]))
        display_text = "Rank\tName\tGuesses\tTime\tTheme\n"
        for idx, entry in enumerate(leaderboard, start=1):
            display_text += f"{idx}\t{entry['name']}\t{entry['guesses']}\t{entry['time']}s\t{entry['theme']}\n"
        self.leaderboard_text.config(state="normal")
        self.leaderboard_text.delete("1.0", tk.END)
        self.leaderboard_text.insert(tk.END, display_text)
        self.leaderboard_text.config(state="disabled")
        
    def update_leaderboard(self, name, guesses, elapsed):
        leaderboard = []
        if os.path.exists(LEADERBOARD_FILE):
            with open(LEADERBOARD_FILE, "r") as f:
                try:
                    leaderboard = json.load(f)
                except Exception:
                    leaderboard = []
        leaderboard.append({"name": name, "guesses": guesses, "time": elapsed, "theme": self.theme})
        leaderboard.sort(key=lambda x: (x["guesses"], x["time"]))
        with open(LEADERBOARD_FILE, "w") as f:
            json.dump(leaderboard, f, indent=4)
        self.update_leaderboard_display()
        
    def on_window_resize(self, event):
        new_width = self.winfo_width()
        new_height = self.winfo_height()
        self.bg_image = create_gradient_image(new_width, new_height, GRADIENT_TOP, GRADIENT_BOTTOM)
        self.bg_label.config(image=self.bg_image)
        self.bg_label.image = self.bg_image
        self.start_animation(self.current_emotion)
        
    def choose_emotion(self, score):
        if score < 10:
            return "angry"
        elif score < 30:
            return "sad"
        elif score < 50:
            return "fear"
        elif score < 70:
            return "surprise"
        elif score < 95:
            return "happy"
        else:
            return "love"
        
    def start_animation(self, emotion):
        frame_width, frame_height = 300, 220
        cache_key = (emotion, frame_width, frame_height)
        if emotion != self.current_emotion or cache_key not in getattr(self, "cached_frames", {}):
            self.current_emotion = emotion
            if not hasattr(self, "cached_frames"):
                self.cached_frames = {}
            if cache_key in self.cached_frames:
                self.resized_emotion_frames = self.cached_frames[cache_key]
            else:
                original_frames = self.emotion_frames.get(emotion, [])
                frames = []
                try:
                    resample = Image.Resampling.LANCZOS
                except AttributeError:
                    resample = Image.LANCZOS
                for frame in original_frames:
                    resized_frame = frame.resize((frame_width, frame_height), resample)
                    photo = ImageTk.PhotoImage(resized_frame)
                    frames.append(photo)
                self.resized_emotion_frames = frames
                self.cached_frames[cache_key] = frames
            self.current_frame_index = 0
        self.animate()
        
    def animate(self):
        if not self.resized_emotion_frames:
            return
        photo = self.resized_emotion_frames[self.current_frame_index]
        self.gif_label.config(image=photo)
        self.gif_label.image = photo
        self.current_frame_index = (self.current_frame_index + 1) % len(self.resized_emotion_frames)
        self.animation_job = self.after(250, self.animate)
        
    def start_game(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Missing Name", "Please enter your name before starting the game.")
            return
        self.player_name = name
        self.theme = self.theme_var.get()
        self.target_word = random.choice(THEMES[self.theme])
        self.guesses = 0
        self.best_guess = ("", 0)
        self.status_text.delete("1.0", tk.END)
        self.status_text.insert(tk.END, f"Theme: {self.theme}\n", "header")
        self.status_text.insert(tk.END, "Guess the secret word related to the theme! 🤔\n", "header")
        # Play start sound.
        self.sound_manager.play_start_sound()
        self.start_animation("surprise")
        self.start_time = time.time()
        if self.theme in THEME_COLORS:
            top_color, bottom_color = THEME_COLORS[self.theme]
            self.bg_image = create_gradient_image(self.winfo_width(), self.winfo_height(), top_color, bottom_color)
            self.bg_label.config(image=self.bg_image)
            self.bg_label.image = self.bg_image
        self.update_stopwatch()
        self.show_start_feedback()
        self.guess_entry.focus_set()
        
    def process_guess(self, event=None):
        guess = self.guess_entry.get().strip().lower()
        self.guess_entry.delete(0, tk.END)
        # Play guess sound for each guess input.
        self.sound_manager.play_guess_sound()
        if guess == "exit":
            self.status_text.insert(tk.END, f"\n❌ Game over! The secret word was: {self.target_word}\n", "error")
            self.sound_manager.play_lose_sound()
            self.status_text.see(tk.END)
            return

        score = similarity_score(guess, self.target_word)
        self.guesses += 1

        new_emotion = self.choose_emotion(score)
        if new_emotion != self.current_emotion:
            self.start_animation(new_emotion)

        self.status_text.insert(tk.END, f"\n💬 Guess: {guess} | ", "guess")
        self.status_text.insert(tk.END, f"⭐ Similarity Score: {score}%\n", "score")

        if score == 100:
            elapsed = int(time.time() - self.start_time)
            self.sound_manager.play_win_sound()
            self.update_leaderboard(self.player_name, self.guesses, elapsed)

            # Load leaderboard to determine placement
            leaderboard = []
            if os.path.exists(LEADERBOARD_FILE):
                with open(LEADERBOARD_FILE, "r") as f:
                    try:
                        leaderboard = json.load(f)
                    except Exception:
                        leaderboard = []

            # Sort and find rank
            leaderboard.sort(key=lambda x: (x["guesses"], x["time"]))
            player_rank = next((i+1 for i, entry in enumerate(leaderboard)
                                if entry["name"] == self.player_name and
                                entry["guesses"] == self.guesses and
                                entry["time"] == elapsed and
                                entry["theme"] == self.theme), "N/A")

            # Display win details
            self.status_text.insert(tk.END, f"\n🎉 Correct! The word was '{self.target_word}'.\n", "correct")
            self.status_text.insert(tk.END, f"🏆 Theme: {self.theme}\n", "header")
            self.status_text.insert(tk.END, f"⏱️ Time: {elapsed} seconds\n", "header")
            self.status_text.insert(tk.END, f"🥇 Leaderboard Rank: {player_rank}\n", "header")
            self.status_text.see(tk.END)
            return

        if score > self.best_guess[1]:
            self.best_guess = (guess, score)

        response = get_response_from_score(guess, score)
        self.status_text.insert(tk.END, f"\n{response}\n", "response")

        if self.guesses % 3 == 0:
            vague_clue = get_vague_clue(self.target_word)
            self.status_text.insert(tk.END, f"\n💡 Vague Clue: {vague_clue}\n", "vague")
        if self.guesses % 5 == 0:
            helpful_clue = get_helpful_clue(self.target_word)
            self.status_text.insert(tk.END, f"\n🔑 Helpful Clue: {helpful_clue}\n", "helpful")

        self.status_text.see(tk.END)

    def show_start_feedback(self):
        self.start_feedback.lift()
        self.start_feedback.after(2000, lambda: self.start_feedback.lower())

    def on_window_resize(self, event):
        new_width = self.winfo_width()
        new_height = self.winfo_height()
        self.bg_image = create_gradient_image(new_width, new_height, GRADIENT_TOP, GRADIENT_BOTTOM)
        self.bg_label.config(image=self.bg_image)
        self.bg_label.image = self.bg_image
        self.start_animation(self.current_emotion)

if __name__ == "__main__":
    app = ReverseAkinatorGUI()
    app.mainloop()
