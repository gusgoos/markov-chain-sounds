import numpy as np
import sounddevice as sd
import keyboard
import time
import threading

# Notas de la escala pentatónica (en C mayor): C, D, E, G, A
notes = ['C', 'D', 'E', 'G', 'A']

frequencies = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'G': 392.00,
    'A': 440.00
}

# Matriz de transición (probabilidades de 0 a 1)
transition_matrix = np.array([
    [0.1, 0.3, 0.3, 0.2, 0.1],  # C
    [0.2, 0.1, 0.3, 0.3, 0.1],  # D
    [0.2, 0.2, 0.1, 0.3, 0.2],  # E
    [0.3, 0.2, 0.2, 0.1, 0.2],  # G
    [0.1, 0.2, 0.3, 0.2, 0.2],  # A
])

def generate_tone(freq, duration=0.4, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * freq * t)
    return tone.astype(np.float32)

def play_note(freq):
    tone = generate_tone(freq)
    sd.play(tone, samplerate=44100)  # ⏱️ No sd.wait() here!

# Iniciar desde una nota aleatoria
current_index = np.random.choice(len(notes))

print("🎹 Presiona cualquier tecla para generar una nueva nota (ESC para salir)")

while True:
    if keyboard.is_pressed('esc'):
        print("Saliendo...")
        break

    if keyboard.read_event().event_type == keyboard.KEY_DOWN:
        current_note = notes[current_index]
        freq = frequencies[current_note]
        print(f"Nota: {current_note} ({freq} Hz)")

        threading.Thread(target=play_note, args=(freq,), daemon=True).start()

        current_index = np.random.choice(
            len(notes), p=transition_matrix[current_index]
        )

        time.sleep(0.03)



# Generar secuencias aleatorias de notas
def generate_note_sequence(start_index, steps=8):
    sequence = [notes[start_index]]
    current_index = start_index

    for _ in range(steps - 1):
        current_index = np.random.choice(
            len(notes), p=transition_matrix[current_index]
        )
        sequence.append(notes[current_index])

    return sequence
print("🎼 Ejemplos de secuencias generadas (modo Markov):")
for i in range(3):
    start = np.random.choice(len(notes))
    seq = generate_note_sequence(start, steps=8)
    print(f"  → {' - '.join(seq)}")
print("\n🎹 Presiona cualquier tecla para generar una nueva nota (ESC para salir)")