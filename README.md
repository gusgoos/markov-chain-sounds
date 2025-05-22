# markov-chain-sounds

# 🎶 Markov Melody Generator

This project is a simple Python-based melody generator that uses a **Markov Chain** to simulate musical note transitions within the **C major pentatonic scale**. Notes are played in real-time when a key is pressed, and transitions follow a probabilistic model.

## 🧠 How It Works

- A Markov chain models the transition probabilities between notes: C, D, E, G, A.
- Each time a key is pressed, a new note is selected based on the current note's transition probabilities.
- A short tone is played for the selected note using the `sounddevice` library.
- Initial example sequences are printed to demonstrate the generative logic.
