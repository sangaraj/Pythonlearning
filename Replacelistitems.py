fruits = ["apple","mango","guava","Banana", "kiwi", "papaya"]
print(len(fruits))
fruits[5] = "pine apple"
print(fruits)

fruits1 = ["apple","mango","guava","Banana", "kiwi", "papaya"]
fruits1[0:2] = ["icecream", "chocklate"]
print(fruits1)

#inserting more item then what we are replacing
fruits2 = ["apple","mango","guava","Banana", "kiwi", "papaya"]
print(len(fruits2))
fruits2[0:2] = ["icecream", "chocklate", "Biscute"]
print(len(fruits2))
print(fruits2)


#inserting less item then what we are replacing
fruits3 = ["apple","mango","guava","Banana", "kiwi", "papaya"]
print(len(fruits3))
fruits3[0:2] = ["icecream"]
print(len(fruits3))
print(fruits3)




