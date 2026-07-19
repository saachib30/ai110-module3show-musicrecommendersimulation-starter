# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This version of the Music Recommender Simulation uses a simple content-based recommendation system. Instead of using data from millions of users, it compares each song’s attributes to a user’s taste profile. The recommender looks at features such as genre, mood, energy, and acousticness, then gives each song a score based on how closely it matches the user. The highest-scoring songs are returned as personalized recommendations.

---

## How The System Works

How The System Works

Real-world recommendation systems use data about users and content to predict what someone might enjoy next. Platforms like Spotify, YouTube, and TikTok often use a mix of collaborative filtering and content-based filtering. Collaborative filtering looks at patterns from similar users, such as likes, skips, playlists, or watch history. Content-based filtering looks at the item itself, such as a song’s genre, mood, tempo, energy, or acousticness.

My project focuses on a simpler content-based recommender. Each song is represented with attributes, and each user is represented with a taste profile. The recommender compares the song data to the user profile, calculates a weighted score, and then ranks the songs from strongest match to weakest match.

Features Used

Each Song uses these features:

id
title
artist
genre
mood
energy
tempo_bpm
valence
danceability
acousticness

Each UserProfile stores these preferences:

favorite_genre
favorite_mood
target_energy
likes_acoustic
Phase 2 Design Plan

The recommender will use the song catalog in data/songs.csv. Each song includes features such as genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. I expanded the dataset with additional songs so the recommender has a wider range of genres and moods to compare.

The main user profile for testing will be:

user_prefs = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.8,
    "likes_acoustic": False
}

This profile represents a user who likes upbeat, happy pop music and does not strongly prefer acoustic songs.

Final Algorithm Recipe

The recommender will score each song using this weighted system:

Genre match: +2.0
Mood match: +1.5
Energy closeness: up to +1.5
Acousticness preference: +1.0

The maximum possible score is 6.0.

Energy will be scored by closeness instead of simply rewarding higher energy:

energy_score = max(0, 1 - abs(song_energy - target_energy)) * 1.5

This matters because a user who prefers medium or calm music should not automatically receive the highest-energy songs. The best match is the song closest to the user’s target energy. I lowered the energy weight to 1.5 so that energy helps fine-tune recommendations without becoming as important as genre.

Data Flow
User Preferences
        ↓
Load songs from songs.csv
        ↓
Score each song one by one
        ↓
Sort songs from highest score to lowest score
        ↓
Return top K recommendations
Expected Biases

This recommender may over-prioritize genre, which means it could ignore strong matches from other genres. For example, a happy, high-energy dance song might be ranked lower than a pop song simply because the user’s favorite genre is pop. It may also create a filter bubble by repeatedly recommending songs that are very similar to the user’s existing preferences.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



