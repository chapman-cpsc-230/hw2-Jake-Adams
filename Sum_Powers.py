import math

b = float(input("Enter a Floating Point Number: "))
n = int(input("Enter an integer: "))
m = n
total = 0
while n >= 0:
    total = total + b**n
    n = n-1


print(total)

a = b**(m+1)
c = a/(b-1)
#print(a)
print(c)
