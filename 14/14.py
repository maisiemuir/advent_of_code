with open('14_example_input.txt') as f:
    input = f.read().split("\n")
    input_clean = []
    for row in input:
        row_clean = [x.split(",") for x in row.split(" -> ")]
        for i, item in enumerate(row_clean):
            for j, x in enumerate(item):
                row_clean[i][j] = int(row_clean[i][j])
        input_clean.append(row_clean)

print(input)
print(input_clean)
xs = []
ys = []
for row in input_clean:
    for x, y in row:
       xs.append(x)
       ys.append(y)
max_x = max(xs)
min_x = min(xs)
max_y = max(ys)
min_y = max(ys)

def item(x,y):
    return
# df[y][x]
max_x = 3
max_y = 5
#print([["."max_x+1) for x in range()
image = [["." for x in range(max_x + 1)] for y in range(max_y + 1)]
image = [["." for x in range(max_y + 1)] for y in range(max_x + 1)]
print(image)
image[0][2] = "x"

def print_image(image):
    width = len(image[0])
    string = ""
    for x in range(width):
        for ys in image:
            string = string + ys[x]
        string = string + "\n"
    print(string)

print_image(image)
print(input_clean)


val1 = 5
val2 = 10
for i in range(val1, val2+1):
    print(i)

print(False > 4)