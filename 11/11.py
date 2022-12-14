import numpy as np

class MonkeyGame:
    def __init__(self, items, tests, operations, divide_by_3 = True):
        self.items = items
        self.tests = tests
        self.operations = operations
        self.no_monkeys = len(items)
        self.inspections = [0]*self.no_monkeys
        self.divide_by_3 = divide_by_3
        if not self.divide_by_3:
            self.divisor = np.prod([x[0] for x in self.tests])

    def perform_operation(self, method, val, old):
        if method == "mult":
            new = old * val
        elif method == "add":
            new = old + val
        else: #method == "square"
            new = old * old
        if self.divide_by_3:
            new = new//3
        return new

    def perform_test(self, worry_lvl, n, true_idx, false_idx):
        if not self.divide_by_3:
            if worry_lvl > 96577*3:
                worry_lvl = worry_lvl - (self.divisor)*((worry_lvl//self.divisor) - 1)
        if worry_lvl % n == 0:
            return true_idx, worry_lvl
        else:
            return false_idx, worry_lvl

    def throw_item(self, monkey_idx, next_monkey_idx, worry_level):
        # Drop item from first monkey
        self.items[monkey_idx] = self.items[monkey_idx][1:]
        # Append item to next monkey's list
        self.items[next_monkey_idx].append(worry_level)

    def single_round(self):
        for monkey_idx in range(self.no_monkeys):
            # Get monkey's attributes
            current_items = self.items[monkey_idx]
            operation = self.operations[monkey_idx]
            test = self.tests[monkey_idx]
            if len(current_items) != 0:
                for worry_level in current_items:
                    # Monkey inspects item
                    self.inspections[monkey_idx] += 1
                    # Worry level changes
                    worry_level = self.perform_operation(operation[0], operation[1], worry_level)
                    # Perform test to see where item will be thrown
                    next_monkey_idx, worry_level = self.perform_test(worry_level, test[0], test[1], test[2])
                    # Throw item
                    self.throw_item(monkey_idx, next_monkey_idx, worry_level)

    def run(self, rounds):
        for round in range(rounds):
            round += 1 # Round 0 doesn't make sense
            self.single_round()
            if ((round % 200 == 0) and (round != 0)) | (round == 20) | (round == 1) | (round == rounds):
                print(f"== After round {round} ==")
                for monkey_idx in range(self.no_monkeys):
                    print(f"Monkey {monkey_idx} made {self.inspections[monkey_idx]} inspections.")
        print(f"The total level of monkey business is {np.prod(sorted(self.inspections)[::-1][:2])}.")

# Example input
items = [
    [79, 98],
    [54, 65, 75, 74],
    [79, 60, 97],
    [74]
]
tests = [
    [23, 2, 3],
    [19, 2, 0],
    [13, 1, 3],
    [17, 0, 1]
]
operations = [
    ["mult", 19],
    ["add", 6],
    ["square", None],
    ["add", 3]
]

game = MonkeyGame(items, tests, operations)
game.run(rounds=20)

game = MonkeyGame(items, tests, operations, divide_by_3=False)
game.run(rounds=10000)

# My input
items = [
    [71, 56, 50, 73],
    [70, 89, 82],
    [52, 95],
    [94, 64, 69, 87, 70],
    [98, 72, 98, 53, 97, 51],
    [79],
    [77, 55, 63, 93, 66, 90, 88, 71],
    [54, 97, 87, 70, 59, 82, 59]
]
tests = [
    [13,1,7],
    [7,3,6],
    [3,5,4],
    [19,2,6],
    [5,0,5],
    [2,7,0],
    [11,2,4],
    [17,1,3]
]
operations = [
    ["mult", 11],
    ["add", 1],
    ["square", None],
    ["add", 2],
    ["add", 6],
    ["add", 7],
    ["mult", 7],
    ["add", 8]
]
game = MonkeyGame(items, tests, operations)
game.run(rounds=20)

game = MonkeyGame(items, tests, operations, divide_by_3=False)
game.run(rounds=10000)