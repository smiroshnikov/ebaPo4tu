import re

# s = 'This is my tweet check it out http://tinyurl.com/blah and http://blabla.com'
# x = re.findall(r'(https?://\S+)', s)
# print(x)
# s = 'ink found <a href="https://www.guardicore.com/security/">Security</a>! '
# x = re.findall(r'(https?://\S+)', s)
# print(x)

myString = 'ink found <a href="https://www.guardicore.com/security/">Security</a>! '
urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', myString)
print(urls)

