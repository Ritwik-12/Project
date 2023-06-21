import connect.Connection as cc
class StudentC:
    def validate(self):
        roll=int(input("Enter Roll:"))
        passwd=input("Enter Password:")
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        q="select * from exam_student_info where roll='%d' and passwd='%s'"%(roll,passwd)
        stm.execute(q)
        t=-1
        s=""
        result=stm.fetchall()
        for r in result:
            t=r['roll']
        return t
    
    def student_menu(self):
        t=self.validate()
        if t==-1:
            print("Invalid Roll or password")
        else:
            while(True):
                print("----------MENU-------")
                print("Welcome ",t)
                print("1 for Give exam")
                print("2 for show results:")
                print("3 for change password")
                print("4 for exit")
                print("----------------------")
                ch=int(input("\nEnter your choice:"))
                if ch==1:
                    self.give_exam(t)
                if ch==2:
                    self.show_results(t)
                if ch==3:
                     self.change_password()
                if ch==4:
                    break
    def give_exam(self,roll1):
        sub=input("Enter subject name to Exam:")
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        q="select * from exam_result where roll='%d' and subject='%s'"%(roll1,sub)
        stm.execute(q)
        f=0
        result=stm.fetchall()
        con.close()
        for r in result:
            f=1
        if f==1:
            print("Already exam given")
        else:
            self.start_exam(roll1,sub)
    def start_exam(self,roll1,sub):
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        q="select * from exam_ques where subject='%s'" %(sub)
        marks=0
        stm.execute(q)
        result=stm.fetchall()
        i=1
        for r in result:
            print("Question no:",i,r['ques'])
            print("a)",r['opta'])
            print("b)",r['optb'])
            print("c)",r['optc'])
            print("d)",r['optd'])
            ans=input("\nType correct answer in opta/optb/optc/optd manner:")
            if ans==r['cans']:
                marks=marks+1
            i=i+1
        
        q1="insert into exam_result values('%d','%s','%d')"%(roll1,sub,marks)
        stm.execute(q1)
        con.commit()
        print("YOUR RESULTS:")
        print(roll1,sub,marks)
        con.close()
    def change_password(self,roll1):
        newpass=input("Enter your new password:")
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        q="update exam_student_info set passwd='%s' where roll='%d'"%(newpass,roll1)
        stm.execute(q)
        con.commit()
        con.close()
        print("Password modified successfully")
    def show_results(self,roll1):
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        q="select * from exam_results where roll='%d'"%(roll1)
        stm.execute(q)
        result=stm.fetchall()
        f=0
        for r in result:
            print("Roll number ",r['roll']," has got ",r['marks']," marks in ",r['subject'])
            f=1
        if f==0:
            print("First give exam")
        con.close()
