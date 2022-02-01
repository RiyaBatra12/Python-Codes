import random
import time 
movies=["ANTIM","SHERSHAAH","BODYGAURD"]
m=random.randint(0,2)
movie=movies[m]
guess=[' ']
h="HANGMAN"
while True:
    print("="*50)
    print("\t",h)
    print('='*50)
    dash=False
    for ch in movie:
        if ch in guess:
            print(ch,end=' ')
        else:
            print("_",end=" ")
            dash=True
    if dash==False:
        print("YOU WIN!!!!!")
        break
    print()
    print("="*50)
    g=input("Enter the Guess Alphabet")
    if len(g) !=1:
        print("Please enter single alphabet only")
        continue
    if not g.isalpha():
        print("No symbol,digit or space is allowed")
        continue
    g=g.upper()
    if g not in movie:
        h=h[:len(h)-1]
        if len(h)==0:
            print("YOU LOOSE, GAME OVER!!!!")
            break
    guess.append(g)
    time.sleep(2)
                
            
