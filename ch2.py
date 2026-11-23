print("enter a number(numerator):")
numerator = int(input())
print("enter a number(denominator):")
denominator = int(input())
result = numerator % denominator
if result ==0:
    print("no. divisible")
else:
    print("no. not divisible")
