import MySQLdb

print ("hello")

try:
    conn = MySQLdb.connect(host="127.0.0.1", user="root",
                           passwd="root", db="test")
except MySQLdb.Error as err:
    print("Connection error: {}".format(err))
    conn.close()

sql = "SELECT * FROM a"

try:
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    data = cur.fetchall()
except MySQLdb.Error as err:
    print("Query error: {}".format(err))

print(data)
print("\n\n\n")

print(type(data))

for x in data:
    print(x['id']," ",x['name']," ",x['q']," ",type(x),"\n")

