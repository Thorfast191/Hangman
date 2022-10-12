from string import ascii_uppercase
from tkinter import *
from tkinter import messagebox
import guess as guess
import random

window = Tk()
window.title("Hangman")

word = ["hitman","witcher","halo","Uncharted","transformers"]


photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
          PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
          PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
          PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"),
          PhotoImage(file="images/hang11.png")]


def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0

    the_word = random.choice(word)
    the_word_withSpaces = " ".join(the_word)
    lblword.set(' '.join("_" * len(the_word)))


def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 11:
        txt = list(the_word_withSpaces)
        guessed = list(lblword.get())
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lblword.set("".join(guessed))
                if lblword.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You guessed it!")
        else:
            numberOfGuesses += 1
            imageLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman", "Game Over")


imageLabel = Label(window)
imageLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imageLabel.config(image=photos[0])

lblword = StringVar()
Label(window, textvariable=lblword, font=("Serif")).grid(row=0, column=0, padx=10, columnspan=6)

n = 0
for i in ascii_uppercase:
    Button(window, text=i, command=lambda i=i: guess(i), font=("Futura"), width=5).grid(row=1 + n // 9, column=n % 9, )
    n += 1

newGame()
window.mainloop()
