from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def print_lyrics(): 
    lines = [
        (Fore.LIGHTCYAN_EX, "Si tú supieras todo lo que yo he hecho solo pa' ver si te olvido, wow, yeah", 0.04),
        (Fore.LIGHTCYAN_EX, "Si tú supieras todas las veces que he querido escribirte y no te escribo", 0.04),
        (Fore.LIGHTMAGENTA_EX, "Todos estos cabrones que te tiran, mami, todos esos son hijos míos", 0.04),
        (Fore.MAGENTA, "Se te olvidó que tú y yo nos dimos un beso después de habernos despedido", 0.04),
        
        (Fore.LIGHTCYAN_EX, "Ya estoy cansado que postees en tus stories corazones partidos", 0.04),
        (Fore.LIGHTCYAN_EX, "Yo sé que estás cansada de escucharme, pero, baby, escucha tus latidos, oh", 0.04),
        (Fore.LIGHTMAGENTA_EX, "Baby, perdón, pero el tiempo que no estoy contigo es tiempo perdido", 0.04),
        (Fore.MAGENTA, "Estoy en Miami, hace calor, bebé, pero mi corazón está frío", 0.04),

        (Fore.LIGHTCYAN_EX, "No sé si vuelva a verte", 0.06),
        (Fore.LIGHTMAGENTA_EX, "Los bandidos no tenemos suerte", 0.06),
        (Fore.LIGHTCYAN_EX, "Estaba esperando esta ocasión", 0.06),
        (Fore.LIGHTCYAN_EX, "Vamo' a perrear bailando reggaetón", 0.06),

        (Fore.LIGHTMAGENTA_EX, "Quédate con mis lentes", 0.05),
        (Fore.LIGHTMAGENTA_EX, "Solamente pa' que me recuerdes", 0.05),
    ]

    delays = [2.3, 2.4, 2.3, 2.5,
              2.6, 2.7, 2.4, 2.1,
              1.1, 1.4, 1.3, 0.8,
              1, 1.6]

    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char, end='', flush=True)
            sleep(char_delay) 
        sleep(delays[i])  
        print('')  

print_lyrics()
