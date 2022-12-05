class Code:

    def __init__(self):
        self.data = [f for f in open("input.txt")]
        self.columns = 9

        self.crates = self.build_crates_dict()

    def build_crates_dict(self):
        crates = {i: [] for i in range(1, self.columns+1)}
        operations_starting_line = 0
        for i, line in enumerate(self.data):
            if "[" not in line:
                self.operations_starting_line = i + 2
                break
            else:
                for column in crates.keys():
                    if line[4*column - 3] != " ":
                        crates[column].append(line[4*column - 3])

        for key in crates.keys():
            crates[key] = list(reversed(crates[key]))

        return crates

    def part1(self):
        # create local crates dict to keep original
        crates = self.crates
        for operation in self.data[self.operations_starting_line:]:
            operation_magnituedes = list(map(int, operation.replace("move", "").replace("from", "").replace("to", "").strip().split("  ")))
            operation = {"move": operation_magnituedes[0], "from": operation_magnituedes[1], "to": operation_magnituedes[2]}

            for number in range(operation["move"]):
                # add the new crate
                crates[operation["to"]].append(crates[operation["from"]][-1])
                # remove previous location
                del crates[operation["from"]][-1]


        top_crates_string = ""
        for values in crates.values():
            top_crates_string += values[-1]

        return top_crates_string

    def part2(self):
        # create local crates dict to keep original
        crates = self.crates
        for operation in self.data[self.operations_starting_line:]:
            operation_magnituedes = list(map(int, operation.replace("move", "").replace("from", "").replace("to", "").strip().split("  ")))
            operation = {"move": operation_magnituedes[0], "from": operation_magnituedes[1], "to": operation_magnituedes[2]}

            crates[operation["to"]].extend(crates[operation["from"]][-operation["move"]:])
            del crates[operation["from"]][-operation["move"]:]

        top_crates_string = ""
        for values in crates.values():
            top_crates_string += values[-1]

        return top_crates_string

code = Code()
print(code.part1())
print(code.part2())

# Improvements
# Parsing input:
# 2d matrix, determine the indecies with the column numbers, and build from that
# Or just use vim macros
# Use regex for parsing operations (get more familiar with python regex)

# List removing/appending:
# deque from collections module is preferreed

# String output production:
# use x = "".join([i for i...]) for oneliner
