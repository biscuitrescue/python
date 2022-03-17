#!/usr/bin/env python3

### NESTED LIST

nest=[]
for i in range(3):
    nestx=eval(input("Please input list "+str(i+1)+": "))
    nest.append(nestx)

print(nest)

n=int(input("Enter no of sublists: "))
w=int(input("Enter no of elements on sublists: "))

L1=[]

for i in range(n):
    L2=[]
    print("Input for sublist", (i+1))
    for k in range(w):
        x=int(input("Please input element: "))
        L2.append(x)
    L1.append(L2)
print(L1)

intp=int(input("Please enter number of elements"))

l1=[]
l2=[]
for i in range(intp):
    x=int(input("please enter element"))
    l1.append(x)
for k in range(len(l1)):
    if l1[k]%2==0:
        l2.append(l1[k])
print(l2)
x=[0,1,4,2]
h=x[2]
g=1
for i in range(1,h+1):
    g*=i
print(g)

x=[1,4,5,2]
z=0
for i in range(len(x)):
    z+=x[i]
print(z)



l=eval(input("Please enter list: "))
# for i in range(len(l)-1):
l[::2],l[1::2]=l[1::2],l[::2]
print(l)

l=[1,2,3,4,5,6,7,8]
x=int((len(l)/2))
l1=l[:x]
l2=l[x:]
print(l2+l1)
