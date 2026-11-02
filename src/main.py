"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


PROFILES = {
    "baseline": {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False},
    "conflicting_signals": {"genre": "metal", "mood": "sad", "energy": 0.95, "likes_acoustic": True},
    "diverse_hiphop_anxious": {"genre": "hip-hop", "mood": "anxious", "energy": 0.70, "likes_acoustic": False},
    "diverse_reggae_playful": {"genre": "reggae", "mood": "playful", "energy": 0.60, "likes_acoustic": False},
    "diverse_rnb_romantic": {"genre": "r&b", "mood": "romantic", "energy": 0.52, "likes_acoustic": False},
}


def run_profile(name: str, user_prefs: dict, songs, k: int = 3) -> None:
    print(f"\n{'=' * 40}")
    print(f"Profile: {name} -> {user_prefs}")
    print("=" * 40)
    try:
        recommendations = recommend_songs(user_prefs, songs, k=k)
    except Exception as exc:
        print(f"  ERROR: {type(exc).__name__}: {exc}")
        return

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.split("; "):
            print(f"     - {reason}")


def main() -> None:
    songs = load_songs("data/songs.csv")

    for name, user_prefs in PROFILES.items():
        run_profile(name, user_prefs, songs)
    print()


if __name__ == "__main__":
    main()
