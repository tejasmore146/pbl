from PyPDF2 import PdfReader
import re


def extract(file, page_no):
    '''
    file: input pdf file
    page_no: the page number that you want to scrape
    makes a file.txt which has all the raw scraped data
    '''
    reader = PdfReader(file)
    page = reader.pages[int(page_no)]

    # Open a file in write mode
    with open('file.txt', 'w') as f:
        f.write(page.extract_text())


def remove_header_footer(file):
    '''
    removes the top and bottom irrelevant text
    aka crops the pdf file
    '''
    # Open the file for reading
    with open(file, 'r') as f:
        content = f.read()

    # Define the regular expression patterns to match the strings
    pattern1 = r"P\nrProvisional Allotment List of CAP Round -III for the Admission to the First Year Under Graduate \nTechnical Courses in Engineering and Technology \(4 Years \) &\nMaster of Engineering and Technology \(Integrated 5 Years \) Admissions A \.Y\. 2022-23State Common Entrance Test CellGovernment of Maharashtra\n?"
    pattern2 = r"Legends for SeatType : H-Home University, O-Other than Home University, S-State Level, G-General, L-Ladies, AI-All India\n\* Green Color indicates Betterment in Choice Code , @ Blue Color indicates Betterment in Seat Type ,\nRed Color indicates No Change ,  \^ Gray Color indicates Admitted to Institute ,      &  Black Color indicates Newly Allotted\nMI-Minority Seats Allotted to Minority Candidates belonging to eligible Religious /Linguistic community\nMI-MH - Minority Seats Allotted to Non Minority Maharashtra Candidates , MI-AI - Minority Seats Allotted to Non Minority All India Candidates\nMerit No :  State General Merit No\. for Maharashtra Seats, All India Merit No\. for All India Seats"

    # Use the regular expression patterns to replace all occurrences of the strings with an empty string
    new_content = re.sub(pattern1, '', content, flags=re.MULTILINE | re.DOTALL)
    new_content = re.sub(pattern2, '', new_content)

    # Open the same file for writing and write the modified content
    with open('output.txt', 'w') as f:
        f.write(new_content)


def remove_seat_type(file):
    '''
    Deletes the candidate Seat Type file
    '''
    # Define the text to delete
    delete_patterns = [
        r'Seat Type Candidate\s+CategoryGender Name of the Candidate Application ID Sr.\s+No\.Merit\s+No\.Meri'
        # r'MHT-CET\s+Score'
        # new logic
    ]

    # Read the contents of the file
    with open(file, 'r') as f:
        file_contents = f.read()

    # Delete all occurrences of the target strings
    for pattern in delete_patterns:
        file_contents = re.sub(pattern, '', file_contents)

    # Write the modified contents back to the file
    with open('output.txt', 'w') as f:
        f.write(file_contents)


def fix_line_error(file, space_count):
    '''
    use space_count as 6 for first call, and 5 for second call
    6 is used for when the name is 3 character long, and 5 is used for when the name is 4 character long

    '''
    with open(file, "r") as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].count(" ") == int(space_count):
            current_line = lines[i].strip()
            next_line = lines[i+1].strip()

            # Converting the next_line to list
            next_line_list = next_line.split(" ")
            # pulling out the messed up gender from the line
            gender = next_line_list[-5][-1]
            # removing the extra gender character
            gender_name_last = next_line_list[-5]
            gender_name_last = gender_name_last[:-1]
            # updating the string, and inserting the gender
            next_line_list[-5] = gender_name_last
            next_line_list.insert(-4, gender)
            # convert the string_list to a string
            next_line = " ".join(map(str, next_line_list))

            joined_string = (current_line + " " + next_line)
            new_lines.append(joined_string)
            i += 2
        else:
            new_lines.append(lines[i].strip())
            i += 1

    with open("output.txt", "w") as f:
        f.write("\n".join(new_lines))


def remove_minority(file):

    # Define the regular expression pattern
    pattern = re.compile(r'Minority Seats')

    # Open the file for reading
    with open(file, 'r') as input_file:
        # Read the file line by line
        lines = input_file.readlines()

    # Open the file for writing
    with open('output.txt', 'w') as output_file:
        # Loop through the lines and write only those that don't match the pattern
        for line in lines:
            if not pattern.search(line):
                output_file.write(line)


def state_level_merge(file):

    # Open the file and read its contents
    with open(file, "r") as f:
        text = f.read()

    # Check if the file contains two consecutive lines with "State Level Seats"
    if re.search(r'State Level Seats\nState Level Seats', text):
        # If it does, replace the lines with "State Level Seats"
        merged_text = re.sub(r'State Level Seats\nState Level Seats', 'State Level Seats', text)
        # Write the merged text back to the file
        with open("output.txt", "w") as f:
            f.write(merged_text)


def mht_cet_merge(file):
    # Read the contents of the file
    with open(file, "r") as f:
        text = f.read()

    if re.search(r'MHT-CET \nScore', text):
        merged_text = re.sub(r'MHT-CET \nScore', 'MHT-CET Score', text)
        # Write the merged text back to the file
        with open("output.txt", "w") as f:
            f.write(merged_text)

def jee_main_merge(file):
    # Read the contents of the file
    with open(file, "r") as f:
        text = f.read()

    if re.search(r'JEE\(Main\) \nScore', text):
        merged_text = re.sub(r'JEE\(Main\) \nScore', 'JEE(Main) Score', text)
        # Write the merged text back to the file
        with open("output.txt", "w") as f:
            f.write(merged_text)