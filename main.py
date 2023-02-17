import mido
from pynput.keyboard import Controller, Key
import time

# Открывает MIDI файл
midi_file = mido.MidiFile('example.mid')

# Определяет контроллер клавиатуры
keyboard = Controller()

# Определяет отображение MIDI-нот на клавиши клавиатуры
key_map = {
    'C4': 1,
    'C#4':1,
    'D4': 2,
    'D#4': 2,
    'E4': 3,
    'F4': 4,
    'F#4': 4,
    'G4': 5,
    'G#4': 5,
    'A4': 6,
    'A#4': 6,
    'B4': 7,
    'C5': 8,
}

# Повторяет цикл над каждым сообщением в MIDI-файле
for msg in midi_file.play():
    # Если сообщение является примечанием к сообщению и скорость больше 0
    if msg.type == 'note_on' and msg.note in key_map and msg.velocity > 0:
        # Определение имени ноты и клавиши
        note_name = mido.midi2str(msg.note)
        key = key_map[msg.note]
        print('key_map')
        # Если нота является знаком #, удерживаем клавишу Shift
        if '#' in note_name:
            keyboard.press(Key.shift)
        # Симуляция нажатий клавиши
        keyboard.press(key)
    # Если сообщение является сообщением об отключении записи или скорость равна 0
    elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
        # Проверка заметки на карте ключей
        if msg.note in key_map:
            # Определение имени ноты и клавиши
            note_name = mido.midi2str(msg.note)
            key = key_map[msg.note]
            # Если нота является знаком #, отпустите клавишу Shift
            if '#' in note_name:
                keyboard.release(Key.shift)
            # Симуляция отпускания клавиши (типо уже нажата)
            keyboard.release(key)
    # Задержка
    time.sleep(msg.time)
