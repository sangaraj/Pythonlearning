# Add to two interger values but taken those as string
print("### Add to two interger values but taken those as string ###")
num1 = input("Enter the number1: ")
num2 = input("Enter the number2: ")
# by default user input is taken as string, so instead of adding the no's it consider the no as string and concat them
result1 = num1+num2
print("Additin of two string no is: " + result1)


# Add to two interger values
print("###Add of two int values###")
num3 = input("Enter the number1: ")
num4 = input("Enter the number2: ")
# int function will take only interger not float
result2 = int(num3)+ int(num4)
print("Additin of two no is: " +  str(result2))


#Add of two floadt values
print("###Add of two floadt values###")
num5 = input("Enter the number1: ")
num6 = input("Enter the number2: ")

# int function will take only interger not float
result2 = float(num5)+ float(num6)
print("Additin of two no is: " +  str(result2))



