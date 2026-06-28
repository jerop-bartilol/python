#Relational Operations
cat1=float(input("Enter Cat 1 Mark\n"))
cat2=float(input("Enter Cat 2 Mark\n"))
exam=float(input("Enter Exam Mark\n"))
finalScore=cat1+cat2+exam

if finalScore>=70 and finalScore<=100:
    grade="A"
if finalScore>=60 and finalScore<=69:
    grade="B"
if finalScore>=50 and finalScore<=59:
    grade="C"
if finalScore>=40 and finalScore<=49:
    grade="D"
if finalScore>=0 and finalScore<=39:
    grade="F"

print(f"Final Score={finalScore}\nGrade={grade}")
