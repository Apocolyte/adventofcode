full_ranges_intermediate = [list(map(int, i.strip().replace(",", "-").split("-"))) for i in open("input.txt")]
full_ranges = [[list(range(i[0],i[1])), list(range(i[2], i[3]))] for i in full_ranges_intermediate]

number = 0
for i in full_ranges:
    if sorted(i[0]) == sorted(list(set(i[0]) & set(i[1]))) or sorted(i[1]) == sorted(list(set(i[0]) & set(i[1]))):
        number += 1

# part 1
print(number)

number = 0
for i in full_ranges:
    if len(list(set(i[0]) & set(i[1]))) > 0:
        number += 1

# part 2
print(number)
