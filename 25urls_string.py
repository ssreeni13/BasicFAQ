import re

str = "Im blogger at https://www.pavantestingtools.com/"
str = "My Profile: https://www.pavanonlinetrainings.com/about.html"

# http://www.urlregex.com/
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+

url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
print(url)
