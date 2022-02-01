num=int(input("Enter a number"))
new=num
sum=0
while(new>0):
    dig=new%10
    sum+=dig**3
    new=new//10

if sum==num:
    print("Number entered is an Armstrong number")
else:
    print("Number entered is not armstrong number")
    
