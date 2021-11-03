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
count = 0
for x in X:
    for y in Y:
        if x%y == 0:
            count += 1
if count == len(X):
    print('True')
else:
    print('False')
