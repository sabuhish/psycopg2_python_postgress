# # import User from user file
from user import User

from database import Database


# object this parametr acepting any number of paramet with kwargs
Database.inittialise(user='postgres',
                    password='sabuhi1234567890', 
                    database='learning', 
                    host='localhost' )

# # my_user = User("sabuhi.shukurov@gmail.com", "Sebuhi", "Shukurov", None)

# my_user =User.load_from_db_by_email("sabuhi.shukurov@gmail.com")

# # print(my_user.email)

# # my_user.save_to_db()

# print(my_user)
# # creates first users object
my_user_2 = User("test@gmail.com", "This", "test", None)
# # this methods saves
my_user_2.save_to_db()

# # retrive the user from db
user_from_db = User.load_from_db_by_email("test@gmail.com")

print(user_from_db)

# object 
database_one = Database()
database_two = Database()
# none 
# print(database_one.connection_pool)


# print(Database.connection_pool)
