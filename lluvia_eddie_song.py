from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def print_lyrics():

    lines = [
        (Fore.LIGHTCYAN_EX, "No me digas nada y márchate", 0.05),
        (Fore.LIGHTCYAN_EX, "No llames amor a tu hipocresía", 0.05),
        (Fore.LIGHTMAGENTA_EX, "No me digas nada, el tonto aquí he sido yo", 0.05),
        (Fore.LIGHTMAGENTA_EX, "Me dañaron, rosa, tus espinas", 0.05),
        
        (Fore.CYAN + Style.BRIGHT, "Lluvia, tus besos fríos como la lluvia", 0.05),
        (Fore.LIGHTCYAN_EX, "Que gota a gota fueron enfriando", 0.05),
        (Fore.CYAN, "Mi alma, mi cuerpo y mi ser", 0.05),
        
        (Fore.MAGENTA + Style.BRIGHT, "Lluvia, tus manos frías como la lluvia", 0.05),
        (Fore.LIGHTMAGENTA_EX, "Que día a día fueron enfriando", 0.05),
        (Fore.LIGHTRED_EX, "Mi ardiente deseo y mi piel", 0.05),
    ]

    delays = [1.5, 1.8, 2.0, 2.2,
              2.5, 2.2, 2.0,
              2.5, 2.2, 2.5]

    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        print('')
        
print_lyrics()
