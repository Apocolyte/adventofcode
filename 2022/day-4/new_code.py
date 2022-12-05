data = [f.strip().split(",") for f in open("input.txt")]
data_values = [[list(map(int, j.split("-"))) for j in i] for i in data]

number = 0
for pair in data_values:
    if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        number += 1
    elif pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        number += 1

# part 1
print(number)

for pair in data_values:
    if pair[0][0] <= pair[1][1] and pair
# number = 0
# for i in full_ranges:
#     if len(list(set(i[0]) & set(i[1]))) != 0:
#         number += 1
# 
# # part 2
# print(number)
