class Student:
    def __init__(self,r,n,g,c): #Makes the code to be called automatically when crreating an instance
        #Self has to be the FIRST parametr to declare other paremeters. 
        self.regno=r
        self.name=n
        self.gender=g
        self.course=c
    def display(self):
        print(f"regno\t:{self.regno}")
        print(f"name\t{self.name}")
        print(f"gender\t{self.gender}")
        print(f"course\t{self.course}")
#End of class defination
#Read program inputs
regno=input("Enter registration Number\n")
name=input("Enter student name\n")
gender=input("Enter the gender\n")
course=input("Enter the course\n")
#Instantiate the class
s=Student(regno,name,gender,course) #Creates an object of type Student
#Call dispaly function 
s.display()

        