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

## Sample Recommendation Output

Default user profile:

```python
user_prefs = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.8,
    "likes_acoustic": False
}
```

Terminal output:

```text
Loaded songs: 18

Top recommendations:

Sunrise City - Score: 5.97
Because: genre match (+2.0); mood match (+1.5); energy closeness (+1.5); non-acoustic preference (+1.0)

Gym Hero - Score: 4.30
Because: genre match (+2.0); energy closeness (+1.3); non-acoustic preference (+1.0)

Rooftop Lights - Score: 3.94
Because: mood match (+1.5); energy closeness (+1.4); non-acoustic preference (+1.0)

Night Drive Loop - Score: 2.42
Because: energy closeness (+1.4); non-acoustic preference (+1.0)

Crystal Cascade - Score: 2.38
Because: energy closeness (+1.4); non-acoustic preference (+1.0)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

<img width="946" height="837" alt="image" src="https://github.com/user-attachments/assets/a35b2fc0-6bd8-46bb-9484-c0fd85fb7e57" />


---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

I tested the recommender with several different user profiles to see whether the scoring logic behaved as expected.

Loaded songs: 18
============================================================
Profile: High-Energy Pop
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.85, 'likes_acoustic': False}
------------------------------------------------------------
Top 5 recommendations:

1. Sunrise City - Neon Echo
   Score: 5.96
   Reasons: genre match (+2.0); mood match (+1.5); energy closeness (+1.5); non-acoustic preference (+1.0)

2. Gym Hero - Max Pulse
   Score: 4.38
   Reasons: genre match (+2.0); energy closeness (+1.4); non-acoustic preference (+1.0)

3. Rooftop Lights - Indigo Parade
   Score: 3.87
   Reasons: mood match (+1.5); energy closeness (+1.4); non-acoustic preference (+1.0)

4. Crystal Cascade - Aurora Field
   Score: 2.46
   Reasons: energy closeness (+1.5); non-acoustic preference (+1.0)

5. Storm Runner - Voltline
   Score: 2.41
   Reasons: energy closeness (+1.4); non-acoustic preference (+1.0)

============================================================
Profile: Chill Lofi
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35, 'likes_acoustic': True}
------------------------------------------------------------
Top 5 recommendations:

1. Library Rain - Paper Lanterns
   Score: 6.00
   Reasons: genre match (+2.0); mood match (+1.5); energy closeness (+1.5); acoustic preference (+1.0)

2. Midnight Coding - LoRoom
   Score: 5.89
   Reasons: genre match (+2.0); mood match (+1.5); energy closeness (+1.4); acoustic preference (+1.0)

3. Focus Flow - LoRoom
   Score: 4.42
   Reasons: genre match (+2.0); energy closeness (+1.4); acoustic preference (+1.0)

4. Spacewalk Thoughts - Orbit Bloom
   Score: 3.90
   Reasons: mood match (+1.5); energy closeness (+1.4); acoustic preference (+1.0)

5. Coffee Shop Stories - Slow Stereo
   Score: 2.47
   Reasons: energy closeness (+1.5); acoustic preference (+1.0)

============================================================
Profile: Deep Intense Rock
Preferences: {'genre': 'rock', 'mood': 'intense', 'energy': 0.9, 'likes_acoustic': False}
------------------------------------------------------------
Top 5 recommendations:

1. Storm Runner - Voltline
   Score: 5.98
   Reasons: genre match (+2.0); mood match (+1.5); energy closeness (+1.5); non-acoustic preference (+1.0)

2. Gym Hero - Max Pulse
   Score: 3.96
   Reasons: mood match (+1.5); energy closeness (+1.5); non-acoustic preference (+1.0)

3. Temple of Bass - Grimewave
   Score: 3.90
   Reasons: mood match (+1.5); energy closeness (+1.4); non-acoustic preference (+1.0)

4. Crystal Cascade - Aurora Field
   Score: 2.47
   Reasons: energy closeness (+1.5); non-acoustic preference (+1.0)

5. Basement Riot - Static Teeth
   Score: 2.42
   Reasons: energy closeness (+1.4); non-acoustic preference (+1.0)

============================================================
Profile: Conflicting Sad Energy
Preferences: {'genre': 'lofi', 'mood': 'melancholy', 'energy': 0.9, 'likes_acoustic': False}
------------------------------------------------------------
Top 5 recommendations:

1. Midnight Coding - LoRoom
   Score: 2.78
   Reasons: genre match (+2.0); energy closeness (+0.8)

2. Focus Flow - LoRoom
   Score: 2.75
   Reasons: genre match (+2.0); energy closeness (+0.8)

3. Library Rain - Paper Lanterns
   Score: 2.67
   Reasons: genre match (+2.0); energy closeness (+0.7)

4. Storm Runner - Voltline
   Score: 2.48
   Reasons: energy closeness (+1.5); non-acoustic preference (+1.0)

5. Crystal Cascade - Aurora Field
   Score: 2.47
   Reasons: energy closeness (+1.5); non-acoustic preference (+1.0)


### Accuracy and surprises

To evaluate the recommender, I ran it against several user profiles and reviewed the top results. **Many results made sense** — for example, the "Chill Lofi" profile (lofi, chill, low energy, likes acoustic) returned *Library Rain* as the #1 pick with a near-perfect score, matching on genre, mood, energy, and acousticness all at once. **One surprise/weakness** was that a few high-energy, non-acoustic songs (like *Crystal Cascade*) showed up across almost every profile, because they score points on energy and acousticness even when the genre and mood don't match — so they act like "filler" in the rankings. Overall the **weights feel mostly balanced**: genre (+2.0) and mood (+1.5) correctly dominate for clean matches, though genre can feel slightly too strong in edge cases, where an on-genre song outranks one that fits the mood and energy better. Finally, a key **limitation is the small dataset** — with only 18 songs, the same handful of tracks repeat across profiles and it's hard to judge the recommender's quality. A larger, more varied song list would give more meaningful and diverse recommendations.


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



