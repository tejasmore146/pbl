from all_code import *
import os

if os.path.exists("output.txt"):
    os.remove("output.txt")

file = "CAPR-III_6207.pdf"

extract(file, 17)
file = "file.txt"
remove_header_footer(file)
file = "output.txt"
remove_seat_type(file)
remove_minority(file)
state_level_merge(file)
mht_cet_merge(file)
jee_main_merge(file)
fix_line_error(file, 6)
try:
    fix_line_error(file, 5)
except:
    pass
