"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32)

# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
number_1 = 64
number_2 = 32
print(number_1 + number_2)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
full_name = "Mario Abi Rached"
age = 23
studies = "Visual Effects"

print("Hello, I'm " + full_name + ", I'm currently " + str(age) + " years old and I decided to study " + studies + " in 2020.")

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sentence = "This is my first Python program"
print(len(sentence))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
value_1 = (1920 * 110 / 100)
value_2 = (1080 * 110 / 100)
print("The 10% overscan of 1920 is " + str(value_1) + ", and the 1080 is " + str(value_2) + ".")