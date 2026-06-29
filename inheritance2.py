class person:
    def __init__(self):
        self.name=input("Enter Name\n")
        self.gender=input("Enter Gender\n")
        self.dateOfBirth=input("Enter DOB\n")
class staff(person):
    def __init__(self):
        self.staffNo=input("Enter Staff Number\n")
        super().__init__()
        self.display()#Calls the display function
    def display(self):
        print(f"Staff Number\t{self.staffNo}\n")
        print(f"Staff Name\t{self.name}\n")
        print(f"Staff Gender\t{self.gender}\n")
        print(f"Date of Birth\t{self.dateOfBirth}\n")
        
st=staff()
        
        