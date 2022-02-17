import random
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase

t=Tk()
t.geometry("800x700")

movies=["ANTIM","SHERSHAAH","BODYGAURD","GEHRAIYAAN","CHHAPAAK","SOORYAVANSHI","BHUJ","KAAGAZ","CHHALAANG","LAXMII","TANHAJI"]

photos = [PhotoImage(file="hang0.png"), PhotoImage(file="hang1.png"), PhotoImage(file="hang2.png"),
PhotoImage(file="hang3.png"), PhotoImage(file="hang4.png"), PhotoImage(file="hang5.png"),
PhotoImage(file="hang6.png"), PhotoImage(file="hang7.png"), PhotoImage(file="hang8.png"),
PhotoImage(file="hang9.png"), PhotoImage(file="hang10.png"), PhotoImage(file="hang11.png")]

def game():
    global moviewithspaces
    global guesses
    guesses=0

    movie=random.choice(movies)
    moviewithspaces = " ".join(movie)
    lblmovie.set(' '.join("_"*len(movie)))

def guess(letter):
	global guesses
	if guesses<11:	
		txt = list(moviewithspaces)
		guessed = list(lblmovie.get())
		if moviewithspaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblmovie.set("".join(guessed))
				if lblmovie.get()==moviewithspaces:
					messagebox.showinfo("Hangman","You guessed it!")
		else:
			guesses += 1
			imgLabel.config(image=photos[guesses])
			if guesses==11:
					messagebox.showwarning("Hangman","Game Over")


imgLabel=Label(t)
imgLabel.place(x=100,y=100)


lblmovie = StringVar()
Label(t, textvariable=lblmovie,font=('consolas 40 bold')).place(x=100,y=300)
    




l1=Label(t,text="HANGMAN GAME",font=("comic sans ms",50,"bold"))
l1.place(x=100,y=0)


b27=Button(t,text="PLAY AGAIN",command=lambda:game(),font=("comic sns ms",20,"bold"))
b27.place(x=290,y=600)




n=0
for c in ascii_uppercase:
    if n<=10:
        Button(t, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4).place(x=100+(n*60),y=400)
    elif n<=21:
        Button(t, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4).place(x=100+(n-11)*60,y=460)
    else:
        Button(t, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4).place(x=100+(n-19)*60,y=520)
    n+=1
game()
t.mainloop()

                
            
