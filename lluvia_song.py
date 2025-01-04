import tkinter as tk
from time import sleep
from threading import Thread

def display_lyrics():

    lines = [
        ("No me digas nada y márchate", "cyan", 1.5),
        ("No llames amor a tu hipocresía", "light blue", 1.8),
        ("No me digas nada, el tonto aquí he sido yo", "magenta", 2.0),
        ("Me dañaron, rosa, tus espinas", "red", 2.2),
        ("Lluvia, (Lluvia) tus besos fríos como la lluvia (Lluvia)", "yellow", 2.5),
        ("Que gota a gota fueron enfriando (Lluvia)", "light green", 2.2),
        ("Mi alma, mi cuerpo y mi ser", "green", 2.0),
        ("Lluvia, (Lluvia) tus manos frías como la lluvia (Lluvia)", "orange", 2.5),
        ("Que día a día fueron enfriando (Lluvia)", "pink", 2.2),
        ("Mi ardiente deseo y mi piel", "purple", 2.5)
    ]

    for text, color, delay in lines:
        fade_in_text(text, color) 
        sleep(delay) 
    fade_in_text("🎶 Fin de la Canción 🎶", "white") 

def fade_in_text(text, color):
    """Muestra el texto con efecto de desvanecimiento."""
    for alpha in range(0, 11):  
        label.config(text=text, fg=color, font=("Helvetica", 16 + alpha))  
        root.update()  
        sleep(0.1)  

root = tk.Tk()
root.title("Lluvia - Eddie Santiago")
root.geometry("800x300") 
root.configure(bg="black")

label = tk.Label(
    root,
    text="",
    font=("Helvetica", 16),
    bg="black",
    wraplength=700,
    justify="center"
)
label.pack(expand=True)

thread = Thread(target=display_lyrics, daemon=True)
thread.start()

root.mainloop()
