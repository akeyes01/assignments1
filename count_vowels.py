# Prompt user to enter a string of text
sentence = input("Enter a sentence: ")

# Make all the letters in the string lowercase
sentence = sentence.lower()

# Set  count variable to 021
vowel_count = 0

# For every character (variable char) in string sentence, test (conditional if)
# if char is a vowel (aeiou).  If character (char) is a vowel
# increment variable vowel_count by 1.
for char in sentence:
       if char in "aeiou":
           vowel_count += 1

# Return print string statement with variable vowel_count.
print("The total number of vowels in your sentence is:", vowel_count)