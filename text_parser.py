# lst = ['93', '109699', 'EN22248961', 'JAMODKAR', 'SANDEEP',
#        'UDHAV', 'M', 'NT', '1', '(NT-B)$', '*', 'GNT1O', '19.4998540']

string = "101 121524 EN22233230 THAKUR HIMANSHU PRAVEEN KUMAR M OPEN ^ DEFOPENS 2.1470211"
lst = string.split(" ")


def compress_list(lst):

    # Find the index of the first occurrence of "M" or "F"
    mf_index = None
    for i in range(len(lst)):
        if lst[i] == "M" or lst[i] == "F":
            mf_index = i
            break

    # Find the index of the first occurrence of "~", "@", "^", "*" or "&"
    special_index = None
    for i in range(len(lst)):
        if lst[i] in ["~", "@", "^", "&", "*"]:
            special_index = i
            break

    # # Print mf_index and special_index
    # print("mf_index = ", mf_index)
    # print("special_index = ", special_index)

    # Join everything between the two types of data
    if mf_index is not None and special_index is not None and mf_index < special_index:
        lst[mf_index +
            1:special_index] = [''.join(lst[mf_index+1:special_index])]

    # Join the name
    if mf_index is not None:
        lst[3:mf_index] = [' '.join(lst[3:mf_index])]

    return lst


lst = compress_list(lst)


def strip_strings(lst):
    return list(map(str.strip, lst))


print(strip_strings(lst))
