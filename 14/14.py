class sandPath:
    def __init__(self, file_name, infinite_floor = False):
        self.rock_coords = self.read_file(file_name)

        self.infinite_floor = infinite_floor

        self.initialise_grid()
        self.add_rocks_to_grid()

        self.sand_coords = [500,0]

    def initialise_grid(self):
        self.rock_min_x, self.rock_max_x, self.rock_min_y, self.rock_max_y = self.get_min_max(self.rock_coords)
        if self.infinite_floor:
            y_coord_inf_floor = self.rock_max_y + 2
            self.rock_coords.append([[0,y_coord_inf_floor],[self.rock_max_x+1000,y_coord_inf_floor]])
            self.rock_min_x, self.rock_max_x, self.rock_min_y, self.rock_max_y = self.get_min_max(self.rock_coords)
        self.grid = [["." for x in range(self.rock_max_y + 1)] for y in range(self.rock_max_x + 1000 + 1)]


    def add_rocks_to_grid(self):
        for rock_cluster_coords in self.rock_coords:
            for i, coord in enumerate(rock_cluster_coords):
                if i == 0:
                    self.grid[coord[0]][coord[1]] = "#"
                else:
                    # Check if x has changed or y has changed
                    current_x_val = coord[0]
                    current_y_val = coord[1]
                    previous_x_val = rock_cluster_coords[i-1][0]
                    previous_y_val = rock_cluster_coords[i-1][1]
                    if current_x_val != previous_x_val:
                        min_x_val = min(current_x_val,previous_x_val)
                        max_x_val = max(current_x_val,previous_x_val)
                        for x_val in range(min_x_val,max_x_val+1):
                            self.grid[x_val][current_y_val] = "#"
                    else:
                        min_y_val = min(current_y_val, previous_y_val)
                        max_y_val = max(current_y_val, previous_y_val)
                        for y_val in range(min_y_val, max_y_val + 1):
                            self.grid[current_x_val][y_val] = "#"

    @staticmethod
    def get_min_max(coords):
        xs, ys = [], []
        for row in coords:
            for x, y in row:
                xs.append(x)
                ys.append(y)
        return min(xs), max(xs), min(ys), max(ys)

    @staticmethod
    def read_file(file_name):
        with open(file_name + ".txt") as f:
            input = f.read().split("\n")
            input_clean = []
            for row in input:
                row_clean = [x.split(",") for x in row.split(" -> ")]
                for i, item in enumerate(row_clean):
                    for j, x in enumerate(item):
                        row_clean[i][j] = int(row_clean[i][j])
                input_clean.append(row_clean)
        return input_clean

    def display_grid(self,x_min = False,x_max = False):
        string = ""
        for y in range(len(self.grid[0])):
            for x in range(len(self.grid)):
                xs = self.grid[x]
                if x_min and not x_max:
                    if x >= x_min:
                        string = string + xs[y]
                elif x_max and not x_min:
                    if x <= x_max:
                        string = string + xs[y]
                elif x_min and x_max:
                    if x >= x_min and x <= x_max:
                        string = string + xs[y]
                else:
                    string = string + xs[y]
            string = string + "\n"
        print(string)

    def next_move(self, coords):
        x = coords[0]
        y = coords[1]
        if self.grid[x][y+1] == ".":
            return [x,y+1]
        elif self.grid[x-1][y+1] == ".":
            return [x-1,y+1]
        elif self.grid[x+1][y+1] == ".":
            return [x+1,y+1]
        else:
            return coords

    def forever_falling(self, coords):
        x = coords[0]
        y = coords[1]
        min_y = y + 1
        max_y = self.rock_max_y
        if y == max_y:
            return True
        for y0 in range(min_y,max_y+1):
            if self.grid[x][y0] != ".":
                return False
        return True

    def run(self):
        simulation_running = True
        T = 0
        sand_at_rest = 0
        while simulation_running:
            # Instantiate piece of sand
            # Note: currently assumes that the piece of sand can be initiated here (i.e. nothing blocking)
            coords_curr = self.sand_coords #self.grid[self.sand_coords[0]][self.sand_coords[1]]
            if self.grid[coords_curr[0]][coords_curr[1]] == "o":
                #  If no space left for sand
                comment = "No space left for sand."
                self.display_grid(x_min=490)
                simulation_running = False
            else:
                self.grid[coords_curr[0]][coords_curr[1]] = "+"
            sand_in_air = True
            while sand_in_air and simulation_running:
                # First check if sand is forever falling
                if self.forever_falling(coords_curr):
                    comment = "Sand falling forever."
                    self.display_grid(x_min=450)
                    sand_in_air = False #bad choice of variable name lols
                    simulation_running = False
                coords_next = self.next_move(coords_curr)
                if coords_next == coords_curr:
                    # Sand can't move anywhere
                    self.grid[coords_curr[0]][coords_curr[1]] = "o"
                    sand_at_rest += 1
                    sand_in_air = False
                else:
                    self.grid[coords_curr[0]][coords_curr[1]] = "."
                    self.grid[coords_next[0]][coords_next[1]] = "+"
                    coords_curr = coords_next
            print(f"T = {T}")
            T+=1
        print(comment)
        print(f"Sand grains at rest: {sand_at_rest}")



sand_path = sandPath("14_input", infinite_floor=True)
sand_path.run()
#sand_path.display_grid(x_min = -5)


sand_path = sandPath("14_example_input", infinite_floor=True)
#sand_path.run()
