
# list is denoted by [], it is used to store multiple value in a single variable
# list can store any type of date lile string, int and boolean in same list
# list allows duplicate values
listexample = ["rohit", "srk", "adity"]
print(listexample)

stringlist = ["abc","pqr", "xyz", "abc"]
numberlist = [1,2,3,4,5,1]
booleanlist = [ True, False, True, False]
mixedlist = ["srk", 1, True]
print(stringlist)
print(numberlist)
print(booleanlist)
print(mixedlist)

#this will print the type as List
print(type(stringlist))
print(type(numberlist))
print(type(mixedlist))

#Creating a list using constructor
constructorlist = list(("hi",1,True))
print("Created using list constructor " + str(constructorlist))


#Accessing elements
#This will print the values from the left of the list
print(listexample[0])

# negative values will  print the value from right side of the list
print(listexample[-1])

# accessing elements using range
print(numberlist[1:4]) # will iclude start index but not end index i.e will fetch elements from endindex-1
print(numberlist[:4])
print(numberlist[2:])
print(numberlist[-4:-1])

#check if element exists in the list
if "abc" in stringlist:
    print("abc exists in the list")

# to replace a vlaue in the list
listexample[0] = "mm"
print(listexample)