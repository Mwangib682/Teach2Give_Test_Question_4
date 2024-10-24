"""
QUESTION 4: Write a program that takes an integer as input and returns an integer with 
reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.
"""


#defining a new function named reverse_integer
def reverse_integer(n):
    # Converting the integer to a string and handle negative numbers
    is_negative = n < 0
    n_str = str(abs(n))  # Converting the absolute value of the integer to a string

    # Reversing the string and converting it back to an integer
    reversed_str = n_str[::-1]
    reversed_int = int(reversed_str)

    # Restoring the negative sign if the original number was negative
    if is_negative:
        reversed_int = -reversed_int

    return reversed_int


# Testing cases
print(reverse_integer(328903467))  # Output: 764309823
print(reverse_integer(-56))  # Output: -65
print(reverse_integer(-90))  # Output: -9
print(reverse_integer(91))  # Output: 19

# Accepting input from the user
user_input = int(input("Enter an integer: "))
result = reverse_integer(user_input)
print("Reversed Integer:", result)





"""
My Pycharm results for the above written code are as follows:
C:\Users\hp\PycharmProjects\pythonProject2\.venv\Scripts\python.exe "C:\Users\hp\PycharmProjects\pythonProject2\QUESTION 4.py" 
764309823
-65
-9
19
Enter an integer: 450978
Reversed Integer: 879054

Process finished with exit code 0
"""