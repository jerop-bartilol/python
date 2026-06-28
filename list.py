#Code for writing the list
cars=["Red Bull","Alphine","Hass","Ferrari","Benz"]
#print(cars)

#Getting the number of items in the list
#print(f"Total items in the list{len(cars)}")

#Accesing list items using index
#print(f"Third item on the list\t{cars[2]}")

#Using Negative indexing
#print(f"The second item using -ve indexing\t{cars[-4]}")
#print(f"Item 2-4\t{cars[1:4]}")
#print(f"Return third to last\t{cars[2:]}")

#Searching for items
#searchvar=input("Enter items to search for\n")
#if searchvar in cars:
 #   print(f"{searchvar}\t exist in your list\n")
#else:
  #  print(f"{searchvar}\t doesn't exist in your list\n")
  
  #Updating
#cars[2]="Cadillac"
#print(cars)

#Removing items
#remove method
#cars.remove("Benz")
#print(cars)

# removing using the pop method
#cars.pop(1)
#print(cars)

#Using the delete method
#del cars[3]
#print(cars)

#clearing a list
#cars.clear()
#print(cars)

#Deleting a list
del cars
print(cars)