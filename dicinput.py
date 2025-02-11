#
keys=[1,2,3,4]
values=['a','b','c','d']
d={}
for i in range(len(keys)):
    d[keys[i]]=values[i]
print(d)

#
n=int(input())
l=[]
for i in range(n):
    k=int(input())
    v=input()
    d[k]=v
print(d)
