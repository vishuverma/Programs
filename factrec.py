def factorial(n):
    return 1 if n==0 or n==1 else n*factorial(n-1)

num = int(input("enter the number:?\n"))
print("The factorial of {} is{}".format(num,factorial(num)))