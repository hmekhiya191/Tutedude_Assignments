# Tutedude Assignment-2 Task-3

# Open a file 
file = open("myfile.txt", "w")

# write
file.write("Hello, I'm Harsh.\n")
file.write("I am learning Devops from tutedude.\n")
file.write("File handling is very useful in Python.\n")

file.close()

# read 
file = open("myfile.txt", "r")

content = file.read()

print("\n--- File Content ---")
print(content)


file.close()
