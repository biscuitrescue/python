print("Please enter your marks(student 1): ")
print("")

a=int(input("Physics: "))
b=int(input("Chemistry: "))
c=int(input("Maths: "))
d=int(input("Computer Science: "))
e=int(input("English: "))

avg1=(a+b+c+d+e)/5

print("")
print("Please enter your marks (student 2): ")
print("")

p=int(input("Physics: "))
q=int(input("Chemistry: "))
r=int(input("Maths: "))
s=int(input("Computer Science: "))
t=int(input("English: "))

avg2=(p+q+r+s+t)/5

print("")
print("Please enter your marks (student 3): ")
print("")

v=int(input("Physics: "))
w=int(input("Chemistry: "))
x=int(input("Maths: "))
y=int(input("Computer Science: "))
z=int(input("English: "))

avg3=(v+w+x+y+z)/5

print("")
print("Please enter your marks (student 4): ")
print("")

f=int(input("Physics: "))
g=int(input("Chemistry: "))
h=int(input("Maths: "))
i=int(input("Computer Science: "))
j=int(input("English: "))

avg4=(f+g+h+i+j)/5

print("")
print("Please enter your marks (student 5): ")
print("")

k=int(input("Physics: "))
l=int(input("Chemistry: "))
m=int(input("Maths: "))
n=int(input("Computer Science: "))
o=int(input("English: "))

avg5=(k+l+m+n+o)/5

print("")
print("Average of student 1 is",avg1)
print("Average of student 2 is",avg2)
print("Average of student 3 is",avg3)
print("Average of student 4 is",avg4)
print("Average of student 5 is",avg5)
print("")

if avg1>avg2 and avg1>avg3 and avg1>avg4 and avg1>avg5:
    print("First topper ➜ Student 1")
    if avg2>avg3 and avg2>avg4 and avg2>avg5:
        print("Second topper ➜ Student 2")
    elif avg3>avg2 and avg3>avg4 and avg3>avg5:
        print("Second topper ➜ Student 3")
    elif avg4>avg2 and avg4>avg3 and avg4>avg5:
        print("Second topper ➜ Student 4")
    elif avg5>avg2 and avg5>avg3 and avg5>avg4:
        print("Second topper ➜ Student 5")

if avg2>avg1 and avg2>avg3 and avg2>avg4 and avg2>avg5:
    print("First topper ➜ Student 1")
    if avg1>avg3 and avg1>avg4 and avg1>avg5:
        print("Second topper ➜ Student 2")
    elif avg3>avg1 and avg3>avg4 and avg3>avg5:
        print("Second topper ➜ Student 3")
    elif avg4>avg1 and avg4>avg3 and avg4>avg5:
        print("Second topper ➜ Student 4")
    elif avg5>avg1 and avg5>avg3 and avg5>avg4:
        print("Second topper ➜ Student 5")

if avg3>avg1 and avg3>avg2 and avg3>avg4 and avg3>avg5:
    print("First topper ➜ Student 1")
    if avg2>avg1 and avg2>avg4 and avg2>avg5:
        print("Second topper ➜ Student 2")
    elif avg1>avg2 and avg1>avg4 and avg1>avg5:
        print("Second topper ➜ Student 3")
    elif avg4>avg2 and avg4>avg1 and avg4>avg5:
        print("Second topper ➜ Student 4")
    elif avg5>avg2 and avg5>avg1 and avg5>avg4:
        print("Second topper ➜ Student 5")

if avg4>avg2 and avg4>avg3 and avg4>avg1 and avg4>avg5:
    print("First topper ➜ Student 1")
    if avg2>avg3 and avg2>avg1 and avg2>avg5:
        print("Second topper ➜ Student 2")
    elif avg3>avg2 and avg3>avg1 and avg3>avg5:
        print("Second topper ➜ Student 3")
    elif avg1>avg2 and avg1>avg3 and avg1>avg5:
        print("Second topper ➜ Student 4")
    elif avg5>avg2 and avg5>avg3 and avg5>avg1:
        print("Second topper ➜ Student 5")

if avg5>avg2 and avg5>avg3 and avg5>avg4 and avg5>avg1:
    print("First topper ➜ Student 1")
    if avg2>avg3 and avg2>avg4 and avg2>avg1:
        print("Second topper ➜ Student 2")
    elif avg3>avg2 and avg3>avg4 and avg3>avg1:
        print("Second topper ➜ Student 3")
    elif avg4>avg2 and avg4>avg3 and avg4>avg1:
        print("Second topper ➜ Student 4")
    elif avg1>avg2 and avg1>avg3 and avg1>avg4:
        print("Second topper ➜ Student 5")
