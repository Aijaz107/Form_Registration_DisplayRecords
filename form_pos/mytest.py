l=[(1,2,3),(4,5,6)]
nl=[]
for i in range(len(l)):
    tl=[]
    for j in l[i]:
        if j==l[i][0]:
            pass
        else:
            tl.append(j)
    tl=tuple(tl)
    nl.append(tl)
print(nl)