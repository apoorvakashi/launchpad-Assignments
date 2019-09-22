numbers = [1, 3, 4, 6, 4, 35, 5, 43, 3, 4, 18, 3, 1, 1]
numlist= []
element = int(input("Enter a number: "))
for index, value in enumerate(numbers):
    if value==element:
        numlist.append(index)
print(numlist)
        
    