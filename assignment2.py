
while True: # While loop that runs indefinitely until user enters a number
    try:
        # Prompt user for a number
        first_number = float(input("Please enter a number: "))
        # Exit the loop once a number is provided
        break
    except ValueError:
        # Provide an error message if a non-numeric character is provided
        print("Invalid input. Please enter a number:")

while True: # While loop that runs indefinitely until user enters a second number
    try:
        # Prompt user for a second number.  Convert the string into a float.
        second_number = float(input("Please enter a second number: "))
        # Exit the loop once a number is provided
        break
    except ValueError:
        # Print an error message if a non-numeric character is provided.
        print("Invalid input. Please enter a number.")

# While loop that runs indefinitely until user enters a non-zero number
while second_number == 0:
    # Print error message if non-zero number is provided
    print("You cannot divide by 0.")
    second_number = input("Please enter another number: ")
    if second_number != 0:
        while True: # While loop that runs indefinitely until user enters a number
            try:
        # Prompt user for a second number.  Convert the string into a float.
                second_number = float(input("Please enter a number: "))
        # Exit the loop once a number is provided
                break
            except ValueError:
                # Print an error message if a non-numeric character is provided.
                print("Invalid input. Please enter a number.")
        second_number = float(second_number)

# Compute the sum of the user's two numbers
sum = first_number + second_number

# Print the sum of the user's two numbers
print("The sum of your two numbers is",  sum)

# Compute the difference of the user's two numbers
diff = first_number - second_number

# Print the difference of the user's two numbers
print("The difference of your two numbers is",  diff)

# Compute the product of the user's two numbers
prod = first_number * second_number

# Print the product of the user's two numbers
print("The product of your two numbers is", prod)

# Compute the first number divided by the second number
result = first_number / second_number    

# Print the result 
print(f"The result of your first number divided by your second number is {result:.2f}")
