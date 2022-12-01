import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

data = []
with open("input.txt", "r") as f:
    data = [f.strip() for f in f.readlines()]


all_elves_calories = []
elf_calories = 0
for single_calories in data:

    if not single_calories:
        all_elves_calories.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(single_calories)

# part 1 answer
print(max(all_elves_calories))

# part 2
top_3_elves = []
for i in range(3):
    current_max = max(all_elves_calories) 
    top_3_elves.append(current_max)
    all_elves_calories.remove(current_max)

print(sum(top_3_elves))
