import re

file = open()
result = re.findall(r".*a.*b$", file.read())
print(result)