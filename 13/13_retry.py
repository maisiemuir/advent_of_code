import json
with open('13_example_input.txt') as f:
    input = f.read().split("\n")
    input = [x for x in input if x != ""]
    pairs = []
    for i, row in enumerate(input):
        if i % 2 == 0: # the first of the pair
            pair = []
            pair.append(json.loads(row))
        else:
            pair.append(json.loads(row))
            pairs.append(pair)

def compare_two_items(left_item, right_item):
    print(f"Comparing {left_item} and {right_item}...")
    if (type(left_item) == int) and (type(right_item) == int):
        print("Left item int and right item int")
        if left_item < right_item:
            return True
        elif left_item > right_item:
            return False
        else:
            return "..."
    if (type(left_item) == list) and (type(right_item) == list):
        print("Left item list and right item list")
        for i in range(max(len(left_item),len(right_item))):
            no_left = False
            no_right = False
            try:
                l_item = left_item[i]
            except IndexError:
                no_left = True
            try:
                r_item = right_item[i]
            except IndexError:
                no_right = True
            if no_left and not no_right:
                return True
            elif no_right and not no_left:
                return False
            #elif no_left and no_right:
                #return "..." # Maybe just keep going?
            else:
                if compare_two_items(l_item, r_item) == "...":
                    pass
                else:
                    return compare_two_items(l_item, r_item)
    else: #exactly one is list and one is int? maybe
        print("One item int and one list")
        if (type(right_item) == int):
            right_item = [right_item]
        if (type(left_item) == int):
            left_item = [left_item]
        for i in range(max(len(left_item),len(right_item))):
            no_left = False
            no_right = False
            try:
                l_item = left_item[i]
            except IndexError:
                no_left = True
            try:
                r_item = right_item[i]
            except IndexError:
                no_right = True
            if no_left and not no_right:
                print("No left item")
                return True
            elif no_right and not no_left:
                print("No right item")
                return False
            #elif no_left and no_right:
                #return "..." # Maybe just keep going?
            else:
                return compare_two_items(l_item, r_item)
"""
list_1 = pairs[0][0]
list_2 = pairs[0][1]
print(list_1)
print(list_2)
for i in range(len(list_1)):
    value = compare_two_items(list_1[i], list_2[i])
    print(value)
    if value == True:
        break"""

"""list_1 = pairs[1][0]
list_2 = pairs[1][1]
print(list_1)
print(list_2)
#print(compare_two_items(list_1[1],list_2[1]))
#print(val)
for i in range(len(list_1)):
    value = compare_two_items(list_1[i], list_2[i])
    print(value)
    if (value == True) or (value == False):
        break"""

"""list_1 = pairs[2][0]
list_2 = pairs[2][1]
print(list_1)
print(list_2)
#print(compare_two_items(list_1[1],list_2[1]))
#print(val)
for i in range(len(list_1)):
    value = compare_two_items(list_1[i], list_2[i])
    print(value)
    if (value == True) or (value == False):
        break"""

"""list_1 = pairs[3][0]
list_2 = pairs[3][1]
print(list_1)
print(list_2)
#print(compare_two_items(list_1[1],list_2[1]))
#print(val)
for i in range(max(len(list_1), len(list_2))):
    no_right, no_left = False, False
    try:
        left_item = list_1[i]
    except IndexError:
        no_left = True
    try:
        right_item = list_2[i]
    except IndexError:
        no_right = True
    if no_left and not no_right:
        value = True
    elif no_right and not no_left:
        value = False
    else:
        value = compare_two_items(left_item, right_item)

    #value = compare_two_items(list_1[i], list_2[i])
    print(value)
    if (value == True) or (value == False):
        break"""

"""list_1 = pairs[7][0]
list_2 = pairs[7][1]
print(list_1)
print(list_2)
#print(compare_two_items(list_1[1],list_2[1]))
#print(val)
for i in range(max(len(list_1), len(list_2))):
    print(f"ITEM {i+1}")
    no_right, no_left = False, False
    try:
        left_item = list_1[i]
    except IndexError:
        no_left = True
    try:
        right_item = list_2[i]
    except IndexError:
        no_right = True
    if no_left and not no_right:
        value = True
    elif no_right and not no_left:
        value = False
    else:
        value = compare_two_items(left_item, right_item)

    #value = compare_two_items(list_1[i], list_2[i])
    print(value)
    if (value == True) or (value == False):
        break"""

list_1 = pairs[7][0]
list_2 = pairs[7][1]
print(list_1)
print(list_2)
#print(compare_two_items(list_1[1],list_2[1]))
#print(val)
final_values = []
for pair_num in range(len(pairs)):
    print(f"== Pair {pair_num + 1}")
    list_1 = pairs[pair_num][0]
    list_2 = pairs[pair_num][1]
    for i in range(max(len(list_1), len(list_2))):
        print(f"ITEM {i+1}")
        no_right, no_left = False, False
        try:
            left_item = list_1[i]
        except IndexError:
            no_left = True
        try:
            right_item = list_2[i]
        except IndexError:
            no_right = True
        if no_left and not no_right:
            value = True
        elif no_right and not no_left:
            value = False
        else:
            value = compare_two_items(left_item, right_item)

        #value = compare_two_items(list_1[i], list_2[i])
        print(value)
        if (value == True) or (value == False):
            final_values.append(value)
            break

for i in range(len(pairs)):
    print(f"== Pair {i + 1}")
    print(final_values[i])

true_pairs = []
for i in range(len(pairs)):
    if final_values[i]:
        true_pairs.append(i+1)
    #print(final_values[i])
print(sum(true_pairs))