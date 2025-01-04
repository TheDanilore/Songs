from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def print_lyrics():
    lines = [
        (Fore.LIGHTCYAN_EX, "Staring at two different views on your window ledge", 0.07),
        (Fore.CYAN, "Coffee is going cold, it's like time froze", 0.08),
        (Fore.LIGHTMAGENTA_EX, "There you go wishing, floating down our wishing well", 0.06),
        (Fore.MAGENTA, "It's like I'm always causing problems, causing hell", 0.06),
        (Fore.YELLOW, "I didn't mean to put you through this, I can tell", 0.06),
        (Fore.LIGHTYELLOW_EX, "We're gonna sweep this under the carpet", 0.06),
        
        (Fore.LIGHTGREEN_EX, "I hope that I can turn back the time", 0.07),
        (Fore.LIGHTCYAN_EX, "To make it all alright, all alright for us", 0.08),
        (Fore.LIGHTBLUE_EX, "I'll promise to build a new world", 0.08),
        (Fore.CYAN, "For us two", 0.09),
        (Fore.LIGHTMAGENTA_EX, "With you in the middle", 0.1)
    ]

    delays = [5.57, 6, 1.3, 1.4, 1.8, 2.6, 
              0.7, 1.25, 1.1, 1.8, 1.5]

    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lyrics()
