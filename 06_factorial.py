def factorial(n):
    f=1
    for i in range(1,n+1):
      f*=i
    return f

# Read input and print result
num = int(input())
print(str(num) + "! = " + str(factorial(num)))
