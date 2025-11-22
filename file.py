# Writing to a file (creates a new file or overwrites if it exists)
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test.\n")
    file.write("This is the second line.\n")

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes extra newline


# Appending data
with open("sample.txt", "a") as file:
    file.write("Adding a third line.\n")


with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("First Line:", lines[0])
    print("Second Line:", lines[1])
 
 # Writing binary data (bytes) to a file
data = b"This is binary data."

with open("binary_file.bin", "wb") as file:  # 'wb' = write binary
    file.write(data)

print("Binary data written.")

