# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Museek 1.0**

## 2. Intended Use  

The recommender gives the user three songs that match user's profiling of genre, mood, energy and ascoustic preference. The assumption this recommender makes about the user is that the user cares mainly about genre and mood, with minor attention toward energy level and ascoustic preference. This project is simply for classroom exploration, and is yet to be refined to reflect real users.

## 3. How the Model Works  

For each song, the model looks at: the genre, the mood, how energetic it is, and how acoustic (stripped-down/unplugged) it sounds.

For you, the model considers what's your favorite genre, your favorite mood, how much energy you want right now, and whether you tend to like acoustic-sounding music or more produced/electronic music.

To turn that into a score, it checks each song one feature at a time and adds points when there's a match:

- If the song's genre is your favorite genre, it adds a decent chunk of points.
- If the song's mood matches your favorite mood, it adds the same decent chunk of points. Genre and mood matter the most, so they're worth the most points.
- It compares the song's energy to the energy level you asked for — the closer they are, the more (smaller) bonus points it adds. This acts more like a tiebreaker between songs that already matched on genre and mood.
- It gives a small bonus if the song's "acoustic-ness" lines up with whether you said you like acoustic music or not.

All those points get added up into one final score per song, the songs get sorted from highest score to lowest, and you're shown the top few. Alongside each recommendation, it also lists the specific reasons it scored the song that way (e.g. "matches your favorite genre"), so the recommendation isn't a black box.

Compared to the starter logic, artist was removed as a preference due to a small number of songs in the database. If more titles are updated to the model, artist can be introduced as a key feature. 

---

## 4. Data  

There are 18 songs in the catalog (8 were added to the initial 10). 
The moods include happy, chill, intense, relaxed, moody, focused, nostalgic, triumphant, euphoric, melancholic, playful, romantic, anxious, dreamy. 
The genres represented: pop, lofi, rock, ambient, jazz, synthwave, indie pop, folk, metal, electronic, blues, reggae, r&b, hip-hop, classical.
Unfortunately, there is no punk, funk, country, Latin, or K-pop music yet.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

The system relies on exact match, where genre == genre which would only reward point for pop == pop instead of relative similarity like pop and indie pop. Also where mood == mood which doesn't consider "playful" or "euphoric" when comparing to "happy" even though they are talking about the same kind of feeling. Consequently, the system will always return the same 3 songs unless the user updates their own profile, therefore no diversity or exploration. 

## 7. Evaluation  

I have 5 different profiles for 5 different genres. For each profile, there are always top 3 recommendation based on the score. Since my system weight genre and mood highest, I do expect the very top 1 of each profile to be distinct, and also score way higher than the other two songs. Running the metal profile is also a way for me to check for mixed signal. While the number one song does match the genre with high similarity in energy level, the score is still lower than other profile that matches in genre, mood, energy level and ascoustic. Yet, the one metal song in the list is still ranked the highest because the score weigh heavily on genre. 

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
