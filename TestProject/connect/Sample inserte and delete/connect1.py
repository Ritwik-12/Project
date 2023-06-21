import pymysql
#compatibility and connectivity
con=pymysql.connect(host="localhost",user="root",password='',database='examdb',charset='utf8mb4',\
                    cursorclass=pymysql.cursors.DictCursor)
#carrier
stm=con.cursor()
sid=input("Enter sid:")
name=input("Enter name:")
clg=input("Enter collage name:")
marks=int(input("Enter marks:"))
q="insert into test values('%s','%s','%s','%d')"%(sid,name,clg,marks)
stm.execute(q)
print("Inserted Sucessfully")
con.commit()
con.close()
