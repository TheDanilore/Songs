from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def print_lyrics():

    lines = [
        (Fore.LIGHTCYAN_EX, "Ni en mis pasos ni en mi tiempo", 0.05),
        (Fore.LIGHTCYAN_EX, "Ni en mi cara ni en mi espejo", 0.07),
        (Fore.LIGHTMAGENTA_EX, "Hay un hueco donde no te asomes tú", 0.05),
        (Fore.LIGHTMAGENTA_EX, "No hay un milímetro de piel donde no estés siempre tú", 0.07),
        
        (Fore.CYAN, "Nadie sabe hacerme frente con un beso diferente", 0.05),
        (Fore.CYAN, "Que despierte mis instintos como tú", 0.05),
        (Fore.LIGHTRED_EX, "Nadie conoce el mecanismo de mi amor", 0.05),
        (Fore.LIGHTRED_EX, "Tan solo tú, solo tú", 0.05),
        
        (Fore.MAGENTA + Style.BRIGHT, "Sin ti no hay nada, si no estás tú", 0.06),
        (Fore.RED + Style.BRIGHT, "Sin ti se apaga el amor", 0.07),
    ]

    delays = [1.2, 1, 4, 7.4,
              3.5, 3.6, 4, 4.6,
              4, 4.5]

    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lyrics()
