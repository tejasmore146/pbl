lst = ['93', '109699', 'EN22248961', 'JAMODKAR', 'SANDEEP', 'UDHAV', 'M', 'NT', '1', '(NT-B)$', '*', 'GNT1O', '19.4998540']

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

# Join everything between the two types of data
if mf_index is not None and special_index is not None:
    if mf_index < special_index:
        result = " ".join(lst[mf_index+1:special_index])
    else:
        result = " ".join(lst[special_index+1:mf_index])
    print(result)
else:
    print("Could not find both types of data in the list.")
