
import sqlite3

conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_files TEXT)')
    conn.commit()


conn = sqlite3.connect('test1.db')

# tuple of files
fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # (x,) will denote a one element tuple for each name ending with .txt
            cur.execute('INSERT INTO tbl_files (col_files) VALUES (?)', (x,))
            print(x)

conn.close()
