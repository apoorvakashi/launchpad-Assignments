name = input("Enter your name: ")
age = int(input("Enter your age: "))

yearsto100 = 100 - age
year= 2019 + yearsto100

for i in range(len(name)):
	if name[i] == " ":
		firstname= name[0:i]

ans = f"Hey {name}! You'll turn 100 years old in {year}"
print(ans)
