import re

file = open()
result = re.findall(".*a.*b.*b.*b?.*", file.read())
print(result)