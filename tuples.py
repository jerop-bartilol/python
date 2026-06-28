#Creating a tupple
countries=("Kenya","Tanzania","United Kingdom","United States","Kenya")
#Getting the length of the tupple
#print(f"The tupple length is \t{len(countries)}")
#print(countries)

#Getting a spefic item
#Positive Indexing
#print(f"The third item in the list\t{countries [2]}")

#Negative indexing
#print(f"The second last itme in the list\t{countries[-2]}")

#Ranging items
#print(countries[1:4]) #Return item 2 to 4
# print(countries[2:]) Returns the third to the last
#Start to the last item 
#print(countries[:3])

#Searching through the tupple 
#searchvar=input("Enter item to search for\n")
#if searchvar in countries:
   # print(f"{searchvar}\t Exist in the tupple\n")
#else:
    #print(f"{searchvar}\t doesn't exist on the tupple\n")
    
    #Changing a tupple 
    # Step 1- Creating the tupple(Already done) 
    # Step 2- converting it to a list
myList=list(countries)
     #Update or change something on the list
myList[4]="Brazil"
#Step 4-Convert to a tupple
countries=tuple(myList)
print(countries)




