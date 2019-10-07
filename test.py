import  sqlite3

connection =sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, " \
               "                   username text, " \
               "                   password text)"

cursor.execute(create_table)


user = (-1, 'Test', 'Test')


insert_sql = "INSERT  INTO USERS VALUES (?,?,?)"

cursor.execute(insert_sql,user)

users =[
    (1, 'Bogdan', '1111'),
    (2, 'Vasyl', '2222'),
    (3, 'Ivan', '3333'),
    (4, 'Denys', '4444'),
    (5, 'Ismet', '5555')
]
cursor.executemany(insert_sql, users)

select_sql ='SELECT * FROM USERS'

for row in cursor.execute(select_sql):
    print(row)

connection.commit()

connection.close()