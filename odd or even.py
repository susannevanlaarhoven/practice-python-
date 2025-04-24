# Write your code here :-)
num = int(input("Enter a number: "))
check = int(input("A number to divide by, please: "))
a = num % 2
b = num % 4
c = num % check
if b == 0:
    print(num, "can be divided by 4")
elif a == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
if c == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "doesn't divide evenly by",check,". There's a remainder of " + str(c))
