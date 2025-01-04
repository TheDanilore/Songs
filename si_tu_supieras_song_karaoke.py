import time
from colorama import Fore, Style, init
import speech_recognition as sr

# Inicializar colorama
init(autoreset=True)

# Inicializar el reconocimiento de voz
recognizer = sr.Recognizer()

# Letra de la canción (fragmento)
lyrics = [
    ("Si tú supieras", Fore.LIGHTCYAN_EX),
    ("que aún dentro de mi alma", Fore.CYAN),
    ("conservo aquel cariño", Fore.LIGHTMAGENTA_EX),
    ("que tuve para ti", Fore.MAGENTA),
    ("Quién sabe si supieras", Fore.LIGHTYELLOW_EX),
    ("que nunca te he olvidado", Fore.YELLOW),
    ("volviendo a tu pasado", Fore.LIGHTGREEN_EX),
    ("te acordarás de mí", Fore.LIGHTBLUE_EX)
]

def recognize_and_match():
    # Mostrar instrucción inicial
    print(Fore.LIGHTYELLOW_EX + "🎤 Canta la canción y verás cómo las letras aparecen...")

    for line, color in lyrics:
        with sr.Microphone() as source:
            try:
                # Escuchar la entrada de voz
                print(Fore.LIGHTCYAN_EX + f"🎶 Diga: \"{line}\"")
                audio = recognizer.listen(source, timeout=5)
                
                # Reconocer el texto
                text = recognizer.recognize_google(audio, language="es-ES")
                if line.lower() in text.lower():
                    print(color + line)  # Mostrar la línea en el color asignado
                else:
                    print(Fore.RED + "❌ No coincide. Inténtalo de nuevo.")

            except sr.UnknownValueError:
                print(Fore.RED + "❌ No entendí lo que dijiste. Por favor, repítelo.")
            except sr.RequestError:
                print(Fore.RED + "⚠️ Error al conectar con el servicio de reconocimiento de voz.")

# Ejecutar la función
recognize_and_match()
