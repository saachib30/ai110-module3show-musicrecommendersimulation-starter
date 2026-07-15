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

Real-world recommendation systems use data about users and content to predict what someone might enjoy next. Platforms like Spotify, YouTube, and TikTok often use a mix of collaborative filtering and content-based filtering. Collaborative filtering looks at patterns from similar users, such as likes, skips, playlists, or watch history. Content-based filtering looks at the item itself, such as a song’s genre, mood, tempo, energy, or acousticness.

My project focuses on a simpler content-based recommender. Each song is represented with attributes, and each user is represented with a taste profile. The recommender compares the song data to the user profile, calculates a weighted score, and then ranks the songs from strongest match to weakest match.

### Features Used

Each `Song` uses these features:

- `id`
- `title`
- `artist`
- `genre`
- `mood`
- `energy`
- `tempo_bpm`
- `valence`
- `danceability`
- `acousticness`

Each `UserProfile` stores these preferences:

- `favorite_genre`
- `favorite_mood`
- `target_energy`
- `likes_acoustic`

### Algorithm Recipe

The recommender uses a 100-point scoring system:

- Genre match: 35 points
- Mood match: 30 points
- Energy closeness: 20 points
- Acousticness preference: 15 points

Genre and mood are weighted most heavily because they strongly define the overall type and feeling of a song. Energy is scored by closeness to the user’s target energy, because a higher energy value is not always better. For example, a user who likes calm music should not automatically receive high-energy songs. Acousticness is included because some users may prefer more acoustic, natural-sounding music while others may prefer less acoustic or more produced music.

### Scoring Rule vs. Ranking Rule

A scoring rule calculates how well one song matches one user profile. For example, one song may receive points for matching the user’s favorite genre, matching the user’s favorite mood, having energy close to the user’s target energy, and matching the user’s acoustic preference.

A ranking rule happens after all songs have been scored. The recommender sorts the songs from highest score to lowest score and returns the top results. This means the scoring rule decides the quality of one match, while the ranking rule decides the final order of recommendations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

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



