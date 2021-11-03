# Question 4

listA_input = input("Put the list's elements here, separate each element with a comma ")
listA = listA_input.split(",")
print(f"Your list A is {listA}")

listR_input = input("Input pairs of elements(without a space after the comma) enclosed in parenthesis. \n"
                    "Separate each tuple by a space rather than a comma. e.g (1,2) (5,4) (8,6) ")
temp_listR = listR_input.split()
listR = []
transit = []
for each in temp_listR:
    for l in each:
        if l != ',' and l != '(' and l != ')':
            transit.append(l)
    temp = tuple(transit[0] + transit[1])
    listR.append(temp)
    transit = []
print(f"Your relation is {listR}")

# check if R is a set
R_is_set = listR
final_set = []
for item in R_is_set:
    if item not in final_set:
        final_set.append(item)
if R_is_set == final_set:
    print('\n\nR is a set')
else:
    print('\n\nR is not a set')

# check if R is a subset
# do cart prod
cartesian = []
for each in listA:
    for i in listA:
        for z in i:
            if z != ',' and z != '(' and z != ')':
                temp = tuple(each + z)
                cartesian.append(temp)
p = 0
for i in range(len(listR)):
    for c in range(len(cartesian)):
        if listR[i] == cartesian[c]:
            p += 1
if p == len(listR):
    print("R is a subset of A x A")
else:
    missing_element = []
    for each in listR:
        if each not in cartesian:
            missing_element.append(each)
    print(f"R is not a subset of A x A because the following element is in R but not in A: {missing_element}")

# Check for reflexivity

save = []
comparison = []
count = 0
anothersave = []
finalvar = []
for each in listR:
    for i in each:
        if i != ',' and i != '(' and i != ')':
            if i not in save:
                save.append(i)
for every in save:
    random = every, every
    sometuple = tuple(random)
    comparison.append(sometuple)
for each in comparison:
    if each in listR:
        count += 1
if count == len(comparison):
    print('R is reflexive')
else:
    for each in save:
        anotherrandom = each, each
        temp = tuple(anotherrandom)
        anothersave.append(temp)
        if temp not in listR:
            finalvar.append(each)
    print(f'R is not reflexive, because the number(s) {finalvar} do not have reflexive pair(s)')

# transitive

not_transitive = []
for w,x in listR:
    for y,z in listR:
        if x == y and ((w, z) in listR):
            answer = "R is transitive"
            break
        if x == y and ((w, z) not in listR):
            not_transitive.append([w, x])
            not_transitive.append([y, z])
            answer = (f"R is not transitive: {not_transitive}")
            break
print(answer)

# symmetric

not_symmetric = []
var = True
for a, b in listR:
    if (b, a) not in listR:
        not_symmetric.append([a, b])
        response = (f"R is not symmetric: {not_symmetric}")
        var = False
if var is True:
    response = "R is symmetric"
print(response)