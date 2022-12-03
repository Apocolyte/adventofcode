data = [f.strip() for f in open("input.txt")]
get_value = {char: index+1 for index, char in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}

all_values = []
for backpack in data:
    first_compartment = backpack[:int(len(backpack)/2)]
    second_compartment = backpack[int(len(backpack)/2):]

    both_compartments_char = "" 
    for char in first_compartment:
        if char in second_compartment:
            both_compartments_char = char

    all_values.append(get_value[both_compartments_char])

# part 1
# print(sum(all_values))

grouped_backpacks = []
group = []
for index, backpack in enumerate(data):
    if index % 3 == 2:
        group.append(backpack)
        grouped_backpacks.append(group)
        group = []
    else:
        group.append(backpack)

all_values = []
all_elves_char = ""
for group in grouped_backpacks:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            all_elves_char = char
    
    all_values.append(get_value[all_elves_char])

# part 2
print(sum(all_values))

# Possible improvements:
# - Use set intesections instead of for loops (since only uniqueness is needed, not index)
# - While loop instead of modulo for assigning groups
