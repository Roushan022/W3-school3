a=int(input("ENter a number"))
b=int(input("Enter enf numebr"))
even=0
odd=0
for i in range(a,b+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)
