import os
import random
import time
import ctypes
import threading
from time import sleep
import colorama
import winsound

# Installazione automatica di colorama
os.system("pip install colorama")
colorama.init()

# Struttura POINT per rappresentare le coordinate (x, y)
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

# Funzione per ottenere la posizione corrente del mouse
def get_mouse_position():
    point = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    return point.x, point.y

# Funzione per muovere il mouse
def set_mouse_position(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

# Loop principale per muovere il mouse casualmente
def move_mouse_randomly():
    while True:
        # Ottieni la posizione corrente
        current_x, current_y = get_mouse_position()

        # Calcola un nuovo offset casuale
        x_offset = random.randint(-593, 300)
        y_offset = random.randint(-600, 200)

        # Calcola la nuova posizione
        new_x = current_x + x_offset
        new_y = current_y + y_offset

        # Muove il mouse alla nuova posizione
        set_mouse_position(new_x, new_y)

        # Delay prima del prossimo movimento
        time.sleep(0.5)

# Loop principale per stampare il messaggio colorato
def print_colored_message():
    while True:
        color = random.choice([colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW])
        print(color + "SHTUPIDU SHTUPIDU SHTUPIDU!")
        # Riproduce un bip predefinito
        winsound.Beep(3000, 200)  # Frequenza: 1000 Hz, Durata: 500 ms
        sleep(0.06)

if __name__ == "__main__":
    # Crea i thread per eseguire entrambi i loop contemporaneamente
    thread1 = threading.Thread(target=move_mouse_randomly)
    thread2 = threading.Thread(target=print_colored_message)

    # Avvia i thread
    thread1.start()
    thread2.start()

    # Aspetta che entrambi i thread completino (non succederà mai)
    thread1.join()
    thread2.join()
