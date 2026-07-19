# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users 

This recommender has several limitations because it uses a small song catalog and a simple weighted scoring system. It may create a filter bubble by repeatedly recommending songs that match the user's favorite genre and mood instead of introducing variety. The system can also over-prioritize certain features, such as genre or energy, depending on the weights, which may cause good songs from other genres to rank lower. Since the recommender does not use listening history, skips, lyrics, or collaborative filtering, it cannot understand deeper user taste or long-term behavior. The dataset size also limits fairness because genres or moods with fewer songs have fewer chances to appear in the top recommendations.

---

## 7. Evaluation  

To check whether the recommender behaved as expected, I tested it with four user profiles and looked at the top recommendations for each: **High-Energy Pop** (pop, happy, high energy), **Chill Lofi** (lofi, chill, low energy, likes acoustic), **Deep Intense Rock** (rock, intense, high energy), and **Conflicting Sad Energy** (a lofi/melancholy user who also wants high energy — an intentional contradiction). For each profile I checked whether the #1 song was one a real listener would actually expect, and whether the reasons behind each score made sense.

**What made sense:** the three "clean" profiles all returned an obvious best match with a near-perfect score. High-Energy Pop put *Sunrise City* first, Chill Lofi put *Library Rain* first, and Deep Intense Rock put *Storm Runner* first. In each case the top song matched on all four features at once (genre, mood, energy, and acousticness), which is exactly what I hoped the scoring would reward.

**What was surprising:** a few high-energy, non-acoustic songs (like *Crystal Cascade* and *Gym Hero*) showed up in almost every profile's top five, acting like "filler." The Conflicting Sad Energy profile was the most revealing — because no song in the catalog has a "melancholy" mood, that preference scored nothing, and the results fell back to whatever matched the genre or energy. This showed how much the recommender depends on the dataset actually containing songs that fit the user.

**Comparing the profiles:**

- **Pop vs Lofi:** near-opposites, and the system handled them well — Pop favored bright, high-energy, non-acoustic songs, while Lofi favored calm, low-energy, acoustic ones. Almost no overlap in the top picks.
- **Pop vs Rock:** both want high energy and non-acoustic songs, so they *shared filler tracks* (like *Gym Hero* and *Crystal Cascade*), but genre and mood still pushed the correct #1 to the top of each list.
- **Lofi vs Rock:** the clearest contrast of all — low vs high energy, acoustic vs non-acoustic — so they had essentially no songs in common. This is the recommender at its best.
- **Pop vs Conflicting Sad Energy:** Pop produced a confident, well-matched list, while the Conflicting profile produced weak, low scores and no strong #1, because its own preferences fought each other and the dataset had no melancholy songs to satisfy it.

**Why "Gym Hero" can appear for Happy Pop users:** *Gym Hero* is a pop song with very high energy and low acousticness. For a Happy Pop user it earns the genre points (it's pop), most of the energy-closeness points (its energy is near the user's target), and the non-acoustic points — so even though its mood is "intense" rather than "happy," it still scores high enough to land in the top five. It's a good example of how matching several features partly can add up, even when one feature (mood) doesn't match.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
