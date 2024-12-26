# Prompt user to enter a positive integer
n = int(input("Enter a positive integer: "))

# Declare variable and set it to 0
total = 0

# Add integers in for loop.  Process range of 1 through n+1.  Increment total by one in each increment.
# For every i in range 1 - n+1, increment total by 1
for i in range(1, n+1):
       total += i

# Print the total.  Convert digits to strings using str function
print("The sum of numbers from 1 to " + str(n) + " is " + str(total))