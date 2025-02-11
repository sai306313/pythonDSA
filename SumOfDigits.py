n=int(input())
s=0
while(n>0):
    rem=n%10
    s+=rem
    n=n//10
print(s)    
