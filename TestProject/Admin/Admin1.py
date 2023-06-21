import connect.Connection as cc
class AdminC:
    def adminvalidate(self):
        userid=input("Enter user id:");
        password=input("Enter pass:");
        if userid=="ritwik" and password=="ritwik@123":
            return 1
        else:
            return 0
    def adminhome(self):
        t=self.adminvalidate()
        if t==1:
            print("Welcome Admin")
            self.adminmenu()
        else:
            print("Wrong user id or password")
    def adminmenu(self):
        while True:
            print("---Admin---")
            print("1 for insert student details")
            print("2 for modify student details")
            print("3 for delete student details")
            print("4 for insert new questions")
            print("5 delete question")
            print("6 modify question")
            print("7 view student details")
            print("8 view questions")
            print("9 view results")
            print("10 view individual student detail by roll no")
            print("11 exit")
            ch=int(input("Enter your choice"))
            if ch==1:
                self.insert_user_info()
            elif ch==2:
                self.modify_student()
            elif ch==3:
                self.del_student()
            elif ch==4:
                self.insert_ques()
            elif ch==5:
                self.del_ques()
            elif ch==6:
                self.modify_ques()
            elif ch==7:
                self.view_students()
            elif ch==8:
                self.view_ques()
            elif ch==9:
                self.view_results()
            elif ch==10:
                self.view_idvidual()
            elif ch==11:
                break

    def insert_user_info(self):
        ob=cc.Connect1()
        con=ob.conn()
        roll=int(input("Enter roll:"))
        name=input("Enter name:")
        password=input("Enter password:")
        clg=input("Enter college")
        addr=input("Enter address")
        mob_no=input("Enter mobile no:")
        sem=int(input("Enter sem:"))
        dept=input("Enter department")
        q="insert into exam_student_info values('%d','%s','%s',\
           '%s','%s','%s','%d','%s')" %(roll,name,password,clg,\
                                        addr,mob_no,sem,dept)
        stm=con.cursor()
        stm.execute(q)
        print("Student iserted successfully")
        con.commit()
        con.close()
    def view_students(self):
        ob=cc.Connect1()
        con=ob.conn()
        q="select * from exam_student_info"
        stm=con.cursor()
        stm.execute(q)
        result=stm.fetchall()
        print("Roll   Name  Password  College  address  Mob   SEm   DEPT")
        for r in result:
            print(r['roll'],r['name'],r['passwd'],r['collage'],\
                  r['address'],r['mob_no'],r['sem'],r['dept'])
            #print(r)
        con.close()
    def del_student(self):
        r=int(input("Enter Roll to delete:"))
        ob=cc.Connect1()
        con=ob.conn()
        q="delete from exam_student_info where roll='%d'"%(r)
        stm=con.cursor()
        stm.execute(q)
        print("Student deleted successfully")
        con.commit()
        con.close()
    def modify_student(self):
        r=int(input("Enter roll to modify"))
        print("1 for name modify")
        print("2 for mob no change")
        print("3 for change sem")
        print("4 for change Pass")
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        ch=int(input("Enter choice"))
        if ch==1:
            nm=input("Enter new name")
            q="update exam_student_info set name='%s' where roll='%d'"\
               %(nm,r)
            stm.execute(q)
            print("Name modified successfully")
        if ch==2:
            mob_no=input("Enter new mob no")
            q="update exam_student_info set mob_no='%s' where roll='%d'"\
               %(mob_no,r)
            stm.execute(q)
            print("Mobile no modified successfully")
        if ch==3:
            sem=int(input("Enter new sem:"))
            q="update exam_student_info set sem='%d' where roll='%d'"\
               %(sem,r)
            stm.execute(q)
            print("sem modified successfully")
        if ch==4:
            passwd=input("Enter new pass:")
            q="update exam_student_info set passwd='%s' where roll='%d'"\
               %(passwd,r)
            stm.execute(q)
            print("Pass modified successfully")
        con.commit()
        con.close()
    def insert_ques(self):
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        qid=int(input("Enter question id:"))
        sub=input("Enter subject")
        ques=input("Enter question")
        opta=input("Input opta")
        optb=input("Input optb")
        optc=input("Input optc")
        optd=input("Enter option D:")
        cans=input("Enter correct option")
        q="insert into exam_ques values('%d','%s','%s','%s','%s','%s',\
                   '%s','%s')"%(qid,sub,ques,opta,optb,optc,optd,cans)
        stm.execute(q)
        print("Question inserted successfully")
        con.commit()
        con.close()
    def del_ques(self):
        qid=int(input("Enter qid to delete:"))
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        q="delete from exam_ques where qid='%d'"%(qid)
        stm.execute(q)
        print("Question deleted successfully")
        con.commit()
        con.close()
    def view_ques(self):
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        q="select * from exam_ques";
        stm.execute(q)
        result=stm.fetchall()
        print("Subject    Questions")
        for r in result:
            print(r['qid'],r['subject'],r['ques'],r['opta'],r['optb'],r['optc'],r['optd'],r['cans'])
        con.close()
    def modify_ques(self):
        qid=int(input("Enter question id to modify:"))
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        print("1 for change question\n2 for change opt1")
        print("\n3 for change optb\n4 for change optionC")
        print("\n5 for change optd\n6 for change cans:")
        ch=int(input("\nEnter your choice:"))
        if ch==1:
            ques1=input("Enter new question")
            q="update exam_ques set ques='%s' where qid='%d'"%(ques1,qid)
            stm.execute(q)
        if ch==2:
            opta=input("Enter new Opta")
            q="update exam_ques set opta='%s' where qid='%d'"%(opta,qid)
            stm.execute(q)
        if ch==3:
            optb=input("Enter new Optb")
            q="update exam_ques set optb='%s' where qid='%d'"%(optb,qid)
            stm.execute(q)
        if ch==4:
            optc=input("Enter new Optc")
            q="update exam_ques set optc='%s' where qid='%d'"%(optc,qid)
            stm.execute(q)
        if ch==5:
            optd=input("Enter new Optd")
            q="update exam_ques set optd='%s' where qid='%d'"%(optd,qid)
            stm.execute(q)
        if ch==6:
            cans=input("Enter new Cans")
            q="update exam_ques set cans='%s' where qid='%d'"%(cans,qid)
            stm.execute(q)
        con.commit();
        con.close()
        print("Question modified suceessfully")
    def view_results(self):
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        print("\n1 for c")
        print("2 for Math")
        ch=int(input("Enter your choice"))
        sub=""
        if ch==1:
            sub="c"
        if ch==2:
            sub="Math"
        print(sub)
        q="select * from exam_results where subject='%s'"%(sub)
        stm.execute(q)
        result=stm.fetchall()
        for r in result:
            print("Roll no ",r['roll']," has got ",r['marks']," in ",r['subject'])
        con.close()
    def view_idvidual(self):
        ob=cc.Connect1()
        con=ob.conn()
        stm=con.cursor()
        i=int(input("Enter Roll to view student details:"))
        q="select * from exam_student_info where roll='%d'"%(i)
        stm.execute(q)
        result=stm.fetchall()
        for r in result:
            print(r['roll'],r['name'],r['passwd'],r['collage'],\
                  r['address'],r['mob_no'],r['sem'],r['dept'])
        con.close()
    
