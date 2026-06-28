Destination=input("Enter the time of destination")
time=input("Enter the depature time")

if Destination=="Voi" and time=="11:00":
    RegNo="KBZ 009Z"
    ArrivalTime="12:00"
    available=False
elif Destination=="Kisumu" and time=="9:00":
    RegNo="KBX 100X"
    ArrivalTime="12:00"
    available=False
elif Destination=="Mombasa" and time=="8:00":
    RegNo="KAQ 998Y"
    ArrivalTime="2.00"
    available=False
else:
    available=True
    
if available== False:
    print(f"{Destination} not available")
    