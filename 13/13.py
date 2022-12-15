import json
import numpy as np

class listComparison:
    def __init__(self, pairs, packets, verbose = False):
        self.pairs = pairs
        self.packets = packets
        self.packets.append([[2]])
        self.packets.append([[6]])
        self.spaces = ""
        self.verbose = verbose

    def printv(self, text):
        if self.verbose:
            print(text)

    def compare_items(self, x1, x2):
        """
        :param x1:
        :param x2:
        :return:  True if inputs are "in the right order" (as per definition in Advent of Code)
        """
        if (type(x1) == int) and (type(x2) == int):
            self.printv(f"{self.spaces}- Compare {x1} vs {x2}")
            #print("Left item int and right item int")
            if x1 < x2:
                self.spaces = self.spaces + "  "
                self.printv(f"{self.spaces}- Left side is smaller, so inputs are in the RIGHT ORDER")
                return True
            elif x1 > x2:
                self.spaces + "  "
                self.printv(f"{self.spaces}- Right side is smaller, so inputs are in the WRONG ORDER")
                return False
            else:
                return "same"
            # If x1 == x2, do nothing
        else: #i.e. at least one is list
            self.spaces = self.spaces + "  "
            if (type(x2) == int):
                x2 = [x2]
                self.printv(f"{self.spaces}- Mixed types; convert right to {x2} and retry comparison")
            if (type(x1) == int):
                x1 = [x1]
                self.printv(f"{self.spaces}- Mixed types; convert left to {x1} and retry comparison")
            self.printv(f"{self.spaces}- Compare {x1} vs {x2}")
            max_length = max(len(x1), len(x2))
            if x1 == x2:
                if x1 == []:
                    return "same"
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
                    self.printv(f"{self.spaces}- Left side ran out of items, so inputs are in the RIGHT ORDER")
                    return True
                elif no_right and not no_left:
                    self.printv(f"{self.spaces}- Right side ran out of items, so inputs are in the WRONG ORDER")
                    return False
                #elif no_right and no_left:
                    #print("hi")
                    #return "same"
                else:
                    value = self.compare_items(l_item, r_item)
                    if value == "same":
                        if i == max_length - 1: #Only return "same" if we are at the end of the list
                            return value
                    else:
                        return value
                    # Note we can shorten the above probably

    def run_part1(self):
        correct_pairs = []
        for i, pair in enumerate(self.pairs):
            self.spaces = ""
            self.printv(f"== Pair {i+1} ==")
            list1 = pair[0]
            list2 = pair[1]
            value = self.compare_items(list1, list2)
            if value:
                correct_pairs.append(i+1)

        print(f"The sum of the indices of the correct pairs: {np.sum(correct_pairs)}")

    def run_part2(self):
        order_found = False
        iters = 0
        while not order_found:
            switched = False
            for i in range(len(self.packets) - 1):
                packet_1 = self.packets[i]
                packet_2 = self.packets[i+1]
                correct_order = self.compare_items(packet_1,packet_2)
                if not correct_order:
                    # Switch their order
                    self.packets[i] = packet_2
                    self.packets[i+1] = packet_1
                    switched = True
            if switched == False:
                order_found = True

            iters+=1
        decoder_key = 1
        for i, packet in enumerate(self.packets):
            if (packet == [[2]]) | (packet == [[6]]):
                decoder_key = decoder_key*(i+1)
        print(f"Decoder key: {decoder_key}")


with open('13_input.txt') as f:
    input = f.read().split("\n")
    input = [x for x in input if x != ""]
    pairs = []
    packets = []
    for i, row in enumerate(input):
        if i % 2 == 0: # the first of the pair
            pair = []
            pair.append(json.loads(row))
        else:
            pair.append(json.loads(row))
            pairs.append(pair)
        packets.append(json.loads(row))


list_comparison = listComparison(pairs,packets,verbose=False)
list_comparison.run_part1()
list_comparison.run_part2()


