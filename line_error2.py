with open("file3.txt", "r") as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    if lines[i].count(" ") == 6:
        new_lines.append(lines[i].strip() + " " + lines[i+1].strip())
        i += 2
    else:
        new_lines.append(lines[i].strip())
        i += 1

with open("file4.txt", "w") as f:
    f.write("\n".join(new_lines))

# really ? sometimes the weirdest solutions seem to work, after two whole days of toiling, this solution worked
# though i did have to think out of the box, and it's 3 am while im making this commit
# I tried a lot of regex, and a lot of code that was supposed to do the work manually by converting it all to string and stuff
# but for that manual code to work, i had to detect the sequence
# then, by a random thought it occured, and i did NOT think it would work
# but well there you have it.
# I'd really love to give this assignment to some of my friends and see how they would approach this problem lmao

# Okay got happy too soon, the lines are combined but the gender value is still stuck to the name
# whatever, the code is understandable, will just fix it tomorrow
