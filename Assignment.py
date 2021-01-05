

import sqlite3


conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assign( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_assign(file_name) VALUES (?)", \
                ('Hello.tct'))
    conn.commit()
conn.close()
