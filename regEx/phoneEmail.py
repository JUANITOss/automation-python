#! python 3

import re, subprocess

# Function to copy text to clipboard
def copy_to_clipboard(text):
    process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
    process.communicate(input=text.encode('utf-8'))

# Function to paste text from clipboard
def paste_from_clipboard():
    process = subprocess.Popen(['xclip', '-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode('utf-8')

# Create RegEx for email
myEmailRegEx = re.compile(r'[^\s@]+@[^\s@]+\.[a-zA-Z]{3}(\.[a-zA-Z]{2})?')

emailRegEx = re.compile(r'''
(
[^\s@]+          # Name
@                # @
[^\s@]+          # Domain
\.[a-zA-Z]{3}    # 
(\.[a-zA-Z]{2})? # Country-specific
)
''', re.VERBOSE)

# Create RegEx for phone
phoneRegEx = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?         # Area Code
(\s|-)                          # Separator                        
\d\d\d                          # Digits
-                               # Separator
\d\d\d\d                        # Digits
(((ext(\.)?\s)|(x))(\d{2,5}))?  # Extension       
)
''', re.VERBOSE)

# Get text of clipboard
text = paste_from_clipboard()

# Extract email phone & name from text
extPhone = phoneRegEx.findall(text)
extMail = emailRegEx.findall(text)

allPhones = [pn[0] for pn in extPhone]
allMails = [ml[0] for ml in extMail]

# Copy extracted phone/email to clipboard

txt = "\n\n".join([f"Mail: {mail}\nPhone: {phone}" for mail, phone in zip(allPhones, allMails)])
    
copy_to_clipboard(txt)


# Text copied

# Thomas Ford kppilspnbx1@live.com 805-324-5310
# Spencer Mccarty smccarty19@outlook.com 509-735-5037
# Anton Zimmerman antonz@icloud.com 479-370-6824
# Jeffry Jacobson jjacobson@sbcglobal.net 517-610-2685
# Joaquin Merrill jmerrill@aol.com 601-571-9567
# Waylon Holder wholder34@me.com 811-230-2024
# Federico Pickett yiafpwdr98@aol.com 800-514-7080
# Milo Harper mharper@aol.com 615-208-3677
# Andy Owen owe3619@comcast.net 957-802-8298
# Kendall Mcmillan kmcmillan11@gmail.com 649-808-2639
# Cortez Underwood cunderwood10@att.net 641-800-1884
# Robin Michael rmichael63@live.com 284-474-5209
# Orville Wade rfdct61@msn.com 336-422-7446
# Pete Becker pbecker9@verizon.net 211-825-1882

# Result

print(txt)

