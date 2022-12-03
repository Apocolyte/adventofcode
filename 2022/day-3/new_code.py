class Code:
    data = [f.strip() for f in open("input.txt")]
    get_value = {char: index+1 for index, char in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}

    def part1(self):
        total = 0
        for rucksack in Code.data:
            first_compartment = rucksack[:len(rucksack) // 2]
            second_compartment = rucksack[len(rucksack) // 2:]

            both_compartments_char = list(set(first_compartment) & set(second_compartment))[0]
            total += Code.get_value[both_compartments_char]

        return total

    def part2(self):
        total = 0
        for i in range(0, len(Code.data), 3):
            all_elves_char = list(set(Code.data[i]) & set(Code.data[i+1]) & set(Code.data[i+2]))[0]
            total += Code.get_value[all_elves_char]

        return total

code = Code()
print(code.part1())
print(code.part2())
