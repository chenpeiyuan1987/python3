import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'world')

cursor = db.cursor()

cursor.execute('SELECT COUNT(1) FROM country')


data = cursor.fetchone()

print("World Count: %s" % data)

db.close()
