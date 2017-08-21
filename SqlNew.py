import MySQLdb

def Delimiter():
    print("_________________________________________________\n")

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
'''
db=MySQL()
db.Show("SELECT VERSION()")

'''
db=MySQLdb.connect("127.0.0.1","root","root","test")
cu=db.cursor()
cu.execute("SELECT VERSION()")
cu_response=cu.fetchall()
print(cu_response)
db.close()
