#For delete from the sql table
import pymysql
#compatibility and connectivity
con=pymysql.connect(host="localhost",user="root",password='',database='examdb',charset='utf8mb4',\
                    cursorclass=pymysql.cursors.DictCursor)
#carrier
stm=con.cursor()
sid=input("Enter sid:")
q="delete from test where sid ='%s'"%(sid)
stm.execute(q)
print("Deleted sucessfully")
con.commit()
con.close()

