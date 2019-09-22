numbers = [1,1,2,3,4,6,78,35,4,35,6,9,10]
numlist = []
for i in numbers:
    if i not in numlist:
        numlist.append(i)
print(numlist)