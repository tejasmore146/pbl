import re

# Open the file for reading
with open('file.txt', 'r') as file:
    # Read the contents of the file
    text = file.read()

# Remove the specified text using regex
text = re.sub(r"Legends for SeatType :.*Merit No :.*\n", "", text)

# Open the file for writing and write the modified text to it
with open('file2.txt', 'w') as file:
    file.write(text)
