#Write a Python program to 
#insert spaces between words starting with capital letters.
import re

example="HiMyNameIsYerdaulet."
x=re.findall('[A-Z][a-z]*',example)
result=' '.join(x)
print(result)

