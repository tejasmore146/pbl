lst = ['93', '109699', 'EN22248961', 'JAMODKAR', 'SANDEEP',
       'UDHAV', 'M', 'NT', '1', '(NT-B)$', '*', 'GNT1O', '19.4998540']


def get_category(lst):
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

    # Print mf_index and special_index
    print("mf_index = ", mf_index)
    print("special_index = ", special_index)

    # Join everything between the two types of data
    # if mf_index is not None and special_index is not None:
    #     if mf_index < special_index:
    #         category = " ".join(lst[mf_index+1:special_index])
    #     else:
    #         category = " ".join(lst[special_index+1:mf_index])
    #     print(category)
    # else:
    #     print("Could not find both types of data in the list.")

    if mf_index is not None and special_index is not None:
        if mf_index < special_index:
            category = " ".join(lst[mf_index+1:special_index])
        else:
            category = " ".join(lst[special_index+1:mf_index])

        return category



print(get_category(lst))