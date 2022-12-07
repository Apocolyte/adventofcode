data = open("input.txt").readlines()[0]

packet_start = []
for i, char in enumerate(data[:-4]):
    if len(set(data[i:i+4])) == 4:
        packet_start.append(f"{data[i:i+4]}")
        break

# account for first marker offset
# part 1
print(data.index(packet_start[0])+4)


message_start = []
for i, char in enumerate(data[:-14]):
    if len(set(data[i:i+14])) == 14:
        message_start.append(f"{data[i:i+14]}")
        break

# part 2
print(data.index(message_start[0])+14)
