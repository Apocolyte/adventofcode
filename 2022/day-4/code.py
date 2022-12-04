data = [i.strip().split(",") for i in open("input.txt")]

full_ranges = []
for i, pair in enumerate(data):

    pair_ranges = []
    for j, single in enumerate(pair):
        single_range = [int(x) for x in single.split("-")]
        single_range_list = list(range(single_range[0], single_range[1]+1))

        pair_ranges.append(single_range_list)

    full_ranges.append(pair_ranges)

number = 0
for i in full_ranges:
    # print(i)

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

# sets unnecessary in this case, check for lowest and max values instead
# poor and confusing input parsing
