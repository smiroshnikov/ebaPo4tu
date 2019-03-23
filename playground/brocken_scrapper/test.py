import re

# s = 'This is my tweet check it out http://tinyurl.com/blah and http://blabla.com'
# x = re.findall(r'(https?://\S+)', s)
# print(x)
# s = 'ink found <a href="https://www.guardicore.com/security/">Security</a>! '
# x = re.findall(r'(https?://\S+)', s)
# print(x)

def is_valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)


print(is_valid_url("https://www.guardicore.com/alex/sergei").string)
# print(is_valid_url("https://www.guardicore.com/alex/sergei"))


# https://www.regextester.com/94502
# ms = "https://www.guardicore.com/alex/sergei"
# # urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', ms)
# urls = re.findall("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$", ms)
# urls = re.findall('^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$', ms)
# re.search()
# print(urls)

