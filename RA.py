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
from clue_data import THEMES

# A fresh, engaging aesthetic color scheme:
GRADIENT_TOP = "#ffecd2"      # Soft cream at the top
GRADIENT_BOTTOM = "#fcb69f"   # Warm peach at the bottom
BG_COLOR = "#ffffff"          # White background for panels/overlays
HEADER_BG = "#f7f7f7"         # Light header background
HEADER_FG = "#ff6f61"         # Vibrant accent for header text
TEXT_FG = "#333333"           # Dark text for clarity
BUTTON_BG = "#ff6f61"         # Matching accent for buttons
BUTTON_FG = "#ffffff"         # White text for buttons
CAT_BG = "yellow"             # Yellow background for the cat-themed box

LEADERBOARD_FILE = "leaderboard.json"

def create_gradient_image(width, height, color1, color2):
    """
    Create a vertical gradient image from color1 to color2.
    Returns an ImageTk.PhotoImage.
    """
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

class ReverseAkinatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # Start maximized (zoomed) with borders.
        self.state("zoomed")
        self.title("Help Therapod Remember!")
        self.configure(bg=BG_COLOR)
        self.resizable(True, True)
        
        # Initialize pygame mixer and background music.
        pygame.mixer.init()
        self.current_volume = 0.5
        self.is_muted = False
        try:
            pygame.mixer.music.load("bg_music.wav")
            pygame.mixer.music.play(-1)  # Loop indefinitely.
            pygame.mixer.music.set_volume(self.current_volume)
        except Exception as e:
            print("Error loading background music:", e)
        
        # Set up gradient background.
        self.bg_image = create_gradient_image(self.winfo_width(), self.winfo_height(), GRADIENT_TOP, GRADIENT_BOTTOM)
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Initialize game variables.
        self.guesses = 0
        self.best_guess = ("", 0)
        self.target_word = ""
        self.theme = ""
        self.player_name = ""
        self.current_emotion = "surprise"  # Default emotion
        self.start_time = None  # For stopwatch
        
        # For animated GIFs:
        self.emotion_frames = {}          # Original frames per emotion
        self.cached_frames = {}           # Cached resized frames (keyed by (emotion, width, height))
        self.resized_emotion_frames = []  # Currently active cached frames
        self.current_frame_index = 0
        self.animation_job = None
        
        self.load_emotion_images()
        self.create_widgets()
        self.bind("<Configure>", self.on_window_resize)
        self.start_game()
        
    def load_emotion_images(self):
        """Load all emotion GIFs from the 'face' folder as lists of PIL Image frames."""
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
        # Main grid: three rows (header, main game UI, bottom stats).
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Header Frame (Row 0)
        self.header_frame = tk.Frame(self, bg=HEADER_BG)
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20,10))
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.title_label = tk.Label(self.header_frame, text="Help Therapod Remember!",
                                    font=("Segoe UI", 28, "bold"), bg=HEADER_BG, fg=HEADER_FG)
        self.title_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.subtitle_label = tk.Label(self.header_frame, text="Can you help remind therapod what word he's thinking of?",
                                       font=("Segoe UI", 16), bg=HEADER_BG, fg=TEXT_FG)
        self.subtitle_label.grid(row=1, column=0, sticky="w", padx=10, pady=(0,10))
        
        # Main Game UI Frame (Row 1)
        self.main_frame = tk.Frame(self, bg=BG_COLOR)
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=3)  # Left panel
        self.main_frame.grid_columnconfigure(1, weight=1)  # Right panel
        
        # Left Panel (Game UI)
        self.left_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0,10))
        self.left_frame.grid_columnconfigure(0, weight=1)
        
        # Player Name Entry (required)
        self.name_frame = tk.Frame(self.left_frame, bg=BG_COLOR)
        self.name_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        self.name_frame.grid_columnconfigure(1, weight=1)
        self.name_label = tk.Label(self.name_frame, text="Enter Name:", bg=BG_COLOR,
                                   fg=TEXT_FG, font=("Segoe UI", 14, "bold"))
        self.name_label.grid(row=0, column=0, sticky="w", padx=5)
        self.name_entry = tk.Entry(self.name_frame, font=("Segoe UI", 12))
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5)
        
        # Top Controls: theme dropdown, start button, volume slider, and mute button.
        self.top_controls = tk.Frame(self.left_frame, bg=BG_COLOR)
        self.top_controls.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        for i in range(5):
            self.top_controls.grid_columnconfigure(i, weight=1)
        self.theme_label = tk.Label(self.top_controls, text="Select a Theme:", bg=BG_COLOR,
                                    fg=TEXT_FG, font=("Segoe UI", 14, "bold"))
        self.theme_label.grid(row=0, column=0, sticky="w", padx=5)
        self.theme_var = tk.StringVar(self)
        self.theme_var.set(list(THEMES.keys())[0])
        self.theme_menu = ttk.OptionMenu(self.top_controls, self.theme_var, list(THEMES.keys())[0], *THEMES.keys())
        self.theme_menu.grid(row=0, column=1, sticky="ew", padx=5)
        self.start_button = ttk.Button(self.top_controls, text="Start Game", command=self.start_game)
        self.start_button.grid(row=0, column=2, sticky="ew", padx=5)
        # Volume slider.
        self.volume_slider = tk.Scale(self.top_controls, from_=0, to=100, orient=tk.HORIZONTAL,
                                      command=self.update_volume, bg=BG_COLOR, fg=TEXT_FG, font=("Segoe UI", 10))
        self.volume_slider.set(50)
        self.volume_slider.grid(row=0, column=3, sticky="ew", padx=5)
        # Mute/Unmute button.
        self.mute_button = ttk.Button(self.top_controls, text="Mute", command=self.toggle_mute)
        self.mute_button.grid(row=0, column=4, sticky="ew", padx=5)
        
        # Status Display Box.
        self.status_text = tk.Text(self.left_frame, bg="white", fg=TEXT_FG, font=("Segoe UI", 12),
                                    wrap=tk.WORD, height=10)
        self.status_text.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.left_frame.grid_rowconfigure(2, weight=1)
        
        # Guess Input Box.
        self.guess_entry = tk.Entry(self.left_frame, font=("Segoe UI", 12))
        self.guess_entry.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
        self.guess_entry.bind("<Return>", self.process_guess)
        self.guess_entry.focus_set()
        self.submit_button = ttk.Button(self.left_frame, text="Submit Guess", command=self.process_guess)
        self.submit_button.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        
        # Status Text Tags.
        self.status_text.tag_config("header", foreground=HEADER_FG, font=("Segoe UI", 16, "bold"))
        self.status_text.tag_config("guess", foreground=TEXT_FG, font=("Segoe UI", 12))
        self.status_text.tag_config("score", foreground=HEADER_FG, font=("Segoe UI", 12, "italic"))
        self.status_text.tag_config("response", foreground="#E67E22", font=("Segoe UI", 14, "bold"))
        self.status_text.tag_config("vague", foreground="#1ABC9C", font=("Segoe UI", 14, "bold"))
        self.status_text.tag_config("helpful", foreground="#9B59B6", font=("Segoe UI", 14, "bold"))
        self.status_text.tag_config("correct", foreground="#2ECC71", font=("Segoe UI", 18, "bold"))
        self.status_text.tag_config("error", foreground="#E74C3C", font=("Segoe UI", 14, "bold"))
        
        # Right Panel: Cat-themed (Therapod) box with yellow background, with cat ears.
        self.right_frame = tk.Frame(self.main_frame, bg=CAT_BG, width=300, height=220, bd=5, relief="raised")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.right_frame.grid_propagate(False)
        self.cat_canvas = tk.Canvas(self.right_frame, bg=CAT_BG, width=300, height=220, highlightthickness=0)
        self.cat_canvas.pack(fill="both", expand=True)
        # Draw two triangles for cat ears.
        self.cat_canvas.create_polygon(40, 10, 60, 0, 80, 10, fill=CAT_BG, outline="black")
        self.cat_canvas.create_polygon(220, 10, 240, 0, 260, 10, fill=CAT_BG, outline="black")
        # Place the GIF label at the center.
        self.gif_label = tk.Label(self.cat_canvas, bg=CAT_BG)
        self.cat_canvas.create_window(150, 120, window=self.gif_label)
        
        # Bottom Frame: Contains Stopwatch and Leaderboard panels.
        self.bottom_frame = tk.Frame(self, bg=BG_COLOR)
        self.bottom_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        
        # Stopwatch Panel (Left)
        self.stopwatch_frame = tk.Frame(self.bottom_frame, bg=BG_COLOR, bd=2, relief="groove")
        self.stopwatch_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.stopwatch_label = tk.Label(self.stopwatch_frame, text="00:00:00", font=("Courier New", 36, "bold"),
                                        bg="black", fg="red")
        self.stopwatch_label.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Leaderboard Panel (Right)
        self.leaderboard_frame = tk.Frame(self.bottom_frame, bg=BG_COLOR, bd=2, relief="groove")
        self.leaderboard_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.leaderboard_frame.grid_columnconfigure(0, weight=1)
        self.leaderboard_title = tk.Label(self.leaderboard_frame, text="Leaderboard", font=("Segoe UI", 16, "bold"),
                                          bg=BG_COLOR, fg=HEADER_FG)
        self.leaderboard_title.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        # Filter Option for theme.
        self.filter_frame = tk.Frame(self.leaderboard_frame, bg=BG_COLOR)
        self.filter_frame.grid(row=1, column=0, sticky="ew", padx=10)
        self.filter_frame.grid_columnconfigure(0, weight=1)
        self.filter_frame.grid_columnconfigure(1, weight=1)
        self.filter_label = tk.Label(self.filter_frame, text="Filter by Theme:", font=("Segoe UI", 12),
                                     bg=BG_COLOR, fg=TEXT_FG)
        self.filter_label.grid(row=0, column=0, sticky="w", padx=5)
        self.leaderboard_filter_var = tk.StringVar(self)
        self.leaderboard_filter_var.set("All")
        filter_options = ["All"] + list(THEMES.keys())
        self.leaderboard_filter = ttk.OptionMenu(self.filter_frame, self.leaderboard_filter_var, *filter_options, command=lambda _: self.update_leaderboard_display())
        self.leaderboard_filter.grid(row=0, column=1, sticky="ew", padx=5)
        self.leaderboard_text = tk.Text(self.leaderboard_frame, bg="white", fg=TEXT_FG, font=("Segoe UI", 12),
                                        height=10, state="disabled", wrap=tk.WORD)
        self.leaderboard_text.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.leaderboard_frame.grid_rowconfigure(2, weight=1)
        
        self.start_animation("surprise")
        
        # Feedback overlay for game start.
        self.start_feedback = tk.Label(self, text="Game Started! Get Ready to Play!",
                                       font=("Segoe UI", 20, "bold"), fg=HEADER_FG, bg=BG_COLOR)
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
        self.start_animation("surprise")
        self.start_time = time.time()
        self.update_stopwatch()
        self.show_start_feedback()
        
    def process_guess(self, event=None):
        guess = self.guess_entry.get().strip().lower()
        self.guess_entry.delete(0, tk.END)
        if guess == "exit":
            self.status_text.insert(tk.END, f"\n❌ Game over! The secret word was: {self.target_word}\n", "error")
            return
        
        score = similarity_score(guess, self.target_word)
        self.guesses += 1
        
        new_emotion = self.choose_emotion(score)
        if new_emotion != self.current_emotion:
            self.start_animation(new_emotion)
        
        self.status_text.insert(tk.END, f"\n💬 Guess: {guess} | ", "guess")
        self.status_text.insert(tk.END, f"⭐ Similarity Score: {score}%\n", "score")
        
        if score == 100:
            self.status_text.insert(tk.END, f"\n🎉 Correct! The word was '{self.target_word}'. You took {self.guesses} guesses.\n", "correct")
            elapsed = int(time.time() - self.start_time)
            self.status_text.insert(tk.END, f"Time: {elapsed} seconds\n", "header")
            self.update_leaderboard(self.player_name, self.guesses, elapsed)
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
        
    def update_leaderboard_display(self):
        leaderboard = []
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
        self.start_animation("surprise")
        self.start_time = time.time()
        self.update_stopwatch()
        self.show_start_feedback()
        
    def process_guess(self, event=None):
        guess = self.guess_entry.get().strip().lower()
        self.guess_entry.delete(0, tk.END)
        if guess == "exit":
            self.status_text.insert(tk.END, f"\n❌ Game over! The secret word was: {self.target_word}\n", "error")
            return
        
        score = similarity_score(guess, self.target_word)
        self.guesses += 1
        
        new_emotion = self.choose_emotion(score)
        if new_emotion != self.current_emotion:
            self.start_animation(new_emotion)
        
        self.status_text.insert(tk.END, f"\n💬 Guess: {guess} | ", "guess")
        self.status_text.insert(tk.END, f"⭐ Similarity Score: {score}%\n", "score")
        
        if score == 100:
            self.status_text.insert(tk.END, f"\n🎉 Correct! The word was '{self.target_word}'. You took {self.guesses} guesses.\n", "correct")
            elapsed = int(time.time() - self.start_time)
            self.status_text.insert(tk.END, f"Time: {elapsed} seconds\n", "header")
            self.update_leaderboard(self.player_name, self.guesses, elapsed)
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
        
    def update_leaderboard_display(self):
        leaderboard = []
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
        
if __name__ == "__main__":
    app = ReverseAkinatorGUI()
    app.mainloop()
