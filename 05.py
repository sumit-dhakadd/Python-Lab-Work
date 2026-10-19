import os
import sys

# Show the present directory
current_path = os.getcwd()
print("Current Directory:", current_path)

# Show directory contents
print("\nContents of Current Directory:")
items = os.scandir(".")
for entry in items:
    print(entry.name)

# Check and create workspace folder
folder = os.path.join(current_path, "workspace")

if os.path.isdir(folder):
    print("\nWorkspace folder already exists.")
else:
    os.makedirs(folder)
    print("\nWorkspace folder created.")

# Move into workspace
os.chdir(folder)
print("Current Directory:", os.getcwd())

# Write a message to the log file
filename = "system_log.txt"
message = "System utility executed successfully.\n"

with open(filename, "a") as f:
    f.write(message)

print("\nLog file created/updated:", filename)

# Find all text files
print("\nText Files:")
text_files = [name for name in os.listdir(".") if name.endswith(".txt")]

for name in text_files:
    print(name)

# Display log file data
print("\nLog File Content:")
with open(filename, "r") as f:
    print(f.read(), end="")

# Go back to the original directory
os.chdir(current_path)
print("\nReturned to:", os.getcwd())

# Print command-line arguments
print("\nCommand-line Arguments:")
for arg in sys.argv:
    print(arg)
