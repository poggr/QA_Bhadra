#if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")

#if else statement
if age <= 12:
    print("Child")
else: 
    print("Not a child")

#if elif else
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1>num2:
    print("num1 is greater than num2")
elif num1==num2:
    print("num1 is equal to num2")
else:
    print("num1 is less than num2")