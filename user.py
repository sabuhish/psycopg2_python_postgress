# imports databse file 
from database import CursorFromConnectionFromPool


class User:
    def __init__(self,email, first_name, last_name, id):
        self.email =email
        self.first_name =first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)
    
    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO users (email, fisrt_one, last_name) VALUES (%s, %s, %s)', (self.email, self.first_name, self.last_name ))
                # connection.commit()
                # connection.close()
                # putting connection back

    # loading from psotgress
    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('select * from users where email=%s', (email,))
            user_data = cursor.fetchone()
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])

