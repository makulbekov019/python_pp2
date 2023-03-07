import re
with open() as file:
    content= file.read()
result=re.findall("^[A-Z][a-z]+",content)
print(result)