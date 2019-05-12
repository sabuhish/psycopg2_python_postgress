# import pstcopy2
from psycopg2 import pool


# min and max if we set 4  it will create 4, second one sets how many you wnat
# connection_pool = pool.SimpleConnectionPool(1, 10,                                      user='postgres',
#                                 password='sabuhi1234567890', 
#                                 database='learning', 
#                                 host='localhost' )

# creating method with psycopg2
# def connect():
#     return psycopg2.connect(user='postgres',password='sabuhi1234567890', database='learning', host='localhost')


# create connection pool outisde of class
#connection created 
class Database:
    # So this property here belongs to the class itself and not one of the objects. class property, private
    __connection_pool = None


    # acces connection directly
    @classmethod
    def inittialise(cls, **kwargs):
        # the property connection pool of the database class, not an object.
        cls.__connection_pool = pool.SimpleConnectionPool(1, 
                                                        10,     
                                                        **kwargs)


    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()


    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)

    # stops commit
    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()

# init creates connection property
class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection =None
        self.cursor =None

    # to get new connection from the pool
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor =self.connection.cursor()
        return self.cursor

    # commit connection
    def __exit__(self, excexption_type, excexption_value, excexption_tb):
        if excexption_value is not None: #errors
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)




# cp =ConnectionPool()
# cp.connection_pool