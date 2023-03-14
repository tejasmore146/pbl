line1 = " 13 82534 EN22153130 CHOUDHARY CHANDAN "
line2 = "UPENDRAM OPEN ^ GOPENH 48.1419882"
# now only need to figure out the code to detect the two lines and join them


string = " 13 82534 EN22153130 CHOUDHARY CHANDAN \nUPENDRAM OPEN ^ GOPENH 48.1419882"
string_list = string.split(" ")
print(string_list)
# pulling out the messed up gender from the line
gender = string_list[-5][-1]
# removing the extra gender character
gender_name3 = string_list[-5]
gender_name3 = gender_name3[:-1]
# updating the string, and inserting the gender
string_list[-5] = gender_name3
string_list.insert(-4, gender)
string_list.append(" ")
# remove the new line character
new_line_name3 = string_list[-7]
new_line_name3 = new_line_name3[1:]
print(new_line_name3)
string_list[-7] = new_line_name3
# convert the string_list to a string
string = " ".join(map(str, string_list))
print(string_list)
print(string)
