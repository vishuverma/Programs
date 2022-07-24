number = int(input("Enter the number:?\n"))
num = number
b = len(str(number))
sum1 = 0
while number!=0:
    r = number%10
    sum1 = sum1+(r**b)
    number = number//10
    
if num == sum1:
    print("The given number",num,"is a Armstrong number")
    
else:
     print("The given number",num,"is not a Armstrong number")