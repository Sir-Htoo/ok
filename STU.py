# Htoo Maw
# Cisoo
#12-6-2020
class student:
    stu={} #Class vairable
    def __init__(self,name,mark): #Special method
        self.adname=name
        self.admark=mark
        self.ddelete=name

    def add(self): #instance method
        student.stu.update([(self.adname,self.admark)])
        return print(student.stu)

    @classmethod
    def delete(cls): #class method
        sdelete = input("Please Enter you want to remove Student's Name ")
        if sdelete in student.stu:
            cls.stu.pop(sdelete)
            print("{}'s Mark Removed".format(sdelete))
            print(student.stu)
        else:
           print("{} can not be found in Student list".format(sdelete))
        return teacher()

    @staticmethod
    def search(): #Static method
        ssea=ssearch()
        if ssea in student.stu:
            print("{}'s Mark Found.".format(ssea))
            print("{} = {}".format(ssea,student.stu[ssea]))
        else:
            print(ssea + " can not be found in Student list.")
            print("{} cannot be found in Student list".format(ssea))
        return teacher()
#====================================================================
def stuadd(student):
    addname = input("Enter Student' Name = ")  # add
    addmark = int(input("Enter Student' Mark = "))  # add
    sinfo=student(addname,addmark)
    sinfo.add()
    teacher()
    tm = tmenu()
#====================================================================
def studelete(student):
    print(student.delete())
    tm = tmenu()
#===========================================================================
def stusearch(student):
    student.search()
    tm=tmenu()
#===========================================================================
def main():
    print("\n")
    print("****************** Student's Marks System ******************\n")
    print("************************** Main Menu ***********************\n")

    print("[1] If you are Teacher type 'T'.")
    print("[2] If you are Student type 'S'.")
    print("[3] To Exit type 'E'.")
#======================================================================
def tmenu():
    ch=choice()
    if ch=='add':
        stuadd(student)
    elif ch=='remove':
        studelete(student)
    elif ch=='search':
        stusearch(student)
    elif ch=='B':
        main()
        me=menu()
        ##
    tm=tmenu()
    return tm

#===========================================================================
def choice():
    ch=input ("Enter input your choice = ")
    return ch
#===========================================================================
def ssearch():
    print("\n")
    print("******************** Search Student'mark ****************\n")
    ssea=input("Please Enter you want to Search Student's Name ")
    return ssea
#===========================================================================
def teacher():
    print("\n")
    print("********************* Teacher Menu *********************\n")
    print("[1] To add marks Type 'add'.")
    print("[2] To remove marks type 'remove'.")
    print("[3] To Search Marks types 'search'.")
    print("[4] Go to Back Main Menu type 'B'.")
#===========================================================================

#===========================================================================
import sys
def menu():
    main()
    ch=choice()
    if ch=='T':
        teacher()
        tm=tmenu()
    elif ch=='S':
        ssea=ssearch()
        if ssea in student.stu:
            print("{}'s Mark Found.".format(ssea))
            print("{} = {}".format(ssea,student.stu[ssea]))
        else:
            print("{} can not be found in Student list.".format(ssea))
            #ma=main(addname,addmark)
            me=menu()
    elif ch=='E':
        sys.exit()
    ##
    me=menu()
    return me

me=menu()
