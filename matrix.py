#!/usr/bin/env python3

l=[[1,2,3],[4,5,6],[7,8,9]]
s=''
for i in range(len(l)):
    diag=l[i][i]
    s+=str(diag)
print("main diagonal is:",s)
for i in range(len(l)):
    k=0
    su=0
    while k<len(l[i]):
        su+=l[i][k]
        k+=1
    print(su,end=',')
    print
    pu=1
    for k in range(len(l[i])):
        pu*=l[i][k]
    print(pu,end=',')
