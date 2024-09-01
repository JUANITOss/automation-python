import re

message = 'juanchi@example.com.ar'

# First one I made, its bad Ik
# regMail = re.compile(r'^[^\s@]+@[^\s@]+\.[A-Za-z]+{3,}(\.[A-Za-z]{2,})?$')

regMail = re.compile(r'^[^\s@]+@[^\s@]+\.[a-zA-Z]{3,}(\.[a-zA-Z]{2,})?$')

mo = regMail.search(message)

print(mo.group())
