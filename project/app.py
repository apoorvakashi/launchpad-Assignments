from models import *
from datetime import datetime

db.connect()


'''
check user
list user
add user
1. See TBR
2. See READ PILE
3. update TBR
4. see CURRENT
5. List by category
6. suggestions
7. see favourites
8. exit to menu")

'''


def check_user():
	users = User.select()
	if len(users)==0:
		return 0
	else:
		return 1


def list_users():
	yes = check_user()
	if yes:
		users = User.select()
		for user in users:
			print(user.id, user.name)

	else:
		print("Please Add User!!!!!")

def add_user():
	name = input("Enter name of user : ")
	user = User(name = name)
	user.save()

def check_tbr():
	tbrs = Tbr.select()
	if len(tbrs)==0:
		return 0
	else:
		return 1


def see_tbr():
	yes = check_tbr()
	if yes:
		tbrs = Tbr.select()
		for tbr in tbrs:
			print(tbr.id, tbr.name)








