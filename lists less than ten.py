# Write your code here :-)
lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst2 = []
for x in lst1:
    if x < 5:
        print(x)
for x in lst1:
    if x < 5:
        lst2.append(x)
print(lst2)

b = int(input("Please enter a number: "))
for x in lst1:
    if x < b: print(x)
