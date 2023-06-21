#Main.py
import Admin.Admin1 as AA
import Student.student1 as Ss
while True:
    print("\n1.Admin\n2.User\n3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        ob=AA.AdminC()
        ob.adminhome()
    elif ch==2:
        ob1=Ss.StudentC()
        ob1.student_menu()
    else:
        break
