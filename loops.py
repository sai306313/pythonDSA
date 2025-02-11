#with while
n = int (input())
count = 0
if(n<0):
    n = n*-1
count = 0
while(n>0):
    n=n//10
    count+=1
print(count)


#without while
n=input()
if n[0]=='-':
    print(len(n)-1)
else:
    print(len(n))


#prime numbers
n = int(input())
flag=True
x=0
for i in range(2,int(n**0.5)+1):
    x +=1
    if (n%i==0):
        break
    flag = False
if flag:
    print("prime",x)
else:
    print("not prime",x)
