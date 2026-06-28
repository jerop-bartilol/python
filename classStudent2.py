class Person:
    def __init__(self):
       pass
    def accept(self):
       self.name=input("Enter name\n")
       self.dateOfBirth=input("Enter DOB\n")
       self.gender=input("Enter gender\n")
       self.weight=input("Enter weight\n")
       self.height=input("Enter height")
    def display(self):
        print(f"name\t:{self.name}")
        print(f"Date Of Birth\t:{self.dateOfBirth}")
        print(f"gender\t:{self.gender}")
        print(f"weight\t:{self.weight}")
        print(f"height\t{self.height}")
        

p=Person()
p.accept()
p.display()