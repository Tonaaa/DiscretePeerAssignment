# Question 5
inputX = input('input elements of a list "X". Separate by comma')
inputY = input('input elements of a list "Y". Separate by comma')
splitX = inputX.split(',')
splitY = inputY.split(',')
X = []
Y = []
for each in splitX:
    integer = int(each)
    X.append(integer)
for v in splitY:
    integer = int(v)
    Y.append(integer)
for y in Y:
    count = 0
    for x in X:
        if x%y != 0:
            count += 1
    if count == 0:
        truth = True
        break
if truth:
    print('True')
else:
    print('False')
