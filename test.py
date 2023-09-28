import random

# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Read all the lines from the input file
try:
    with open("random_numbers.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("The file 'random_numbers.txt' does not exist.")
    exit(1)

# Select a random line from the list of lines
random_line = random.choice(lines).strip()

# Check if the random number is a palindrome
if len(random_line) == 5 and random_line.isdigit():
    if is_palindrome(random_line):
        result = f"{random_line} is a palindrome."
    else:
        result = f"{random_line} is not a palindrome."
else:
    result = f"{random_line} is not a valid 5-digit number."

# Write the result to the log file
with open("log.txt", "a") as log_file:
    log_file.write(result + "\n")

print(result)
