import pymysql
class Connect1:
    def conn(self):
        self.con=pymysql.connect(host="localhost",user="root",\
                    password='',database='examdb',\
                    charset='utf8mb4',\
                    cursorclass=pymysql.cursors.DictCursor)
        
        return self.con
