import re

# line = "Cats are smarter than dogs"
# searchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

# if searchObj:
#     print "searchObj.group() : ", searchObj.group()
#     print "searchObj.group() : ", searchObj.group(1)
#     print "searchObj.group() : ", searchObj.group(2)
# else:
#     print "Nothing found!!"


## match vs searching
## match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string


## search and replace
## re.sub(pattern, repl, string, max=0)

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num