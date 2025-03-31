import random
import nltk
from fuzzywuzzy import fuzz
from nltk.corpus import wordnet
from clue_data import CLUES, THEMES  # Importing clues from a separate file

# Ensure NLTK resources are available
nltk.download("wordnet")

# Themes and word lists


# Generic vague responses
VAGUE_RESPONSES = [
    "Not even close! {guess} is way off.",  # 0: Furthest
    "You're thinking in the wrong direction with {guess}.", #1
    "You're starting to get warmer with {guess}, but still far.", #2
    "That's a bit closer. {guess} shares some similarities.",#3
    "You're narrowing it down! {guess} has a connection.", #4
    "You're very close! {guess} is related, but not the answer.", #5
    "Almost there! {guess} is practically touching the answer.", #6
]

def get_synonyms(word):
    """Find synonyms of a word using WordNet."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower().replace("_", " "))
    return synonyms

def get_response_from_score(guess, score):
    """
    Generates a response based on the user's guess and a score indicating closeness.

    Args:
        guess: The user's guess (string).
        score: A score (0-100) representing how close the guess is to the answer.
    Returns:
        A response string formatted with the guess.
    """

    if score < 10:
        response = f"Not even remotely close. {guess} is way off."
    elif score < 30:
        response = f"You're thinking in the wrong direction with {guess}."
    elif score < 50:
        response = f"You're starting to get warmer with {guess}, but still far."
    elif score < 70:
        response = f"That's a bit closer. {guess} shares some similarities."
    elif score < 85:
        response = f"You're narrowing it down! {guess} has a connection."
    elif score < 95:
        response = f"You're very close! {guess} is related, but not the answer."
    else:
        response = f"Almost there! {guess} is practically touching the answer."
    return response

def get_vague_clue(word):
    """Return a random vague clue for the word."""
    clues = CLUES.get(word, {}).get("vague", ["Think of something related to the theme."])
    return random.choice(clues)

def get_helpful_clue(word):
    """Return a random helpful clue for the word."""
    clues = CLUES.get(word, {}).get("helpful", ["No specific clue available."])
    return random.choice(clues)

def similarity_score(guess, target):
    """Calculate similarity score using Levenshtein and Jaccard similarity."""
    levenshtein_score = fuzz.ratio(guess, target)
    guess_set = set(guess)
    target_set = set(target)
    jaccard_score = len(guess_set & target_set) / len(guess_set | target_set) * 100
    synonym_bonus = 10 if guess in get_synonyms(target) else 0
    return round((levenshtein_score * 0.6) + (jaccard_score * 0.3) + synonym_bonus, 2)

def play_game():
    """Main game function with clues and responses."""
    print("🔎 Welcome to Reverse Akinator!")
    
    while True:
        print("Select a theme:", ", ".join(THEMES.keys()))
        theme = input("Enter a theme: ").strip().lower()
        
        if theme not in THEMES:
            print("Invalid theme. Try again...")
            continue

        target_word = random.choice(THEMES[theme])
        print(f"\n🎭 You will guess a word related to '{theme}'. Try to find the secret word!")
        guesses = 0
        best_guess = ("", 0)
        
        while True:
            guess = input("\nEnter your guess (or type 'exit' to quit): ").strip().lower()
            if guess == "exit":
                print(f"\n❌ You gave up! The secret word was: {target_word}")
                break
            
            score = similarity_score(guess, target_word)
            guesses += 1

            print(f"⚡ Similarity Score: {score}%")
            
            if score == 100:
                print(f"🎉 Correct! The word was '{target_word}'. You took {guesses} guesses.")
                break
            
            if score > best_guess[1]:
                best_guess = (guess, score)
            #give vague response everytime
            print(get_response_from_score(guess,score))
            # Vague clue every 3 guesses
            if guesses % 3 == 0:
                print("\n🌟 Helpful Clue:", get_vague_clue(target_word))
            # Helpful clue every 5 guesses
            if guesses % 5 == 0:
                print("\n🌟 Helpful Clue:", get_helpful_clue(target_word))

        print(f"\n🏆 Best Guess: {best_guess[0]} ({best_guess[1]}%)")

# Run the game
play_game()
