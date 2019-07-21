# create a tuple

first_tuple = (8, 9, 10)

# single entry tuple

single_entry_tuple = (10)

# list and tuple

list1 = ["one", "two", "three"]
tuple1 = ("one", "two", "three")

list1.remove(list1[1])
lst = list(tuple1)
lst.remove(lst[1])
tuple1 = tuple(lst)

print(list1)
print(tuple1)

list1.insert(1, 2)
lst = list(tuple1)
lst.insert(1, 2)
tuple1 = tuple(lst)

print(list1)
print(tuple1)

# check and print type of tuples

t1 = (9)
t2 = (9,)
t3 = ('9')

print(type(t1))
print(type(t2))
print(type(t3))

# using the bool function

tuple2 = (10)
print(bool(tuple2))

tuple3 = ()
print(bool(tuple3))