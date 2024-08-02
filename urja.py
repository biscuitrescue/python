num= int(input('Enter a number: '))
factorial=1
a=1
if num<0:
 print('factorial doesnt exist')
elif num==0:
 print('factorial of 0 is 1')
else:
 while a<=num:
  factorial=factorial*a
  a=a+1

print("factorial of",num,"is",factorial)
