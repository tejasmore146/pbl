import re

# Open the file for reading
with open('file.txt', 'r') as f:
    content = f.read()

# Define the regular expression patterns to match the strings
pattern1 = r"P\nrProvisional Allotment List of CAP Round -III for the Admission to the First Year Under Graduate \nTechnical Courses in Engineering and Technology \(4 Years \) &\nMaster of Engineering and Technology \(Integrated 5 Years \) Admissions A \.Y\. 2022-23State Common Entrance Test CellGovernment of Maharashtra\n?"
pattern2 = r"Legends for SeatType : H-Home University, O-Other than Home University, S-State Level, G-General, L-Ladies, AI-All India\n\* Green Color indicates Betterment in Choice Code , @ Blue Color indicates Betterment in Seat Type ,\nRed Color indicates No Change ,  \^ Gray Color indicates Admitted to Institute ,      &  Black Color indicates Newly Allotted\nMI-Minority Seats Allotted to Minority Candidates belonging to eligible Religious /Linguistic community\nMI-MH - Minority Seats Allotted to Non Minority Maharashtra Candidates , MI-AI - Minority Seats Allotted to Non Minority All India Candidates\nMerit No :  State General Merit No\. for Maharashtra Seats, All India Merit No\. for All India Seats"

# Use the regular expression patterns to replace all occurrences of the strings with an empty string
new_content = re.sub(pattern1, '', content, flags=re.MULTILINE | re.DOTALL)
new_content = re.sub(pattern2, '', new_content)

# Open the same file for writing and write the modified content
with open('file2.txt', 'w') as f:
    f.write(new_content)
