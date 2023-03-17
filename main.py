from all_code import *
import os

if os.path.exists("output.txt"):
    os.remove("output.txt")

file = "CAPR-III_6207.pdf"

extract(file, 5)
file = "file.txt"
remove_header_footer(file)
file = "output.txt"
remove_seat_type(file)
file = "output.txt"
fix_line_error(file, 6)
file = "output.txt"
fix_line_error(file, 5)
