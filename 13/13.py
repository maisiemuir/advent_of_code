import json
import numpy as np

class listComparison:
    def __init__(self, pairs):
        self.pairs = pairs
        self.spaces = ""

    def compare_items(self, x1, x2):
        """
        :param x1:
        :param x2:
        :return:  True if inputs are "in the right order" (as per definition in Advent of Code)
        """
        if (type(x1) == int) and (type(x2) == int):
            print(f"{self.spaces}- Compare {x1} vs {x2}")
            #print("Left item int and right item int")
            if x1 < x2:
                self.spaces = self.spaces + "  "
                print(f"{self.spaces}- Left side is smaller, so inputs are in the RIGHT ORDER")
                return True
            elif x1 > x2:
                self.spaces + "  "
                print(f"{self.spaces}- Right side is smaller, so inputs are in the WRONG ORDER")
                return False
            else:
                return "same"
            # If x1 == x2, do nothing
        else: #i.e. at least one is list
            self.spaces = self.spaces + "  "
            if (type(x2) == int):
                x2 = [x2]
                print(f"{self.spaces}- Mixed types; convert right to {x2} and retry comparison")
            if (type(x1) == int):
                x1 = [x1]
                print(f"{self.spaces}- Mixed types; convert left to {x1} and retry comparison")
            print(f"{self.spaces}- Compare {x1} vs {x2}")
            max_length = max(len(x1), len(x2))
            for i in range(max_length):
                #print(f"Comparing {i+1} of {max(len(x1), len(x2))} items")
                no_left = False
                no_right = False
                try:
                    l_item = x1[i]
                except IndexError:
                    no_left = True
                try:
                    r_item = x2[i]
                except IndexError:
                    no_right = True
                if no_left and not no_right:
                    print(f"{self.spaces}- Left side ran out of items, so inputs are in the RIGHT ORDER")
                    return True
                elif no_right and not no_left:
                    print(f"{self.spaces}- Right side ran out of items, so inputs are in the WRONG ORDER")
                    return False
                else:
                    value = self.compare_items(l_item, r_item)
                    if value == "same":
                        if i == max_length - 1: #Only return "same" if we are at the end of the list
                            return value
                    else:
                        return value
                    # Note we can shorten the above probably

    def run(self):
        correct_pairs = []
        for i, pair in enumerate(self.pairs):
            self.spaces = ""
            print(f"== Pair {i+1} ==")
            list1 = pair[0]
            list2 = pair[1]
            #print(self.compare_items(list1, list2))
            if self.compare_items(list1, list2) == True: #Get rid of the == True bit
                correct_pairs.append(i+1)
        print(f"The sum of the indices of the correct pairs: {np.sum(correct_pairs)}")


with open('13_input.txt') as f:
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

list_comparison = listComparison(pairs)
list_comparison.run()