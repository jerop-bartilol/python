myPc={
    "model":"HP",
    "RAM":"16GB",
    "Color":"Grey",
    "Speed":"17,Gen 13",
    "Price":150000
}
#print(myPc) 
# Length of the dict
#print(f"Dictionary Length\t{len(myPc)}")  

# Accesing an item
#print(f"My Pc RAM:\t{myPc["RAM"]}")

#Getting the keys
#print(myPc.keys())

#Adding an item in the set
#myPc["Hard Disk"]="520 GB, Sata Drive"
#print(myPc) 

#Getting the values
#print(myPc.values())

#Getting both the values and the keys
#print(myPc.items)

#Updating Values
#myPc["RAM"]="32GB RAM"
#print(myPc) 
# Removing items from dict
#myPc.pop("RAM")
#del myPc["model"]
#myPc.popitem()
#print(myPc)

#Searching
searchDict=input("Item to search for\n")
if searchDict in myPc:
    print(f"{searchDict}\t Exist in the dictionary")
else:
    print(f"{searchDict}\t item doesn't exist in the dictionary") 