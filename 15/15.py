class beaconExclusions:
    def __init__(self, file_name):
        self.coords = self.read_file(file_name)
        self.initialise_grid()
        #self.display_grid()
        self.populate_grid()

    def read_file(self, file_name):
        with open(file_name + ".txt") as f:
            input = f.read().split("\n")
            coords = []
            for row in input:
                row_transformed = row.replace("Sensor at x=", "").replace(", y=", " ").replace(
                    ": closest beacon is at x=", " ")
                row_transformed = [int(x) for x in row_transformed.split(" ")]
                coords.append(row_transformed)
        return coords

    def get_min_max(self):
        sensor_x_coords = [x[0] for x in self.coords]
        sensor_y_coords = [x[1] for x in self.coords]
        beacon_x_coords = [x[2] for x in self.coords]
        beacon_y_coords = [x[3] for x in self.coords]
        # Edit thewse if we want a larger/smaller grid
        # We could really optimise how we get the min and max coords required, but CBA
        self.min_x = min(sensor_x_coords + beacon_x_coords) - 20
        self.max_x = max(sensor_x_coords + beacon_x_coords) + 20
        self.min_y = min(sensor_y_coords + beacon_y_coords) - 20
        self.max_y = max(sensor_y_coords + beacon_y_coords) + 20
        print(f"min x: {self.min_x}")
        print(f"max x: {self.max_x}")
        print(f"min y: {self.min_y}")
        print(f"max y: {self.max_y}")

    def assign_grid(self, x, y, string):
        self.map[x-self.min_x][y-self.min_y] = string

    def grid(self, x, y):
        # If min x is -32 and min y is -24 for example, we want grid[-32][-24] to return the value grid[0][0]
        return self.map[x-self.min_x][y-self.min_y]

    def initialise_grid(self):
        self.get_min_max()
        print(f"width: {abs(self.max_x - self.min_x)}")
        print(f"height: {abs(self.max_y - self.min_y)}")
        self.map = [["." for x in range(self.min_y, self.max_y + 1)] for y in range(self.min_x, self.max_x + 1)]

    def display_grid(self):
        string = ""
        for y in range(len(self.map[0])):
            for x in range(len(self.map)):
                xs = self.map[x]
                string = string + xs[y]
            string = string + "\n"
        print(string)

    @staticmethod
    def manhattan_distance(coord1, coord2):
        return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

    def populate_grid(self):
        for row in self.coords:
            sensor_coord = row[:2]
            print(f"sensor_coord: {sensor_coord}")
            beacon_coord = row[-2:]
            print(f"beacon_coord: {beacon_coord}")
            distance = self.manhattan_distance(sensor_coord, beacon_coord)
            self.assign_grid(sensor_coord[0], sensor_coord[1], "S")
            self.assign_grid(beacon_coord[0], beacon_coord[1], "B")
            for x in range(sensor_coord[0] - distance, sensor_coord[0] + distance + 1):
                print(f"x = {x}...")
                for y in range(sensor_coord[1] - distance, sensor_coord[1] + distance + 1):
                    if self.grid(x,y) == ".":
                        if self.manhattan_distance(sensor_coord, [x,y]) <= distance:
                            self.assign_grid(x,y,"#")
            break
            #self.display_grid()

    def count_beacon_not_present(self, y):
        count = 0
        for x in range(self.min_x, self.max_x + 1):
            if self.grid(x,y) == "#" or self.grid(x,y) == "S":
                print(f"x,y = {x}, {y}")
                count+=1
        print(f"Number of positions that cannot contain beacon: {count}")



#beacon_exclusions = beaconExclusions("15_example_input")
#beacon_exclusions.count_beacon_not_present(y=10)
beacon_exclusions = beaconExclusions("15_input")
#rint(beacon_exclusions.min_x)
#print(beacon_exclusions.min_y)
#beacon_exclusions.count_beacon_not_present(y=2000000)
