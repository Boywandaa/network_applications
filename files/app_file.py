

# 1. Writing to a file (creates file if not exists, overwrites if it does)
with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new file.\n")

# 2. Appending to a file (creates file if not exists, adds to the end)
with open('example.txt', 'a') as file:
    file.write("Adding another line.\n")

# 3. Reading the entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Entire content:\n", content)

# 4. Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print("Line:", line.strip())  # .strip() removes newline character

# 5. Reading into a list of lines
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("Lines as list:", lines)

# 6. Writing a list of lines
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('lines.txt', 'w') as file:
    file.writelines(lines_to_write)

# 7. Using `with` automatically closes files
# Manual method (not recommended, but useful to know):
file = open('example.txt', 'r')
try:
    data = file.read()
    print("Manual read:", data)
finally:
    file.close()

# 8. Working with file paths (recommended)
import os
from pathlib import Path

# Using os
filename = os.path.join("folder", "myfile.txt")

# Using pathlib (modern way)
path = Path("folder") / "myfile.txt"

# Ensure folder exists before writing
os.makedirs("folder", exist_ok=True)
with open(filename, 'w') as file:
    file.write("Pathlib + os write example.")

# 9. Checking if a file exists
if os.path.exists('example.txt'):
    print("example.txt exists!")

# 10. Deleting a file
# os.remove('example.txt')  # Uncomment to delete the file

# 11. File modes
"""
'r'  - Read (default)
'w'  - Write (truncate if exists)
'a'  - Append
'x'  - Create (fail if exists)
'b'  - Binary mode (e.g. 'rb', 'wb')
't'  - Text mode (default, e.g. 'rt', 'wt')
'+'' - Read/write (e.g. 'r+', 'w+')
"""

# === End of File I/O Reference ===
