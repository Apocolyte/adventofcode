import numpy as np

data = [list(f.strip()) for f in open("input.txt")]
# reassign with integar values
data = np.array([[int(element) for element in row] for row in data])

first_column_length = len([f[0] for f in data])
first_row_length = len(data[0])

total_visible_trees = 0

# outer edge case
total_visible_trees += 2*(first_row_length - 2) + 2*first_column_length

data_transposed = data.transpose()
         
elements_checked = {f"{i},{j}": False for i, row in enumerate(data) for j, element in enumerate(row)}
for i, row in enumerate(data):
    if i == 0 or i+1 == len(data):
        continue

    for j, element in enumerate(row):
        if j == 0 or j+1 == len(data_transposed[j]):
            continue

        if (data[i,j] > data[i,:j]).all() or (data[i,j] > data[i,j+1:]).all():
            if elements_checked[f"{i},{j}"] == False:
                total_visible_trees += 1
                elements_checked[f"{i},{j}"] = True

        elif (data[i,j] > data[:i,j]).all() or (data[i,j] > data[i+1:,j]).all():
            if elements_checked[f"{i},{j}"] == False:
                total_visible_trees += 1
                elements_checked[f"{i},{j}"] = True

        # print(f"full: {data[:,j]}")
        # print(f"at {i}")
        # print(f"elem: {data[i,j]}\n")
# part 1
print(total_visible_trees)

scenic_scores = {f"{i},{j}": 0 for i, row in enumerate(data) for j, element in enumerate(row)}
for i, row in enumerate(data):
    for j, element in enumerate(row):

        left = 0
        if j != 0:
            for comp in np.flip(data[i,:j]):
                left += 1

                if data[i,j] <= comp:
                    break

        right = 0
        if j+1 != len(row):
            for comp in data[i,j+1:]:
                right += 1

                if data[i,j] <= comp:
                    break

        up = 0
        if i != 0:
            for comp in np.flip(data[:i,j]):
                up += 1

                if data[i,j] <= comp:
                    break

        down = 0
        if i+1 != len(data):
            for comp in data[i+1:,j]:
                down += 1
                if data[i,j] <= comp:
                    break

        scenic_scores[f"{i},{j}"] = up*down*left*right

# sort scenic scores
sorted_scenic_scores = {k: v for k, v in sorted(scenic_scores.items(), key=lambda item: item[1])}
# part 2
print(sorted_scenic_scores)
