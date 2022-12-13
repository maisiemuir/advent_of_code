class getShortestPath:
    def __init__(self, grid):
        self.grid = grid
        self.grid_height = len(self.grid)
        self.grid_width = len(self.grid[0])

        # Get start position
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                if self.grid[i][j] == "S":
                    self.start_pos = [i,j]

    @staticmethod
    def get_next_pos(current_pos, move):
        i, j = current_pos
        # Assumes move is feasible
        if move == 0:
            i = i - 1
        elif move == 1:
            j +=1
        elif move == 2:
            i +=1
        else: #move == 3
            j = j - 1
        return [i, j]

    @staticmethod
    def get_height(letter):
        if letter == "S":
            return 1
        elif letter == "E":
            return 26
        else:
            return ord(letter) - 96

    def is_move_possible(self, current_pos, move, route):
        """
        :param current_pos: [i,j]
        :param move: 0 (up), 1 (right), 2 (down), 3 (left)
        :param route: [[a,b],[c,d],[e,f],...] route up until now
        :return: True or False
        """
        # Get current position on grid
        i, j = current_pos
        # Cannot move out of the grid
        if (i == 0) and (move == 0):
            return False
        if (i == self.grid_height - 1) and (move == 2):
            return False
        if (j == self.grid_width - 1) and (move == 1):
            return False
        if (j == 0) and (move == 3):
            return False

        # Get current and next position
        current_letter = self.grid[i][j]
        next_pos = self.get_next_pos(current_pos, move)

        # Check we haven't been there already
        if next_pos in route:
            return False
        else:
            # Get current and next heights
            i_next, j_next = next_pos
            next_letter = self.grid[i_next][j_next]
            current_height = self.get_height(current_letter)
            next_height = self.get_height(next_letter)
            if next_height <= current_height + 1:
                return True
            else:
                return False

    def get_all_possible_moves(self, pos, route):
        possible_moves = []
        for move in range(4):
            if self.is_move_possible(pos, move, route):
                possible_moves.append(move)
        return possible_moves

    def run(self):
        num_steps = 0
        found_E = False
        while not found_E:
            # Get new routes
            if num_steps == 0:
                all_routes = [[self.start_pos]]
            else:
                all_routes = new_all_routes.copy()
            new_all_routes = []
            for route in all_routes:
                current_pos = route[-1]
                possible_moves = self.get_all_possible_moves(current_pos, route)
                for move in possible_moves:
                    a_new_route = route.copy()
                    next_pos = self.get_next_pos(current_pos, move)
                    a_new_route.append(next_pos)
                    new_all_routes.append(a_new_route)
            num_steps += 1
            # Check if found E
            for route in new_all_routes:
                i_current, j_current = route[-1]
                if self.grid[i_current][j_current] == "E":
                    found_E = True
        print(f"End found in {num_steps} steps.")

example_grid = [['S','a','b','q','p','o','n','m'],
                ['a','b','c','r','y','x','x','l'],
                ['a','c','c','s','z','E','x','k'],
                ['a','c','c','t','u','v','w','j'],
                ['a','b','d','e','f','g','h','i']]

path_finder = getShortestPath(example_grid)
path_finder.run()

#my_grid =