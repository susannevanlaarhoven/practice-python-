# Write your code here :-)
num = int(input("Please enter a number: "))
lst = range(1, (num + 1))
result = []
for i in lst:
    if num % i == 0:
        result.append(i)

print(result)
