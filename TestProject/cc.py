import pymysql

conn=pymysql.connect(host="localhost",user="root",password="",database="examdb",charset='utf8mb4',\
                    cursorclass=pymysql.cursors.DictCursor)
cursor=conn.cursor()
q="select * from exam_student_info"
cursor.execute(q)
results=cursor.fetchall()
print("no of student in the exam",cursor.rowcount)
for r in results:
     print(r['roll'],r['name'],r['passwd'],r['collage'], r['address'],r['mob_no'],r['sem'],r['dept'])
cursor.close()
conn.close()
