def comp_choosing():
    import random as R
    a=R.randint(1,3)
    if a==1:
        a="R"
    elif a==2:
        a="P"
    else:
        a="S"

    return a

def game():
    z=comp_choosing()
    n=input("Enter your choice(R for Rock, P for Paper and S for Scissor:\t")
    n=n.upper()
    print("Computer's choice is:\t",z)
    print("Your choice is:\t",n)
    if z==n:
        print("This round is a draw")
        return 0
    elif z=="R":
        if n=="P":
            print("You won this round")
            return +1
        else:
            print("You lost this round")
            return -1
    elif z=="P":
        if n=="S":
            print("You won this round")
            return +1
        else:
            print("You lost this round")
            return -1
    else:
        if n=="R":
            print("You won this round")
            return 1
        else:
            print("You lost this round")
            return -1

print("In this game R means Rock,P means Paper and S means Scissor\t")
score=0
score+=game()
m=1
while m!=0:
    choice=input("Do you want to play again?(type yes or no):\t")
    if choice=="yes":
        score+=game()
        print("Your score is:\t",score)

    else:
        print("Your final score is:\t",score)
        m=0
        if score==0:
            print("It is a Draw")
        elif score>0:
            print("You won")
        else:
            print("You lost")
            
            
        
        
        
