import mido
from pynput.keyboard import Controller, Key
import time

# OОткрывает MIDI файл
midi_file = mido.MidiFile('example.mid')

# Определияет контроллер клавиатуры
keyboard = Controller()

# Определяет отображение MIDI-нот на клавиши клавиатуры
key_map = {
    60: Key.space,    # C4 -> пробел
    62: Key.right,    # D4 -> вправо
    64: Key.left,     # E4 -> влево
    65: Key.down,     # F4 -> вниз
    67: Key.up,       # G4 -> вверх
}

# Повторяет цикл над каждым сообщением в MIDI-файле
for msg in midi_file.play():
    # Если сообщение является примечанием к сообщению и скорость больше 0
    if msg.type == 'note_on' and msg.velocity > 0:
        # Проверка заметки на карте ключей
        if msg.note in key_map:
            # Симуляция нажатий клавиши
            keyboard.press(key_map[msg.note])
    # Если сообщение является сообщением об отключении записи или скорость равна 0
    elif msg.type == 'note_off' or msg.velocity == 0:
        # Проверка заметки на карте ключей
        if msg.note in key_map:
            # Симуляция отпускания клавиши (типо уже нажата)
            keyboard.release(key_map[msg.note])
    # Задержка
    time.sleep(msg.time)
