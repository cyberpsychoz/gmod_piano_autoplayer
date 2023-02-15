import mido
from pynput.keyboard import Controller, Key
import time

# Open the MIDI file
midi_file = mido.MidiFile('example.mid')

# Define the keyboard controller
keyboard = Controller()

# Define the mapping of MIDI notes to keyboard keys
# This is just an example, you can customize it as needed
key_map = {
    60: Key.space,    # C4 -> space bar
    62: Key.right,    # D4 -> right arrow key
    64: Key.left,     # E4 -> left arrow key
    65: Key.down,     # F4 -> down arrow key
    67: Key.up,       # G4 -> up arrow key
}

# Loop over each message in the MIDI file
for msg in midi_file.play():
    # If the message is a NoteOn message and the velocity is greater than 0
    if msg.type == 'note_on' and msg.velocity > 0:
        # Check if the note is in the key map
        if msg.note in key_map:
            # Simulate a key press
            keyboard.press(key_map[msg.note])
    # If the message is a NoteOff message or the velocity is 0
    elif msg.type == 'note_off' or msg.velocity == 0:
        # Check if the note is in the key map
        if msg.note in key_map:
            # Simulate a key release
            keyboard.release(key_map[msg.note])
    # Sleep for a short duration to simulate the note duration
    time.sleep(msg.time)
