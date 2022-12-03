data = [f.strip() for f in open("input.txt")]
get_value = {char: index+1 for index, char in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}

all_values = []
for rucksack in data:
    first_compartment = rucksack[:int(len(rucksack)/2)]
    second_compartment = rucksack[int(len(rucksack)/2):]

    both_compartments_char = "" 
    for char in first_compartment:
        if char in second_compartment:
            both_compartments_char = char

    all_values.append(get_value[both_compartments_char])

# part 1
# print(sum(all_values))

grouped_rucksacks = []
group = []
for index, rucksack in enumerate(data):
    if index % 3 == 2:
        group.append(rucksack)
        grouped_rucksacks.append(group)
        group = []
    else:
        group.append(rucksack)

all_values = []
all_elves_char = ""
for group in grouped_rucksacks:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            all_elves_char = char
    
    all_values.append(get_value[all_elves_char])

# part 2
print(sum(all_values))

# Possible improvements:
# - Set intesections instead of for loops
# - While loop instead of modulo for assigning groups
# - Integar division when splitting lines
