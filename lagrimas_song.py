from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def print_lyrics(): 
    lines = [
        (Fore.LIGHTCYAN_EX, "Después de tanto amor, tú te vas y me abandonas", 0.06),
        (Fore.LIGHTCYAN_EX, "Ya no puedo seguir así, buscaré a otra", 0.08),
        (Fore.LIGHTMAGENTA_EX, "Hoy tú te ríes, pero mañana llorarás", 0.06),
        (Fore.LIGHTMAGENTA_EX, "Porque el amor que yo a ti te daba, tú vas a ver que no es fácil de encontrar", 0.05),
        
        (Fore.LIGHTCYAN_EX, "Después de tanto amor, tú te vas y me abandonas", 0.06),
        (Fore.LIGHTCYAN_EX, "Ya no puedo seguir así, buscaré a otra", 0.06),
        (Fore.LIGHTGREEN_EX, "Y algún día voy a encontrarte, y ojalá que me pidas perdón", 0.04),
        (Fore.LIGHTGREEN_EX, "Te diré: \"mamita, olvídalo, tú fuiste la que fallaste\"", 0.05),
        
        (Fore.LIGHTCYAN_EX, "Después de tanto amor, tú te vas y me abandonas", 0.06),
        (Fore.LIGHTCYAN_EX, "Ya no puedo seguir así, buscaré a otra", 0.06)
    ]

    delays = [1.7, 2.2, 2.4, 1.0,
              1.8, 2.3, 2.3, 2.2,
              2.2, 2.6]

    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        print('') 

print_lyrics()
