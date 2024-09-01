import re

msg = "batmobile batman batalt"

batRegex = re.compile(r'bat(mobile|man|arang|woman)')

mo = batRegex.search(msg)

print(mo.group())