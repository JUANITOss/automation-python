import re

msg = "batmobile batman batalt"

batRegex = re.compile(r'bat(mobile|man|arang|woman)')

mo = batRegex.findall(msg)

print(mo)

batRegex2 = re.compile(r'bat(wo)?man')

msg2 = 'The adventures of batwoman'

mo2 = batRegex2.search(msg2)

print(mo2.group())
