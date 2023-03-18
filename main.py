from all_code import *
import os

if os.path.exists("output.txt"):
    os.remove("output.txt")

file = "CAPR-III_6207.pdf"

extract(file, 4)
file = "file.txt"
remove_header_footer(file)
file = "output.txt"
remove_seat_type(file)
remove_minority(file)
fix_line_error(file, 6)
state_level_merge(file)
try:
    fix_line_error(file, 5)
except:
    pass
