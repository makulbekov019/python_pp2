#Write a Python program with builtin 
#function that accepts a string and calculate 
#the number of upper case letters and lower case 
#letters

def letters(y):
    upper=0
    lower=0
    for i in y:
        if(i.isupper()):
            upper+=1
        if(i.islower()):
            lower+=1
    print("number of uppercase letters of "+ y +" is "+str(upper))
    print("number of lowercase letters of "+ y +" is "+str(lower))
letters("A Lot Of Different WORDS")
letters("HI, my name is Yerdaulet")