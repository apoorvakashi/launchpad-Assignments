from peewee import *

db = SqliteDatabase('mybooks.db')


class User(Model):
	name = CharField()

	class Meta:
		database = db


class Books(Model):
	name = CharField()
	author = CharField()
	genre = CharField()
	progress = IntegerField()
	table = CharField()
	owner = ForeignKeyField(User, backref = "books")

	class Meta:
		database = db



class Tbr(Model):
	name = CharField()
	author = CharField()
	genre = CharField()
	pages = IntegerField()
	progress = IntegerField()
	owner = ForeignKeyField(User, backref = "tbrs")


	class Meta:
		database = db


class Read(Model):
	name = CharField()
	author = CharField()
	genre = CharField()
	year = IntegerField()
	rating = DecimalField()
	owner = ForeignKeyField(User, backref = "reads")

	class Meta:
		database = db


class Favourite(Model):
	name = CharField()
	author = CharField()
	genre = CharField()
	rating = DecimalField()

	class Meta:
		database = db



if __name__ == "__main__":
    db.connect()
    db.create_tables([User, Books, Tbr, Read, Favourite])







