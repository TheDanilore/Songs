from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

print(Fore.RED + "Este texto debe aparecer en rojo")
print(Fore.GREEN + "Este texto debe aparecer en verde")
print(Fore.BLUE + "Este texto debe aparecer en azul")
print(Style.BRIGHT + Fore.YELLOW + "Este texto es amarillo brillante")
