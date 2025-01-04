from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def print_lyrics():
    lines = [
        (Fore.LIGHTMAGENTA_EX, "You can't fight it, you can't breathe", 0.06),
        (Fore.YELLOW, "You say something so loving, but", 0.07),
        (Fore.LIGHTYELLOW_EX, "Now I gotta let you go", 0.08),
        (Fore.LIGHTGREEN_EX, "You'll be better off in someone new", 0.065),
        (Fore.LIGHTGREEN_EX, "I don't wanna be alone", 0.07),
        (Fore.LIGHTCYAN_EX, "You know it hurts me too", 0.11),
        (Fore.CYAN, "You look so broken when you cry", 0.07),
        (Fore.LIGHTCYAN_EX, "One more and then I say goodbye", 0.07),
        (Fore.LIGHTBLUE_EX, "Sometimes, all I think about is you", 0.07),
        (Fore.BLUE, "Late nights in the middle of June", 0.07),
        (Fore.LIGHTYELLOW_EX, "Heat waves been faking me out", 0.07),
        (Fore.LIGHTRED_EX, "Can't make you happier now", 0.07)
    ]

    delays = [0.4, 0.73, 1.5, 0.8, 0.8, 0.9,
              0.5, 0.6, 0.7, 0.7, 0.7, 0.8]

    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lyrics()
