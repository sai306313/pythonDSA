l=[2,'bb',3,'ddddd']
#with index
for i in range(len(l)):
    print(l[i],end=" ")
print()

#without index
for i in l:
    print(i,end=" ")
print()

#fuctions
l.append(2)
print(l,end=" ")

l2=['sai']
l.extend(l2)
print(l)
