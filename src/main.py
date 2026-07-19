"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

The functions live in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# Profiles used to stress-test the recommender: some clean matches,
# plus a conflicting one where the mood and target energy disagree.
PROFILES = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.85, "likes_acoustic": False},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35, "likes_acoustic": True},
    "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.90, "likes_acoustic": False},
    # Conflict: "melancholy" is a calm/low-energy mood, but the target energy is high.
    "Conflicting Sad Energy": {"genre": "lofi", "mood": "melancholy", "energy": 0.90, "likes_acoustic": False},
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    for name, user_prefs in PROFILES.items():
        print("=" * 60)
        print(f"Profile: {name}")
        print(f"Preferences: {user_prefs}")
        print("-" * 60)

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("Top 5 recommendations:\n")
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} - {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Reasons: {explanation}")
            print()


if __name__ == "__main__":
    main()
