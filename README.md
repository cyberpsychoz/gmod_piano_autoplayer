# Garrys'mod Playable piano script Beta 0.2
A script that turns notes from a midi file into keystrokes on the keyboard.

This code reads the MIDI file named 'example.mid', defines a mapping of MIDI notes to keyboard keys, and simulates keystrokes on the keyboard based on the notes in the MIDI file. NoteOn messages trigger a key press, while NoteOff messages or notes with a velocity of 0 trigger a key release. The code also includes a short delay to simulate the duration of each note.
