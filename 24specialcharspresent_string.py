import re
str1 = "welcome@@2To%%Python**Programming@!!^%%@$"
str2 = "Welcome to Python Programming"

# http://www.urlregex.com/
# [@_!#$%^&*()<>?/|}{~:]
regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')

if regex.search(str2) == None :
    print("No Special characters present in a string")
else:
    print("String contains special characters")