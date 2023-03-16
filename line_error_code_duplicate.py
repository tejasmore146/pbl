with open("file4.txt", "r") as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    if lines[i].count(" ") == 5:
        current_line = lines[i].strip()
        next_line = lines[i+1].strip()

        # Converting the next_line to list
        next_line_list = next_line.split(" ")
        # pulling out the messed up gender from the line
        gender = next_line_list[-5][-1]
        # removing the extra gender character
        gender_name3 = next_line_list[-5]
        gender_name3 = gender_name3[:-1]
        # updating the string, and inserting the gender
        next_line_list[-5] = gender_name3
        next_line_list.insert(-4, gender)
        # convert the string_list to a string
        next_line = " ".join(map(str, next_line_list))


        joined_string = (current_line + " " + next_line)
        new_lines.append(joined_string)
        i += 2
    else:
        new_lines.append(lines[i].strip())
        i += 1

with open("file5.txt", "w") as f:
    f.write("\n".join(new_lines))
