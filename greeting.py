# Prompt user to enter their name
name = input("Enter your name: ")

# Print user name with greeting
print("Hello, " + name + "! Nice to meet you.")

# Count characters in name and assign to variable length_of_name
length_of_name = len(name)

# Print length of user's name using str function
print("Your name has " + str(length_of_name) + " characters.")

# Convert user's name to all caps using upper method
print("In uppercase, your name looks like: " + name.upper())