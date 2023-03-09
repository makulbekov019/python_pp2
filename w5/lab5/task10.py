#
#CamelCase
#to 
#snake_case

import re
example="HiIAmYerdaulet."
x=re.findall('[A-Z][a-z]*',example)
result='_'.join(i.lower() for i in x)
print(result)
