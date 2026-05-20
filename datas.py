import sqlite3




db = sqlite3.connect('users.db')
cursor = db.cursor()


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users(
#                id TEXT,
#                name TEXT,
#                phone_num TEXT,
#                adress TEXT
#                )

# ''')

async def add_to_db(id,name,phone,adress):
    cursor.execute('''
INSERT INTO users(id,name,phone_num,adress)
                   VALUES(?,?,?,?)

''',(id,name,phone,adress))
    
async def show_users():
    cursor.execute('''
SELECT * FROM users

''')
    datas = cursor.fetchall()
    return datas


