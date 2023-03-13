import re

# Define the text to delete
delete_patterns = [
    r'Seat Type Candidate\s+CategoryGender Name of the Candidate Application ID Sr.\s+No\.Merit\s+No\.Meri',
    r'MHT-CET\s+Score'
]

# Read the contents of the file
with open('file2.txt', 'r') as f:
    file_contents = f.read()

# Delete all occurrences of the target strings
for pattern in delete_patterns:
    file_contents = re.sub(pattern, '', file_contents)

# Write the modified contents back to the file
with open('file3.txt', 'w') as f:
    f.write(file_contents)
