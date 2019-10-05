from app import *

print("welcome to mybooks", "-"*20, sep="\n")

while True:

	print("\n", "-"*20, "\n")
	print(list_users())
	print("a.Add user")
	print("e.exit")


	print("-----Select-----")
	select = input("---->")


	if select == 'a':
		add_user()

	elif select == 'e':
		exit()
	
	else:
		while True:
			print("\n\n      welcome")
			print("\n", "-"*20, "\n")
			print("What would you like to do?:\n\
1. See TBR\n\
2. See READ PILE\n\
3. update TBR\n\
4. see CURRENT\n\
5. List by category\n\
6. suggestions\n\
7. see favourites\n\
8. exit to menu")

			choice = input("enter your choice\n")

		
		if choice == "1":
			see_tbr()

# 		elif choice == "2":
# 			see_read()
		
# 		elif choice == "3":
# 			update_tbr()
		
# 		elif choice == "4":
# 			see_current()
		
# 		elif choice == "5":
# 			list_by_category()
		
# 		elif choice == "6":
# 			list_suggestions()
		
# 		elif choice == "7":
# 			see_favourites()
		
		else:
			break





