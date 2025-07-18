## PeterAlert20
## Este programa muestra una ventana con una animación GIF de Peter Griffin bailando y reproduce la canción "Surfin Bird" de The Trashmen en bucle.
## Utiliza las siguientes librerías:
## - tkinter: para la interfaz gráfica.
## - PIL (Pillow): para manejar y animar el GIF.
## - pygame: para reproducir el archivo MP3.
## - os: para manejar rutas de archivos de forma portable.
##
## Asegúrate de tener los siguientes archivos en la misma carpeta que este script:
## - peter1.ico: icono de la ventana.
## - SurfinBird.mp3: archivo de audio que se reproducirá.
## - peter.gif: archivo GIF animado de Peter Griffin.
##
## Este proyecto está inspirado en un meme que vi en internet,
## basado en el famoso episodio de la serie Family Guy donde Peter Griffin baila
## la canción "Surfin Bird" de The Trashmen.


import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os

pygame.mixer.init()

print(""" Hey Lois, im an python script!
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⠿⠿⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣟⢋⡝⠻⠷⢄⣀⡔⢻⠛⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣎⠑⠋⠙⠛⢹⠀⠃⠀⣸⠀⠗⠞⠢⡼⠋⠉⢕⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⠎⠀⠀⠀⠀⢀⡁⠒⠊⠁⢠⣤⣤⣴⠃⠀⠀⠀⢆⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠷⠀⠀⠀⠀⠀⠈⠈⠑⠂⠤⠤⠥⠤⠤⣿⡀⠀⠀⠸⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⡆⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⢥⡀⠀⠀⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⣹⠀⠀⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢯⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣤⣴⠞⢶⣀⠶⠏⠀⠀⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠳⡀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⡜⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠔⠊⠁⠀⠀⠀⠙⢄⠈⠳⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠀⡞⠈⠑⠢⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⢄⠀⠉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡜⠀⠀⠀⠀⠀⠑⢤⣀⠀⠀⠀
⠀⠀⠀⣴⣁⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⡀⠀⠈⠓⠢⢄⣀⠀⠀⠀⢀⣔⠉⠀⢀⡮⠂⠡⡇⠀⠀⠀⠀⠀⢹⠱⡀⠀
⠀⡔⣉⠀⠀⠀⠀⠈⠉⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠤⡀⠀⠀⠀⢨⠗⣆⡜⠀⠑⠴⠋⠀⠀⠀⢡⠀⠀⠀⠀⠀⡸⠘⠈⡆
⢠⠋⣠⡤⠒⠒⢒⡒⠠⢄⠀⠈⢦⠀⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⠞⠰⠎⢧⠀⠀⠀⠀⠀⠀⠀⢂⢳⡀⠀⢀⡔⠁⠀⡰⠁
⠰⣾⠁⠀⠀⠀⠀⠈⢆⠈⠑⡄⢄⢣⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⢆⠳⣒⣡⣀⡤⠊⢰⠀
⠀⢣⡄⠀⠀⠀⠀⠀⠈⠆⠀⠚⡌⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠹⡉⠀⠀⠀⡘⠀
⠀⠘⡥⠀⠀⠀⠀⠀⠀⠘⡀⠈⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⢠⠃⠀
""")

root = tk.Tk()
root.title("Peter Alert!")
root.geometry("260x180")
root.resizable(False, False) 

icon_path = os.path.join(os.path.dirname(__file__), "peter1.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

mp3_path = os.path.join(os.path.dirname(__file__), "SurfinBird.mp3")
gif_path = os.path.join(os.path.dirname(__file__), "peter.gif")

pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play(-1)  

gif = Image.open(gif_path)
frames = []
try:
    while True:
        frame = ImageTk.PhotoImage(gif.copy().resize((150, 150)))
        frames.append(frame)
        gif.seek(len(frames))
except EOFError:
    pass

label = tk.Label(root)
label.pack()


def update(ind):
    frame = frames[ind]
    label.configure(image=frame)
    root.after(33, update, (ind+1) % len(frames))  
update(0)


def close_app():
    pygame.mixer.music.stop()
    root.destroy()

button = tk.Button(root, text="OK", command=close_app)
button.pack()

root.mainloop()
