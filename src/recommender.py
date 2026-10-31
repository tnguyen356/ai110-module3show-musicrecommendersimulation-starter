import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads songs from a CSV file into a list of dicts with numeric fields as floats."""
    numeric_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for field in numeric_fields:
                row[field] = float(row[field])
            row["id"] = int(row["id"])
            songs.append(row)
    return songs

GENRE_WEIGHT = 2.0
MOOD_WEIGHT = 2.0
ENERGY_WEIGHT = 1.0
ACOUSTIC_WEIGHT = 0.5

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a song against user preferences and returns the score with matching reasons."""
    score = 0.0
    reasons = []

    if user_prefs.get("genre") == song.get("genre"):
        score += GENRE_WEIGHT
        reasons.append(f"Matches your favorite genre ({song.get('genre')})")

    if user_prefs.get("mood") == song.get("mood"):
        score += MOOD_WEIGHT
        reasons.append(f"Matches your favorite mood ({song.get('mood')})")

    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        energy_closeness = 1 - abs(song.get("energy", 0.0) - target_energy)
        score += energy_closeness * ENERGY_WEIGHT
        if energy_closeness >= 0.8:
            reasons.append("Energy level is close to what you're looking for")

    likes_acoustic = user_prefs.get("likes_acoustic", False)
    acousticness = song.get("acousticness", 0.0)
    if likes_acoustic and acousticness >= 0.5:
        score += ACOUSTIC_WEIGHT
        reasons.append("Has an acoustic sound you tend to enjoy")
    elif not likes_acoustic and acousticness < 0.5:
        score += ACOUSTIC_WEIGHT
        reasons.append("Has a produced, non-acoustic sound matching your taste")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song against user preferences and returns the top k, highest score first."""
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    scored.sort(key=lambda item: item[1], reverse=True)
    return [
        (song, score, "; ".join(reasons) if reasons else "No strong matches found")
        for song, score, reasons in scored[:k]
    ]
