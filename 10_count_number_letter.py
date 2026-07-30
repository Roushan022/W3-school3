string=input("ENter a number")
Digit=0
Letter=0
for i in string:
    if i.isdigit():
        Digit +=1
    elif i.isalpha():
        Letter +=1
        
print("Letters ",Letter)
print("Digits ",Digit)
