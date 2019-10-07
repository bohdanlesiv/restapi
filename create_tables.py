import  sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table_sql_user ='CREATE TABLE IF NOT EXISTS ' \
                  'USERS (ID INTEGER PRIMARY KEY,' \
                         'USERNAME TEXT,' \
                         'PASSWORD TEXT)'

create_table_sql_items ='CREATE TABLE IF NOT EXISTS ' \
                  'ITEMS ( ID INTEGER PRIMARY KEY,' \
                  'ITEM TEXT,' \
                         'PRICE REAL)'


cursor.execute(create_table_sql_user)
cursor.execute(create_table_sql_items)


sql_insert_item = 'INSERT INTO ITEMS VALUES(?,?,?)'

cursor.execute(sql_insert_item,(1,'aperol',100))



connection.commit()

connection.close()