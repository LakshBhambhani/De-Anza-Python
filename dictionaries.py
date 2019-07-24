# declaring dictionaries

my_dict = {"Gaby": 8, "Max": 8}
print(type(my_dict["Gaby"]))
print(my_dict)

#adding a key value pair to my dictionary

my_dict["John"]=12
print(my_dict)

# create list of keys and values

nameList = list(my_dict.keys())
ageList = list(my_dict.values())
wholeValues = list(my_dict.items())

print(nameList)
print(ageList)
print(wholeValues)

my_dict.pop("Max")

print(my_dict)