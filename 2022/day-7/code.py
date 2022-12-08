data = [i.strip() for i in open("input.txt")]

# Use dictionaries where the key represents the directory
current_dir = ""
file_system_map = {}
ident = 0
for line in data:
    line_split = line.split(" ")
    
    if line_split[0] == "$":
        last_command = line_split

        if last_command[1] == "cd":

            if last_command[2] == "..":
                current_dir = file_system_map[current_dir]["backref"]
            else:
                last_dir = current_dir
                current_dir = last_command[2]

                if line_split[2] == "/":
                    file_system_map["/"] = {"backref": "", "contents": []}

                else:
                    for last_content in file_system_map[last_dir]["contents"]:
                        if f"{current_dir}-" in last_content[1] and last_content[0] == "dir":
                            file_system_map[last_content[1]] = {"backref": last_dir, "contents": []}
                            current_dir = last_content[1]

    else:
        if line_split[0] == "dir": # new bit
            line_split[1] = f"{line_split[1]}-{ident}" 
            file_system_map[current_dir]["contents"].append(line_split)

            #print(line_split[1])
            ident += 1
        else:
            # print(current_dir)
            file_system_map[current_dir]["contents"].append(line_split)


# print(file_system_map)


# calculate total directory sizes
def get_nested_directories_sizes(dir_name):
    info = file_system_map[dir_name]
    
    directory_size = 0
    for content in info["contents"]:
        if content[0] == "dir":
            directory_size += get_nested_directories_sizes(content[1])
        else:
            directory_size += int(content[0])

    return directory_size


directory_sizes_total = {}
for dir_name, info in file_system_map.items():
    directory_sizes_total[dir_name] = get_nested_directories_sizes(dir_name)

total_size = 0
for dir_name, dir_data in directory_sizes_total.items():
    if dir_data <= 100000:
        total_size += dir_data

# part 1
print(total_size)

total_disk_space = 70000000
required_to_remove = 30000000
min_size_of_file_to_del = abs(total_disk_space - directory_sizes_total["/"] - 30000000)

# sort the values first
sorted_directory_sizes_total = {k: v for k, v in sorted(directory_sizes_total.items(), key=lambda item: item[1])}

directory_to_delete_size = 0
for directory, size in sorted_directory_sizes_total.items():
    if size >= min_size_of_file_to_del:
        directory_to_delete_size = size
        break

# part 2
print(directory_to_delete_size)

# use the os module to create full paths
# use startswith()
