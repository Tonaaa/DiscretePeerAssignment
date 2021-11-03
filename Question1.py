# Question 1
user_input = input("Fill in a list of elements in a set to check if it's valid. \n"
                   "Separate each item with a comma. DO NOT use quotation marks OR spaces ")
set = user_input.split(',')
final_set = []
for item in set:
    if item not in final_set:
        final_set.append(item)
if set == final_set:
    print(f'\nTrue. Your set was:\n {set} \n and it is valid')
    print()
else:
    print(f'\nFalse. Your set is invalid and should be {final_set}')
