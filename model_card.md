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

Think of it like a matchmaker that gives every song a "compatibility score" with you, then hands you the songs that scored highest.

For each song, it looks at: the genre, the mood, how energetic it is, and how acoustic (stripped-down/unplugged) it sounds.

For you, it asks: what's your favorite genre, your favorite mood, how much energy you want right now, and whether you tend to like acoustic-sounding music or more produced/electronic music.

To turn that into a score, it checks each song one feature at a time and adds points when there's a match:

- If the song's genre is your favorite genre, it adds a decent chunk of points.
- If the song's mood matches your favorite mood, it adds the same decent chunk of points. Genre and mood matter the most, so they're worth the most points.
- It compares the song's energy to the energy level you asked for — the closer they are, the more (smaller) bonus points it adds. This acts more like a tiebreaker between songs that already matched on genre and mood.
- It gives a small bonus if the song's "acoustic-ness" lines up with whether you said you like acoustic music or not.

All those points get added up into one final score per song, the songs get sorted from highest score to lowest, and you're shown the top few. Alongside each recommendation, it also lists the specific reasons it scored the song that way (e.g. "matches your favorite genre"), so the recommendation isn't a black box.

Compared to the starter version (which just printed a placeholder and returned the first few songs untouched), this is the first version that actually reads real data, computes a real score per song based on your taste, ranks songs by that score, and explains itself in plain language instead of a hardcoded "Explanation placeholder".

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

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

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
