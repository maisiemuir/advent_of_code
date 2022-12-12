with open('1_input.txt') as f:
    input = f.read().split("\n")

input_clean = [int(x) if x else None for x in input]

cals_per_elf = []
total_cals = 0
for cals in input_clean:
    if cals:
        total_cals += cals
    else:
        cals_per_elf.append(total_cals)
        total_cals = 0

max_cals = max(cals_per_elf)
print(f"Highest number of calories: {max_cals} kcal")

top_3_summed = sum(sorted(cals_per_elf)[-3:])
print(f"Highest 3 calories summed: {top_3_summed} kcal")