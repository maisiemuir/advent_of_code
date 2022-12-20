class beaconExclusions:
    def __init__(self, file_name):
        self.sensor_coords, self.beacon_coords = self.read_file(file_name)
        self.get_min_max()
        #self.display_grid()
        #self.populate_grid()

    def read_file(self, file_name):
        with open(file_name + ".txt") as f:
            input = f.read().split("\n")
            sensor_coords, beacon_coords = [], []
            for row in input:
                row_transformed = row.replace("Sensor at x=", "").replace(", y=", " ").replace(
                    ": closest beacon is at x=", " ")
                row_transformed = [int(x) for x in row_transformed.split(" ")]
                sensor_coords.append(row_transformed[:2])
                beacon_coords.append(row_transformed[-2:])
        return sensor_coords, beacon_coords

    def get_min_max(self):
        sensor_x_coords = [x[0] for x in self.sensor_coords]
        sensor_y_coords = [x[1] for x in self.sensor_coords]
        beacon_x_coords = [x[0] for x in self.beacon_coords]
        beacon_y_coords = [x[1] for x in self.beacon_coords]
        # Edit thewse if we want a larger/smaller grid
        # We could really optimise how we get the min and max coords required, but CBA
        self.min_x = min(sensor_x_coords + beacon_x_coords) - 1000000
        self.max_x = max(sensor_x_coords + beacon_x_coords) + 1000000
        self.min_y = min(sensor_y_coords + beacon_y_coords) - 1000000
        self.max_y = max(sensor_y_coords + beacon_y_coords) + 1000000
        print(f"min x: {self.min_x}")
        print(f"max x: {self.max_x}")
        print(f"min y: {self.min_y}")
        print(f"max y: {self.max_y}")

    @staticmethod
    def manhattan_distance(coord1, coord2):
        return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


    def run(self, y):
        count = 0
        total = len([i for i in range(self.min_x, self.max_x + 1)])
        idx = 1
        for x in range(self.min_x, self.max_x + 1):
            if idx % 100000 == 0:
                print(f"{idx} out of {total} x coordinates checked...")
            if [x,y] not in self.sensor_coords:
                if [x,y] in self.beacon_coords:
                    pass
                else:
                    for i, sensor_coord in enumerate(self.sensor_coords):
                        beacon_coord = self.beacon_coords[i]
                        dist_sensor_to_coord = self.manhattan_distance(sensor_coord, [x,y])
                        dist_sensor_to_beacon = self.manhattan_distance(sensor_coord, beacon_coord)
                        if dist_sensor_to_coord <= dist_sensor_to_beacon:
                            count+=1
                            # Exit loop!
                            break
            idx +=1
        print(f"Number of positions that cannot contain beacon: {count}")



#beacon_exclusions = beaconExclusions("15_example_input")
#beacon_exclusions.run(y=10)

beacon_exclusions = beaconExclusions("15_input")
beacon_exclusions.run(y=2000000)