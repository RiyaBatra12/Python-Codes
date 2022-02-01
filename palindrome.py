n=input("Enter a string:\t")
l=len(n)-1
s=""
while l>=0:
    s=s+n[l]
    l-=1
if n==s:
    print("It is a palindrome")
else:
    print("it is not a palindrome")
    
    
    
    
    
