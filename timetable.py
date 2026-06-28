LectureHall=input("Enter the lecture hall\n")
TimeSlot=input("Enter the time slot\n")
Day=input("Enter the day of the week\n")

if LectureHall=="TH Lab A" and TimeSlot=="11-2" and Day=="Teusday":
    UnitName="CMT 109-Database Systems"
    LectureName="Joe"
    availabe=False
elif LectureHall=="TH Lab A" and TimeSlot=="2-5" and Day=="Wednesday":
    UnitName="CMT 206-Operating Systems"
    LectureName="Phil"
    available=False
elif LectureHall=="TH Lab B" and TimeSlot=="11-2" and Day=="Friday":
    UnitName="CMT 113-Logical Programing"
    LectureName="Christina"
    available=False
else: 
    available=True
#Program Output
if available== False:
    print(f"{LectureHall} is not available on {Day} {TimeSlot}\n")
    print(f"Unit Name: {UnitName} Lecture Name {LectureName}\n")
else:
    print("The hall is free at that time of the day\n")
    