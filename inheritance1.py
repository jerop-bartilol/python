class person:
    def __init__(self):
        pass
    def acceptPerson(self):
        self.name=input("Enter Name\n")
        self.gender=input("Enter Gender\n")
        self.height=float(input("Enter Height\n"))
        self.weight=float(input("Enter Weight\n"))
    def displayPerson(self):
        print(f"Name:\t{self.name}\n")
        print(f"Gender:\t{self.gender}\n")
        print(f"Height:\t{self.height}\n")
        print(f"Weight:\t{self.weight}\n")
class student(person):#Inherits properties of class person
    pass
#create object of type student 
stud=student()
print("Enter information about a student\n")
stud.acceptPerson()
print("Display Information about the student\n")
stud.displayPerson()