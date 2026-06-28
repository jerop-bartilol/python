#Identity operators
value="Programming"
char=input("Enter Character to search\n")
if char in value:
    print(f"{char}\t is present in {value}")
else:
    print(f"{char}\t is not present in {value}")