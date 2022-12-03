
class Code:
    data = [f.strip() for f in open("input.txt")]
    get_value = {char: index+1 for index, char in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}

    def part1(self):
        all_values = []
        for rucksack in Code.data:
            first_compartment = rucksack[:len(rucksack) // 2]
            second_compartment = rucksack[len(rucksack) // 2:]

            both_compartments_char = list(set(first_compartment).intersection(second_compartment))[0]

            all_values.append(Code.get_value[both_compartments_char])

        return sum(all_values)

    def part2(self):
        grouped_rucksacks = []
        for i in range(0, len(Code.data), 3):
            grouped_rucksacks.append([Code.data[i], Code.data[i+1], Code.data[i+2]])

        all_values = []
        for group in grouped_rucksacks:
            all_elves_char = list(set(group[0]).intersection(group[1], group[2]))[0]
             
            all_values.append(Code.get_value[all_elves_char])

        return sum(all_values)

code = Code()
print(code.part1())
print(code.part2())
