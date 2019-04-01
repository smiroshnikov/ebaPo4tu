import re

# pattern = '(https?:[^>]*)\"'
# p = re.compile(pattern)

# myString = 'ink found <a href="http://bit.ly/1m8CG1I">Security</a>'
# myString = 'ink found <a> http://bit.ly/1m8CG1I </a>'

#
# m = p.findall(myString)
#
# print(m)


def pukan_bombit(url):
    # pattern = '(https?:[^>]*)\"'
    pattern = "(https?:[^>]*)\'"

    p = re.compile(pattern)
    url = p.findall(url)
    return url


myString = 'ink found <a href="https://www.suka.com/security/">Security</a>! <a>href="http://google.com"</a> <a> "http://bit.ly/1m8CG1I" </a>'
ms = 'https://www.guardicore.com/infectionmonkey/'

print(pukan_bombit(myString))
print(pukan_bombit(ms))

if pukan_bombit(ms):
    print("Link")
else:
    print("not link")