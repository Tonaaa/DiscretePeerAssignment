# Question 3

# Input of the first list's elements
userA = int(input("Enter the number of elements of list A: "))
listA = []
i = 1
for item in range(userA):
    elementA = int(input(f"Enter the {i} element of listA: "))
    listA.append(elementA)
    i+=1
print("List A elements are:", listA)

# Input of the second list's elements
userB = int(input("Enter the number of elements of list B: "))
listB = []
i = 1
for item in range(userB):
    elementB = int(input(f"Enter the {i} element of listB: "))
    listB.append(elementB)
print("List B elements are:", listB)

# a)  Finding if B is a subset of A
i = 0
p = 0
c = 0
for i in range(userB):
    for c in range(userA):
        if listB[i] == listA[c]:
            p += 1
if p == userB:
    print("\n\nTrue. B is a subset of A")
else:
    print("\n\nFalse. B is not a subset of A")


# b) The representation of A-B
listC = []
for i in range(userA):
    if listA[i] not in listB:
        listC.append(listA[i])
print("A-B: " + str(listC))


# c) The representation of A*B
cartesian_list = []
for i in range(userB):
    for c in range(userA):
        sub_cartesian_list = [listB[i], listA[c]]
        cartesian_list.append(sub_cartesian_list)
print("A X B: " + str(cartesian_list))
