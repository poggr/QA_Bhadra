#Third party modules
'''
pip install module_name

pip show module_name

'''

import faker
from faker import Faker

fake = Faker()

print(fake.name())
print(fake.name_nonbinary())
print(fake.email())



