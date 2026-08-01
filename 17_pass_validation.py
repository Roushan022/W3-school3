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

        
#without import re         
# password = input("Enter a password: ")
# upper = lower = digit = special = False
# space = False

# for ch in password:
#     if ch.isupper():
#         upper = True
#     elif ch.islower():
#         lower = True
#     elif ch.isdigit():
#         digit = True
#     elif ch in "@#$":
#         special = True
#     elif ch.isspace():
#         space = True

# if len(password) >= 6 and upper and lower and digit and special and not space:
#     print("Valid Password")
# else:
#     print("Invalid Password")
