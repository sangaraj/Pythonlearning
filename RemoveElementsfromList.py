metal = ["Gold","Silver", "Diamond", "Copper", "Alluminum"]
#removed an item using the text
metal.remove("Alluminum")
print(metal)

#removing the item using index
metal.pop(0)
print(metal)

#using pop without index, this will delete the last item
metal1 = ["Gold","Silver", "Diamond", "Copper", "Alluminum"]
metal1.pop()
print(metal1)

#using del funtion with index
metal2 = ["Gold","Silver", "Diamond", "Copper", "Alluminum"]
del metal2[0]
print(metal2)

#using del funtion to delete list
metal3 = ["Gold","Silver", "Diamond", "Copper", "Alluminum"]
del metal3
#print(metal3)


#Clear list, this just clear the content of list but no the list
metal4 = ["Gold","Silver", "Diamond", "Copper", "Alluminum"]
metal4.clear()
print(metal4)





