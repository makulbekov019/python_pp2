
import re

file = open()
result = re.findall("[a-z]+_[a-z]+", file.read())
print(result)
