from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def print_lyrics(): 
    print(Fore.YELLOW + Style.BRIGHT + "\n" + "="*10 + " 🎶 Goodbyes - Post Malone 🎶 " + "="*10 + "\n")
    sleep(0.1)

    lines = [
        (Fore.LIGHTCYAN_EX, "We're both acting insane, but too stubborn to change", 0.04),
        (Fore.LIGHTCYAN_EX, "Now I'm drinkin' again, 80 proof in my veins", 0.04),
        (Fore.LIGHTMAGENTA_EX, "And my fingertips stained, looking over the edge", 0.04),
        (Fore.MAGENTA, "Don't fuck with me tonight", 0.05),
        
        (Fore.LIGHTRED_EX, "Said you needed this heart then you got it", 0.05),
        (Fore.LIGHTRED_EX, "Turns out that it wasn't what you wanted", 0.05),
        (Fore.LIGHTMAGENTA_EX, "And we wouldn't let go and we lost it", 0.05),
        (Fore.RED, "Now I'm a goner", 0.06),
        
        (Fore.LIGHTCYAN_EX, "I want you out of my head", 0.05),
        (Fore.CYAN, "I want you out of my bedroom tonight", 0.06),
        (Fore.LIGHTMAGENTA_EX, "There's no way I could save you", 0.06),
        (Fore.LIGHTRED_EX, "'Cause I need to be saved too", 0.06),
        (Fore.RED + Style.BRIGHT, "I'm no good at goodbyes", 0.05),
    ]

    delays = [1, 1.1, 1.6, 1.6,
              1.1, 1.1, 1.0, 1,
              1.4, 1.3, 1.3, 1.45, 2.0]

    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char, end='', flush=True)
            sleep(char_delay)  
        sleep(delays[i]) 
        print('')  

print_lyrics()
