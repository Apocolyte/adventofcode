# rucksack has two compartments
# items of type need to go in one of the two
# exactly one item type per rucksack is wrong
# equal number of items between compartments
# First half representes compartment 1

# lowercase have priorities 1-26, upper 27-52

data = [f.strip() for f in open("input.txt")]

# print(data[0][:int(len(data[0])/2)])
#print(data[0][int(len(data[0])/2):])

get_value = {char: index+1 for index, char in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}


all_values = []
for backpack in data:
    first_compartment = backpack[:int(len(backpack)/2)]
    second_compartment = backpack[int(len(backpack)/2):]

    both_compartments_char = "" 
    for char in first_compartment:
        if char in second_compartment:
            both_compartments_char = char


    # print(both_compartments_char)
    all_values.append(get_value[both_compartments_char])

# part 1
# print(sum(all_values))

# item carried by all 3 is the group
grouped_backpacks = []
group = []
for index, backpack in enumerate(data):
    if index % 3 == 2:
        group.append(backpack)
        grouped_backpacks.append(group)
        group = []
    else:
        group.append(backpack)

# print(grouped_backpacks)

all_values = []
all_elves_char = ""
for group in grouped_backpacks:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            all_elves_char = char
    
    all_values.append(get_value[all_elves_char])

print(sum(all_values))

