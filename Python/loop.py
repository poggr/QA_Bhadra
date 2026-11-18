#for loop
'''
for variable in range():
    statement
'''
# for i in range(5):
#     print("Hello")
# n=4
# for i in range(0,n):
#     print(i)

'''
for i in range(1,11,2):
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(fruits)

usernames = ["Alice", "Bob", "Charlie"]
for users in usernames:
    print("The usernames are",users)
'''


#While loop repeatedly executes a block of code as long as the given condition remains true. When the condition becomes false, the line immediately after the loop in the program is executed.
'''
while condition:
    statement(s)
    control statement
'''

i= 1
while i<10:
    print(i)
    i=i+i

count=5
while count>1:
    print(count)
    count=count-1

print("Done")


cnt = 0
while (cnt< 3):
    cnt = cnt+1
    print("Hello")


# nested loop
for i in range(1, 4):
    for j in range(i):
        print(i, end=" ")
    print()