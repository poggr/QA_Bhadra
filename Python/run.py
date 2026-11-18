import modules

modules.Hello()
modules.print_name()
modules.print_age()
print(modules.name)
print(modules.age)


'''
from module_name import function_name

from modules import * (for imporitng all the modules)
'''

# from modules import Hello,age
# Hello()
# print(age)


#import with ailias
'''
import modules as md
md.Hello()

from modules import print_name as pn
pn()
'''

#dir to find out what functions are there
# import math
# print(dir(math))
# print(math.sqrt(25))
# print(math.pi)
# print(math.gcd(12,56))

# from math import pi, pow
# print(pi)
# print(pow(2,3))


#Random module
'''
import random
age = random.randint(1,200) #random number from 1-200 is given by randint
print(age)
'''

#importing using choice and choices
# import random
# usernames = ["sachin", "ram", "Hari"]
# print(random.choice(usernames))
# print(random.choices(usernames,k=2))

