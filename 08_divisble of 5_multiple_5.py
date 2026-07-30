a=int(input("Enter starting number: "))
b=int(input("Enter end number: "))
num=[]
for i in range(a,b+1):
    if i%7==0 and i%5==0:
        num.append(str(i))
print(','.join(num))
