sum=0.0
avg=0.0
j=2
while j<=102:
    if j%2==2:
        sum+=j
        odd+=1
    j+=1
else:
    avg=sum/odd
    print(f"Total no of odd numbers\t{odd}")
    print(f"The sum of odd numbers is\t {sum}")
    print(f"The average of odd numbers is\t{avg}")  
    