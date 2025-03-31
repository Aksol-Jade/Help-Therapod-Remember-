# game_logic.py
import random
import nltk
from fuzzywuzzy import fuzz
from nltk.corpus import wordnet
from clue_data import CLUES, THEMES  # Ensure your clue_data.py file defines CLUES and THEMES

# Ensure required NLTK resources are available
nltk.download("wordnet", quiet=True)

def get_synonyms(word):
    """Find synonyms of a word using WordNet."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower().replace("_", " "))
    return synonyms

def semantic_similarity(guess, target):
    """Return the maximum path similarity between any noun synsets of guess and target."""
    syns_guess = wordnet.synsets(guess, pos=wordnet.NOUN)
    syns_target = wordnet.synsets(target, pos=wordnet.NOUN)
    max_sim = 0
    for s1 in syns_guess:
        for s2 in syns_target:
            sim = s1.path_similarity(s2)
            if sim is not None and sim > max_sim:
                max_sim = sim
    return max_sim  # value between 0 and 1

def similarity_score(guess, target):
    """
    Calculate a similarity score incorporating:
      - Levenshtein-based fuzzy matching,
      - Jaccard similarity over character sets,
      - A synonym bonus,
      - Semantic similarity (from WordNet).
    The final score is capped at 100.
    """
    levenshtein_score = fuzz.ratio(guess, target)  # 0-100
    guess_set = set(guess)
    target_set = set(target)
    jaccard_score = (len(guess_set & target_set) / len(guess_set | target_set)) * 100
    synonym_bonus = 10 if guess in get_synonyms(target) else 0
    semantic_sim = semantic_similarity(guess, target)  # value between 0 and 1
    # Scale semantic similarity to a bonus; adjust factor as needed.
    semantic_bonus = semantic_sim * 150
    raw_score = (levenshtein_score * 0.4) + (jaccard_score * 0.2) + synonym_bonus + semantic_bonus
    return round(min(100, raw_score), 2)

def get_vague_clue(word):
    """Return a random vague clue for the word."""
    clues = CLUES.get(word, {}).get("vague", ["Think of something related to the theme."])
    return random.choice(clues)

def get_helpful_clue(word):
    """Return a random helpful clue for the word."""
    clues = CLUES.get(word, {}).get("helpful", ["No specific clue available."])
    return random.choice(clues)

def get_response_from_score(guess, score):
    """Generate a textual response based on the similarity score."""
    if score < 10:
        return f"🚫 Not even remotely close. {guess} is way off."
    elif score < 30:
        return f"❌ You're thinking in the wrong direction with {guess}."
    elif score < 50:
        return f"😕 You're starting to get warmer with {guess}, but still far."
    elif score < 70:
        return f"🙂 That's a bit closer. {guess} shares some similarities."
    elif score < 85:
        return f"👍 You're narrowing it down! {guess} has a connection."
    elif score < 95:
        return f"👏 You're very close! {guess} is related, but not the answer."
    else:
        return f"🔥 Almost there! {guess} is practically touching the answer."
