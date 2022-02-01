n=int(input("Enter the number of terms you want the series for:"))
a=0
b=1
print(a,b,end=" ")

i=1
while(i<=(n-2)):
    r=a+b
    print(r,end=" ")
    a=b
    b=r
    i+=1
    
    
