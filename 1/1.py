with open('1_input.txt') as f:
    input = f.readlines()

input_clean = [int(x.replace("\n","")) if x != "\n" else None for x in input]

cals_per_elf = []
total_cals = 0
for cals in input_clean:
    if cals:
        total_cals += cals
    else:
        cals_per_elf.append(total_cals)
        total_cals = 0

max_cals = max(cals_per_elf)
elf_number = cals_per_elf.index(max_cals) + 1

print(f"Elf {elf_number} has the most calories, with {max_cals} kcal in total.")