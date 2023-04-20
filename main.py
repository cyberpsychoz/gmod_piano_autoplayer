import midi
import time
import os
import sys

from pathlib import Path

keys = {
    0: "z",
    1: "s",
    2: "x",
    3: "d",
    4: "c",
    5: "v",
    6: "g",
    7: "b",
    8: "h",
    9: "n",
    10: "j",
    11: "m",
    12: ",",
    13: "l",
    14: ".",
    15: ";",
    16: "/",
}


def play_key(key):
    if key in keys:
        os.system(
            f"xdotool keydown --window $(xdotool search --name \"Garry's Mod\") {keys[key]}"
        )
        time.sleep(0.01)
        os.system(
            f"xdotool keyup --window $(xdotool search --name \"Garry's Mod\") {keys[key]}"
        )


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <midi file>")
        sys.exit(1)

    midi_file = sys.argv[1]

    if not Path(midi_file).exists():
        print(f"File not found: {midi_file}")
        sys.exit(1)

    pattern = midi.read_midifile(midi_file)
    pattern.make_ticks_abs()

    last_tick = None
    for track in pattern:
        for event in track:
            if isinstance(event, midi.NoteOnEvent):
                if last_tick is None:
                    last_tick = event.tick
                else:
                    delta = event.tick - last_tick
                    if delta > 0:
                        time.sleep(delta / 1000.0)
                    last_tick = event.tick
                play_key(event.data[0] % len(keys))


if __name__ == "__main__":
   main()
