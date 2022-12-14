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

class twoListComparison:
    def __init__(self, list_1, list_2):
        self.right_order = False
        self.list_1 = list_1
        self.list_2 = list_2

    def run(self):
        for i, left_item in enumerate(self.list_1):
            right_item = self.list_2[i]


def compare_two_lists(list_1,list_2):


right_orders = []
for pair_no, pair in enumerate(pairs):
    print(f"== Pair {pair_no} ==")
    list_1 = pair[0]
    list_2 = pair[1]
    print(f"List 1: {list_1}")
    print(f"List 2: {list_2}")
    right_order = False
    for i, left_item in enumerate(list_1):
        right_item = list_2[i]
        print(f"Comparing {left_item} vs {right_item}")

        if left_item < right_item:
            right_order = True
            print("    Left side is smaller, so inputs are in the right order")
            break # Breaks out of for loop

    right_orders.append(right_order)
    if pair_no == 1:
        break