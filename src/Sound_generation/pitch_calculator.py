# Constants
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
MAJOR_SCALE_STEPS = [0, 2, 4, 5, 7, 9, 11, 12]
A4_FREQ = 440
INTERVAL_STEPS = {
    'M3': 4,  # Major third
    'm3': 3,  # Minor third
    'P5': 7,  # Perfect fifth
    'm7': 10, # Minor seventh
    'M7': 11, # Major seventh
    'P4': 5,  # Perfect fourth
    'd5': 6,  # Diminished fifth
    'A5': 8,  # Augmented fifth
}
CHORD_INTERVALS = {
    '7': ['M3', 'P5', 'm7'],
    'M7': ['M3', 'P5', 'M7'],
    'M': ['M3', 'P5'],
    'maj': ['M3', 'P5'],
    'm': ['m3', 'P5'],
    'min': ['m3', 'P5'],
    'M7': ['M3', 'P5', 'M7'],
    'maj7': ['M3', 'P5', 'M7'],
    'm7': ['m3', 'P5', 'm7'],
    'min7': ['m3', 'P5', 'm7'],
    'dim': ['m3', 'd5'],
    'aug': ['M3', 'A5'],
}


def calculate_pitch_note(octave, note_number):
    return A4_FREQ * 2 ** ((octave - 4) + (note_number - 9) / 12)

def note_to_freq(note, octave):
    note_number = NOTES.index(note)
    return calculate_pitch_note(octave, note_number)

def chord_to_notes(chord_root, chord_type):
    if chord_type not in CHORD_INTERVALS:
        raise ValueError(f"Unsupported chord type: {chord_type}")
    intervals = CHORD_INTERVALS[chord_type]
    root_index = NOTES.index(chord_root)
    chord_notes = [NOTES[(root_index + INTERVAL_STEPS[interval]) % 12] for interval in intervals]
    return [chord_root] + chord_notes

def get_chord_frequencies(chord_name, octave):
    if len(chord_name) < 2:
        raise ValueError("Invalid chord name format.")
    chord_root = chord_name[0]
    chord_type = chord_name[1:]
    notes_in_chord = chord_to_notes(chord_root, chord_type)
    frequencies = [note_to_freq(note, octave) for note in notes_in_chord]
    return frequencies

# # Example usage for D7 chord in the 4th octave
# chord_name = "A7"
# octave = 4
# try:
#     frequencies = get_chord_frequencies(chord_name, octave)
#     print(f"Pitches in the {chord_name} chord on octave {octave}:")
#     for freq in frequencies:
#         print(f"{freq:.2f} Hz")
# except ValueError as e:
#     print(e)