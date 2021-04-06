vehicle = ["Bike", "Car", "Cycle"]
# this will the element at the last of the list
vehicle.append("toycar")
print(vehicle)

#This will add the element at the specified postion
vehicle.insert(0,"boat")
print(vehicle)

#extend this will join two list

vehicle1 = ["Bike", "Car", "Cycle"]
vehicle2 = ["plane", "helicopter", "jet"]
vehicle1.extend(vehicle2)
print(vehicle1)
print(vehicle2)