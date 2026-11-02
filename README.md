# 🎵 Music Recommender Simulation

## Project Summary

This version represents each song as a dictionary of attributes (genre, mood, energy, tempo, valence, danceability, acousticness) loaded from a CSV catalog of 18 songs, and a user's taste as a simple preference dictionary (favorite genre, favorite mood, target energy, and whether they like acoustic sound). 

`score_song` turns a user profile and a song into a weighted score: exact genre and mood matches each contribute the most points, how close the song's energy is to the user's target energy contributes a smaller tiebreaking bonus, and a match on acoustic preference adds a small bonus on top. 

`recommend_songs` scores every song in the catalog, sorts by score, and returns the top three along with a plain-language explanation of exactly which preferences the song matched.

---

## How The System Works

= Real-world recommendation suggests your potential next favorite song by scoring and computing your listening habits (genres, artists, replays, skips, etc) to compare it against other songs with similar characteristics. Futhermore, the system will also analyze your habits against other users that also favored songs that you like.  

From these observations, while the database includes feature: genre, mood, energy, tempo, valence (how upbeat/cheerful is this song), danceability and acousticness, the system will be focusing on `genre, mood, energy` to find the user's next potential favorite song. 

The `UserProfile` will store what the listener want and their listening habit: favorite_genre, mood, and target energy. 

The `Recommender` will match each feature against the information in `UserProfile`, 1 if it's a match, 0 if it doesn't, then muliply by a weight to reflect how important each metric is. Mood and genre weights the most, with energy as tie breaker and acoustic match to reflect production style of the songe. 

The song that scores the highest by the `Recommender` will be the recommendation. 

Some potential bias includes:
- This system reflect the designer's assumption about what matters the most for music taste, in this case is genre and mood, which can deny people that want to expand their music profile rather the same narrow lane. 
- The song catalog right now is still quite small and doesn't have a high diversity of genre. Some less common genre might only have one song, thus every run of the recommender that weight heavily on genre will probably keep recommending the same song. 
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

```
Top Recommendations
========================================

1. Sunrise City by Neon Echo
   Score: 5.48
   Reasons:
     - Matches your favorite genre (pop)
     - Matches your favorite mood (happy)
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

2. Rooftop Lights by Indigo Parade
   Score: 3.46
   Reasons:
     - Matches your favorite mood (happy)
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

3. Gym Hero by Max Pulse
   Score: 3.37
   Reasons:
     - Matches your favorite genre (pop)
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

The experiment I tried was commented out the mood metric in my scoring system. What I found out was since the genre weigh just as high, there was really no major change in the top 3 ranking. However, the scoring itself for each song is drastically lower.
---

## Limitations and Risks

The system relies on exact match.
The system will always return the same 3 songs unless there are drastic change to user's profile.

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building this project showed me that a recommender doesn't need anything fancy to "turn data into predictions" — at its core, `score_song` just represents both the song and the user as a handful of labeled attributes, checks which ones line up, and adds up weighted points for each match. The prediction is really just arithmetic: whichever song accumulates the most points under rules I chose (genre and mood matter most, energy is a tiebreaker, acoustic preference is a small bonus) gets recommended. What I didn't expect going in is how much the *weights themselves* are a design choice disguised as a technical detail — deciding genre and mood are worth 2.0 points each while energy and acoustic are worth less isn't neutral, it's an assumption about what "music taste" means, baked directly into the math.

That's also where I think bias shows up most clearly. Because genre and mood are checked with exact string equality, the system can't recognize that "pop" and "indie pop," or "happy" and "euphoric," are related — it either hits an exact label or gets nothing, which rewards people whose taste happens to line up neatly with the catalog's existing labels and ignores everyone else. And because several genres and moods exist on only one song in my 18-song catalog, the recommender ends up returning the same few songs over and over for anyone outside the most common tastes, with no mechanism to explore or diversify. Real-world recommenders have the same risk at a much bigger scale — if the system (or its training data) assumes certain preferences matter most, or if the catalog underrepresents certain genres or artists, it will keep steering every user back toward the same narrow set of "safe" matches instead of genuinely reflecting what they'd actually enjoy.

## PHASE 4: Step 1
========================================
Profile: baseline -> {'genre': 'pop', 'mood': 'happy', 'energy': 0.8, 'likes_acoustic': False}
========================================

1. Sunrise City by Neon Echo
   Score: 5.48
   Reasons:
     - Matches your favorite genre (pop)
     - Matches your favorite mood (happy)
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

2. Rooftop Lights by Indigo Parade
   Score: 3.46
   Reasons:
     - Matches your favorite mood (happy)
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

3. Gym Hero by Max Pulse
   Score: 3.37
   Reasons:
     - Matches your favorite genre (pop)
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

========================================
Profile: conflicting_signals -> {'genre': 'metal', 'mood': 'sad', 'energy': 0.95, 'likes_acoustic': True}
========================================

1. Crownless King by Atlas Forge
   Score: 3.00
   Reasons:
     - Matches your favorite genre (metal)
     - Energy level is close to what you're looking for

2. Golden Hour Memories by Sable & Wren
   Score: 1.00
   Reasons:
     - Has an acoustic sound you tend to enjoy

3. Gym Hero by Max Pulse
   Score: 0.98
   Reasons:
     - Energy level is close to what you're looking for

========================================
Profile: diverse_hiphop_anxious -> {'genre': 'hip-hop', 'mood': 'anxious', 'energy': 0.7, 'likes_acoustic': False}
========================================

1. Low Static Nights by Vesper Row
   Score: 5.50
   Reasons:
     - Matches your favorite genre (hip-hop)
     - Matches your favorite mood (anxious)
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

2. Night Drive Loop by Neon Echo
   Score: 1.45
   Reasons:
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

3. Rooftop Lights by Indigo Parade
   Score: 1.44
   Reasons:
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

========================================
Profile: diverse_reggae_playful -> {'genre': 'reggae', 'mood': 'playful', 'energy': 0.6, 'likes_acoustic': False}
========================================

1. Island Afterglow by Tidewater Collective
   Score: 5.50
   Reasons:
     - Matches your favorite genre (reggae)
     - Matches your favorite mood (playful)
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

2. Velvet Static by Juno Reyes
   Score: 1.42
   Reasons:
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

3. Low Static Nights by Vesper Row
   Score: 1.40
   Reasons:
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

========================================
Profile: diverse_rnb_romantic -> {'genre': 'r&b', 'mood': 'romantic', 'energy': 0.52, 'likes_acoustic': False}
========================================

1. Velvet Static by Juno Reyes
   Score: 5.50
   Reasons:
     - Matches your favorite genre (r&b)
     - Matches your favorite mood (romantic)
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

2. Island Afterglow by Tidewater Collective
   Score: 1.42
   Reasons:
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste

3. Low Static Nights by Vesper Row
   Score: 1.32
   Reasons:
     - Energy level is close to what you're looking for
     - Has a produced, non-acoustic sound matching your taste