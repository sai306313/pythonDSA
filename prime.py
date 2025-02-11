#prime numbers
n = int(input())
flag=True
x=0
for i in range(2,int(n**0.5)+1):
    x +=1
    if (n%i==0):
        flag = False
        break
if flag:
    print("prime",x)
else:
    print("not prime",x)
