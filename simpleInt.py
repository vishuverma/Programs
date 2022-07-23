def simple_I(p,t,r):
    si= (p*t*r)/100
    print("The simple intrest is:", si)
    return si

num = int(input("Enter the principle ammount:?\n"))
num2 = int(input("Enter the time period:?\n"))
num3 = int(input("Enter the rate of intrest:?\n"))

simple_I (num, num3, num2)
