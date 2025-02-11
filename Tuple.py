"""t=()
print(t)

t=(1,2,3,4,5)
print(t)

#tuple directory
print (dir(t))

#input
t=tuple(map(int,input().split()))
print(t)"""

#slicing [start:end:step]
t=(1,2,3,4,5,6,7,8,9,10)
print(t)
print(t[2:8])
print(t[2:8:3])

#step is -ve reverse
print(t[::-1])
print(t[2:8:-1])
print(t[8:2:-2])
print(t[5:1:-3])

t=(2,6,7,8,9,1)
print(sorted(t))
