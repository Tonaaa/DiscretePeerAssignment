# Question 2
from itertools import product
# a
user_setA = input("Enter the elements of the first set separated by a comma ")
setA = set(user_setA.split(","))

user_setB = input("Enter the elements of the second set separated by a comma ")
setB = set(user_setB.split(","))

print(setB.issubset(setA))

# b
print(setA.difference(setB))

# c
print(set(product(setA, setB)))
