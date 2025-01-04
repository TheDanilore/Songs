from time import sleep
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def print_lyrics():
    print(Fore.YELLOW + Style.BRIGHT + "\n" + "="*10 + " 🎶 Me Olvidé de los 2 - Rels B 🎶 " + "="*10 + "\n")
    sleep(1)

    # Lista de líneas con colores y retardos por carácter
    lines = [
        (Fore.LIGHTCYAN_EX, "Ahora somos tres en esta habitación", 0.05),
        (Fore.CYAN, "Yo me olvidé de los dos", 0.05),
        (Fore.LIGHTMAGENTA_EX, "No pregunté ni quién sos", 0.05),
        (Fore.MAGENTA, "Ni siquiera cómo te llamas", 0.05),
        
        (Fore.LIGHTRED_EX, "Teníamos un pacto, no te puedo llamar", 0.06),
        (Fore.RED, "Tú no me puedes amar, no lo podemos negar", 0.06),
        (Fore.LIGHTMAGENTA_EX, "Dijiste que te olvidé y no lo puedo intentar", 0.06),
        (Fore.LIGHTCYAN_EX, "Y ahora, baby, míranos", 0.06),
    ]

    # Tiempos ajustados entre líneas
    delays = [1.5, 1.8, 2.0, 2.0,
              2.2, 2.4, 2.5, 2.0]

    # Mostrar las líneas con efecto visual
    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char, end='', flush=True)
            sleep(char_delay)  # Retardo entre caracteres
        sleep(delays[i])  # Retardo entre líneas
        print('')  # Salto de línea

    # Mensaje de cierre
    print(Fore.YELLOW + Style.BRIGHT + "\n" + "="*10 + " 🎶 End of Song 🎶 " + "="*10 + "\n")
    sleep(1)

print_lyrics()
