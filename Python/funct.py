#python function
'''
function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

Syntax:
def function_name(parameters):
    statement(s)
    return value
'''

# def print_statement():
#     print("Hello World")
#     print("Hello Hello")
#     print("Good Morning")

# print_statement()  # calling the function

#Built-in functions are the functions that are already defined in Python. You can use these functions without defining them. Some of the built-in functions are len(), sum(), max(), min(), etc.
from unittest import result


# print(len("Hello World"))  # calling the built-in function len() to get the length of the string
# print(sum(12,34))  # calling the built-in function sum() to get the sum of two numbers


#user defined functions are the functions that are defined by the user. You can define your own functions using the def keyword. You can also pass parameters to the function and return values from the function.

num1=12
num2=13

def sum(num1,num2):
    result= num1+num2
    print("The sum of 2 numbers is:",result)


def sum(x,y):
    result= x+y
    return result
sum(14,89)


#Function with input() function
def sum():
    numb1=int(input("Enter the first number: "))
    numb2=int(input("Enter the second number: "))
    result= numb1+numb2
    print("The sum of 2 numbers is:",result)

sum()

