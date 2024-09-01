import re

secretNames = re.compile(r'Agent \w+', re.I)

msg = 'Agent bob messed with agent andy and died by hand of agent roberto'

print(secretNames.sub('[REDACTED]', msg))
