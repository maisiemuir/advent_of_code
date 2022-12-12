import numpy as np

class MonkeyGame:
    def __init__(self):
        self.items = [
            [71, 56, 50, 73],
            [70, 89, 82],
            [52, 95],
            [94, 64, 69, 87, 70],
            [98, 72, 98, 53, 97, 51],
            [79],
            [77, 55, 63, 93, 66, 90, 88, 71],
            [54, 97, 87, 70, 59, 82, 59]
        ]
        self.tests = [
            [13,1,7],
            [7,3,6],
            [3,5,4],
            [19,2,6],
            [5,0,5],
            [2,7,0],
            [11,2,4],
            [17,1,3]
        ]
        self.operations = [
            ["mult", 11],
            ["add", 1],
            ["square", None],
            ["add", 2],
            ["add", 6],
            ["add", 7],
            ["mult", 7],
            ["add", 8]
        ]
        self.inspections = [0,0,0,0,0,0,0,0]

    @staticmethod
    def perform_operation(method, val, old):
        if method == "mult":
            new = old * val
        elif method == "add":
            new = old + val
        else: #method == "square"
            new = old * old
        new = round(new/3)
        return new

    @staticmethod
    def perform_test(worry_lvl, n, true_idx, false_idx):
        if worry_lvl % n == 0:
            return true_idx
        else:
            return false_idx

    def throw_item(self, monkey_idx, next_monkey_idx, worry_level):
        # Drop item from first monkey
        self.items[monkey_idx] = self.items[monkey_idx][1:]
        # Append item to next monkey's list
        self.items[next_monkey_idx].append(worry_level)

    def single_round(self):
        for monkey_idx in range(8):
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
                    next_monkey_idx = self.perform_test(worry_level, test[0], test[1], test[2])
                    # Throw item
                    self.throw_item(monkey_idx, next_monkey_idx, worry_level)

    def run(self, rounds):
        for round in range(rounds):
            self.single_round()
        for monkey_idx in range(8):
            print(f"Monkey {monkey_idx} made {self.inspections[monkey_idx]} inspections.")
        print(f"The total level of monkey business is {np.prod(self.inspections)}.")

game = MonkeyGame()
game.run(rounds=20)