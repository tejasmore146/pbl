import re

# Define the regular expression pattern
pattern = r'^\s*(\d+)\s+([A-Z\d\s]+)\s+(\S+)\s*\n\s*([A-Z\d\s]+)\s+(\S+)\s*$'

# Test string
text = ' 13 82534 EN22153130 CHOUDHARY CHANDAN\nUPENDRAM OPEN ^ GOPENH 48.1419882'

# Check if the text matches the pattern and extract the components
match = re.match(pattern, text, flags=re.MULTILINE)
if match:
    # Extract the components
    number1 = match.group(1)
    string_sequence1 = match.group(2)
    measurement1 = match.group(3)
    string_sequence2 = match.group(4)
    number2 = match.group(5)
    
    # Concatenate the components into a single line
    new_text = f"{number1} {string_sequence1} {measurement1} {string_sequence2} {number2}"
    
    print(f"Original text:\n{text}")
    print(f"\nNew text:\n{new_text}")
else:
    print("No match found.")
