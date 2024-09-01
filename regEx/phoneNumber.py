import re

msg = "jasjdkgkasg 123-654-7809 jasdkgajksgdjasg"

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

print(phoneNumRegex.findall(msg))

mo = phoneNumRegex.search(msg)

print(mo.group(3))