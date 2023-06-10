import tkinter as tk
from PIL import Image, ImageTk

def buttonKlick():
    print("Button was klicked!")

okno = tk.Tk()
okno.title("Komunikat")

photo = Image.open("C:/laboratoriumy Git Bash/taptap.jpg")
photo = photo.resize((300, 300))
zdjecie = ImageTk.PhotoImage(photo)

etykietaPhoto = tk.Label(okno, image=zdjecie)
etykietaPhoto.pack()

button = tk.Button(okno, text="Klick this button!", command=buttonKlick)
button.pack()

okno.mainloop()