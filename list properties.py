# Write your code here :-)
import random
a = random.sample(range(1, 20),10)
b = random.sample(range(1, 20),10)
result = []
print(a)
print(b)
for num in a:
    if not num in b: result.append(num)
for num in b:
    if not num in a:
        if not num in result:
            result.append(num)
result.sort()
print(result)
