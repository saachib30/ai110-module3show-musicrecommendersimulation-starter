# 🎧 Model Card: Music Recommender Simulation

## Model Name

**VibeFinder 1.0**

---

## Goal / Task

VibeFinder recommends songs that match a user's taste. The user describes what they like, and the model returns a ranked list of songs. It is a content-based recommender. This means it looks at the features of each song, not at what other people listened to. The goal is to learn and explore how recommenders work, not to serve real users.

---

## Data Used

The model uses a CSV dataset with **18 songs**. Each song has these features:

- **genre** — the style of music (pop, lofi, rock, and more)
- **mood** — the feeling of the song (happy, chill, intense)
- **energy** — how energetic the song is, from 0.0 to 1.0
- **tempo_bpm** — the speed of the song in beats per minute
- **valence** — how positive or happy the song sounds, from 0.0 to 1.0
- **danceability** — how easy it is to dance to, from 0.0 to 1.0
- **acousticness** — how acoustic the song is, from 0.0 to 1.0

The dataset is small and was expanded by hand to include more genres and moods. Some parts of musical taste are missing, such as lyrics, language, and artist popularity.

---

## Algorithm Summary

The user gives four preferences: **genre**, **mood**, **energy**, and **likes_acoustic** (true or false). The model scores every song against these preferences, then ranks the songs from highest score to lowest. It returns the top matches.

Each song earns points like this:

- **Genre match: +2.0** — the song's genre equals the user's favorite genre
- **Mood match: +1.5** — the song's mood equals the user's favorite mood
- **Energy closeness: up to +1.5** — the closer the song's energy is to the user's target, the more points it gets
- **Acousticness preference: +1.0** — the song's acoustic level matches what the user likes

The highest possible score is **6.0**. Energy is scored by closeness, not by "higher is better." This way, a user who wants calm music is not pushed toward the loudest songs. Only the four features above are scored. The other features (tempo_bpm, valence, danceability) are stored but not yet used, because the user profile has no preference for them.

---

## Observed Behavior / Biases

- **Filter bubble.** The model rewards songs that match the user's current genre and mood. It keeps suggesting more of the same and rarely introduces new styles.
- **Genre imbalance.** Some genres have several songs and others have only one. Users who like a common genre get better results than users who like a rare one.
- **Filler songs.** A few high-energy, non-acoustic songs appear in almost every list. They score points on energy and acousticness even when the genre and mood do not match.
- **Missing user history.** The model does not use likes, skips, or listening history. It cannot learn or improve from how a person actually behaves.
- **Small dataset.** With only 18 songs, the same tracks repeat across users, and it is hard to judge how good the model really is.

---

## Evaluation Process

To check the model, I tested it with four user profiles and looked at the top recommendations for each:

- **High-Energy Pop** — pop, happy, high energy
- **Chill Lofi** — lofi, chill, low energy, likes acoustic
- **Deep Intense Rock** — rock, intense, high energy
- **Conflicting Sad Energy** — lofi and melancholy, but also high energy (an intentional contradiction)

For each profile, I checked whether the top song was one a real listener would expect, and whether the reasons behind each score made sense.

The three clean profiles worked well. High-Energy Pop put *Sunrise City* first, Chill Lofi put *Library Rain* first, and Deep Intense Rock put *Storm Runner* first. Each top song matched on all four features at once, which is exactly what the scoring should reward. The surprising part was the Conflicting Sad Energy profile. No song in the dataset has a "melancholy" mood, so that preference scored nothing, and the results fell back to genre and energy. This showed how much the model depends on the dataset actually containing songs that fit the user.

---

## Intended Use

- Classroom learning and exploration
- Understanding how content-based recommenders turn data into scores
- Testing how different user profiles change the results
- A simple starting point for building bigger recommenders

---

## Non-Intended Use

- Real music apps or real users
- Any decision that affects a person's money, safety, or rights
- Judging the quality or value of any artist or song
- Situations that need accurate, fair, or large-scale recommendations

---

## Ideas for Improvement

- Add more songs so the dataset is larger and more balanced across genres
- Use the extra features that already exist: tempo_bpm, valence, and danceability
- Add "melancholy" and other missing moods so every profile has real matches
- Give partial credit for similar genres (for example, pop and indie pop)
- Add some variety on purpose so the top list is not always the same songs
- Include user history, such as likes and skips, to learn over time

---

## Personal Reflection

My biggest learning moment was seeing how a few simple point values could turn song data into real recommendations. AI tools helped me a lot along the way. They explained ideas like collaborative and content-based filtering in plain language, helped me design the scoring rule, and helped me write and test the Python functions. But I still had to double-check the AI. For example, when I ran a weight experiment, the AI showed me the results, and I had to look closely to decide whether the recommendations were truly better or just different. In the end I chose to revert that change.

What surprised me most was how well such a simple algorithm worked. With only genre, mood, energy, and acousticness, the model still picked songs that felt right for each user. It also surprised me how easily it fell into a filter bubble and kept suggesting the same kinds of songs. Next I would like to add more songs, use the features I am not scoring yet, and add some user history so the recommender can learn over time.
