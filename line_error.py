string = " 13 82534 EN22153130 CHOUDHARY CHANDAN \nUPENDRAM OPEN ^ GOPENH 48.1419882"
string_list = string.split(" ")
print(string_list)
gender = string_list[-5][-1]
name_3 = string_list[-5]
name_3 = name_3[:-1]
string_list[-5] = name_3
string_list.insert(-4, gender)
string = " ".join(map(str, string_list))
print(string)