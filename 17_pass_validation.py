import re
passs=input("Enter a password:-")
x=True
while(True):
    if(len(passs)<6):
        print("Pass is to short")
        break
    elif not (re.search("[A-Z]",passs)):
        print("Add Upper Case")
        break
    elif not (re.search("[a-z]",passs)):
        print("Add Lower CAse")
        break
    elif not re.search("[@#$]",passs):
        print("Add Special character ")
        break
    elif not re.search("[0-9]",passs):
        print("Add NUmber")
        break
    elif re.search("\s",passs):
        break
    else:
        print("valid Pass")
        break
        
