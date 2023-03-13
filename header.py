import re

# Open the file for reading
with open('file.txt', 'r') as f:
    content = f.read()

# Define the regular expression pattern to match the string and the new line character that follows it
pattern = r"P\nrProvisional Allotment List of CAP Round -III for the Admission to the First Year Under Graduate \nTechnical Courses in Engineering and Technology \(4 Years \) &\nMaster of Engineering and Technology \(Integrated 5 Years \) Admissions A \.Y\. 2022-23State Common Entrance Test CellGovernment of Maharashtra\n?"

# Use the regular expression to replace all occurrences of the pattern with an empty string
new_content = re.sub(pattern, '', content)

# Open the same file for writing and write the modified content
with open('file2.txt', 'w') as f:
    f.write(new_content)
