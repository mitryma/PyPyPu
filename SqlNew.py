import MySQLdb

def Delimiter():
    print("_________________________________________________\n")

'''
class MySQL(MySQLdb):
    def __init__(self):
        self.db=MySQLdb.connect("127.0.0.1", "root", "root", "test")
        self.cu=self.db.cursor()

    def query(self,SQL):
        self.cu.execute(SQL)
        self.response=self.cu.fetchall()

    def Show(self,SQL):
        self.query(self,SQL)
        print("\n\n")
        Delimiter()
        print("on request: ", SQL)
        Delimiter()
        print(self.response)
        Delimiter()

db=MySQL()
db.Show("SELECT VERSION()")

'''
db=MySQLdb.connect("127.0.0.1","root","root","test")
cu=db.cursor()
cu.execute("SELECT VERSION()")
cu_response=cu.fetchall()
print(cu_response)

cu.execute("SELECT * FROM a")
cu_response=cu.fetchall()
print(cu_response)


SQL=''' CREATE TABLE IF NOT EXISTS CITY (ID INT UNIQUE NOT NULL,
        NAME CHAR(20) NOT NULL,
        COUNTRY_ID INT NOT NULL
    )'''
cu.execute(SQL)

SQL=''' INSERT INTO CITY (ID,NAME,COUNTRY_ID) VALUES (1,"St.Peresburg",1)'''
cu.execute(SQL)

SQL=''' INSERT INTO CITY (ID,NAME,COUNTRY_ID) VALUES (2,"Moscow",1)'''
cu.execute(SQL)

SQL=''' INSERT INTO CITY (ID,NAME,COUNTRY_ID) VALUES (3,"Voroneg",1)'''
cu.execute(SQL)

cu.execute("commit")

cu.execute("SELECT * FROM city")
cu_response=cu.fetchall()
for xx in cu_response:
    print(xx,"\n")

db.close()
