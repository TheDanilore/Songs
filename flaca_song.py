from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def print_lyrics(): 
    lines = [
        (Fore.LIGHTCYAN_EX, "Aunque casi me equivoco", 0.06),
        (Fore.LIGHTCYAN_EX, "Y te digo poco a poco", 0.08),
        (Fore.LIGHTMAGENTA_EX, "No me mientas", 0.06),
        (Fore.LIGHTMAGENTA_EX, "No me digas la verdad", 0.06),
        (Fore.LIGHTRED_EX, "No te quedes callada", 0.07),
        (Fore.LIGHTRED_EX, "No levantes la voz", 0.08),
        (Fore.LIGHTMAGENTA_EX, "Ni me pidas perdón", 0.08),
        
        (Fore.LIGHTCYAN_EX, "Aunque casi te confieso", 0.06),
        (Fore.LIGHTCYAN_EX, "Que también he sido un perro compañero", 0.06),
        (Fore.LIGHTGREEN_EX, "Un perro ideal que aprendió a nadar", 0.07),
        (Fore.LIGHTGREEN_EX, "Y a volver al hogar", 0.07),
        (Fore.CYAN, "Para poder comer", 0.08),
        
        (Fore.MAGENTA, "Flaca", 0.05),
        (Fore.MAGENTA, "No me claves", 0.05),
        (Fore.MAGENTA, "Tus puñales", 0.05),
        (Fore.LIGHTMAGENTA_EX, "Por la espalda", 0.05),
        (Fore.LIGHTMAGENTA_EX, "Tan profundo", 0.05),
        (Fore.LIGHTRED_EX, "No me duelen", 0.08),
        (Fore.LIGHTRED_EX, "No me hacen mal", 0.08),
        
        (Fore.LIGHTBLUE_EX, "Lejos", 0.06),
        (Fore.LIGHTBLUE_EX, "En el centro", 0.06),
        (Fore.LIGHTCYAN_EX, "De la tierra", 0.06),
        (Fore.CYAN, "Las raíces", 0.07),
        (Fore.CYAN, "Del amor", 0.07),
        (Fore.LIGHTGREEN_EX, "Donde estaban", 0.08),
        (Fore.LIGHTGREEN_EX, "Quedarán", 0.08) 
    ]

    delays = [0.4, 0.4, 0.6, 0.9, 0.6, 0.7, 4.1,
              0.7, 1.3, 1.5, 1.2, 4.4,
              1.2, 1.5, 1.5, 1.8, 1.2, 0.9, 4.3,
              1.2, 1.4, 1.6, 1.2, 1.8, 1.5, 3.5]

    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        print('') 

print_lyrics()
