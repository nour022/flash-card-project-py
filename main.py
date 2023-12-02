import pandas
import random
from tkinter import *

# ---------------------------functions------------------------#
data = pandas.read_csv("data/languge.csv")
sd = data.to_dict(orient="records")


def tranlater(words):
	canvas.itemconfig(cart_img, image=card_back)
	canvas.itemconfig(de, text=words["Deutsch"], fill="white")
	canvas.itemconfig(ar, text=words["Arabic"], fill="white")
	canvas.itemconfig(en, text=words["English"], fill="white")


def radom_word():
	words = random.choice(sd)
	# print(words)
	canvas.itemconfig(cart_img, image=card_front)
	canvas.itemconfig(ar, text="")
	canvas.itemconfig(de, text="English", fill="black")
	canvas.itemconfig(en, text=words["English"], fill="black")
	win = window.after(4000, tranlater, words)


# ----------------------------GUI-----------------------------#
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
# window.minsize(900, 700)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=626, bg=BACKGROUND_COLOR, highlightthickness=0)
cart_img = canvas.create_image(400, 300, image=card_front)

de = canvas.create_text(400, 170, text="Title", font=("Ariel", 40, "italic"))
ar = canvas.create_text(400, 390, text="", font=("Ariel", 40, "italic"))
en = canvas.create_text(400, 280, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
right_btn = Button(image=right, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=radom_word)
right_btn.grid(row=1, column=1)
wrong_btn = Button(image=wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=radom_word)
wrong_btn.grid(row=1, column=0)
window.mainloop()
