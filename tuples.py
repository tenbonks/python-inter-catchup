import sys
import timeit

# Tuple, ordered, immutable, allows duplicate elements
# Note: Tuples are handled more efficently in python
myTuple = ("Max", 28, "Boston")
print(myTuple)  # ('Max', 28, 'Boston')

# A single value in a tuple will be recognized as a string
notATuple = ("Max")
print(type(notATuple))  # <class 'str'>

# for single valued tuples, make sure there is a "," following
isATuple = ("Max",)
print(type(isATuple))  # <class 'tuple'>

# there is also a built in tuple function, this can create a tuple from
# an itterable Example: A list
myTupleFunc = tuple(["Sandra", 21, "Dundee"])
print(myTupleFunc)  # ('Sandra', 21, 'Dundee')

# You can access elements by using the index
# 0 = name, 1 = age, 2 = location in this tuple
item = myTuple[1]
print(item, end="\n")  # 28

# Tuples are not mutable so the code below will cause an error
# myTuple[0] = "Andy"

# Itterate through a tuple
for i in myTupleFunc:
    print(i)  # Sandra \n 21 \n Dundee

# Check if value is in a tuple
if "Max" in myTuple:
    print("Yes")
else:
    print("No")

# Check the length of the tuple
print(len(myTuple))  # 3

# Count the amount of specified value
print(myTuple.count('Boston'))  # 1

# Find the index of a value
print(myTuple.index("Max"))  # 0

# You can convert tuples to lists, and lists to tuples
my_list = list(myTuple)
print(my_list)  # ['Max', 28, 'Boston']
print(type(my_list))  # <class 'list'>

# You can slice tuples, slicing acts the same way is it would with lists
# [startIndex:EndIndex] [::indexSteps]
# if no start index, it will default at 0
# no end index it will default to the last index in the tuple
slicedTuple = myTuple[1:3]
print(slicedTuple)  # (28, 'Boston')


# Tuples can be unpacked simply by assigning names to the tuple
# the number of named elements needs to match the tuple
# if I ommited city below, then there would be a value error
# as I have two elements for the 3 values in the tuple
name, age, city = myTuple
print(name, age, city, sep=", ", end=".\n")  # Max, 28, Boston.
print("His name is " + str(name) + ", they are " +
      str(age) + ", Living in " + str(city))
# Output ^ His name is Max, they are 28, Living in Boston

# Following on from unpacking, you can unpack values into a list
# by using '*' prefix on i2, a list will be made from 1:5
# had I of named four elements to unpack to the list would be 1 value shorter
intTuple = (0, 1, 2, 3, 4, 5)
i1, *i2, i3 = intTuple
print(i1)  # 0
print(i2)  # [1, 2, 3, 4]
print(i3)  # 5


# a tuple and a list containing the same values
# importing sys at the top of the file allows me
# to get the size of the argument passed
# notice how tuples are much more efficient with data usage
listSizeTest = [0, 1, 2, "hello", True]
tupleSizeTest = (0, 1, 2, "hello", True)
print(sys.getsizeof(listSizeTest), "Bytes")  # 120 Bytes
print(sys.getsizeof(tupleSizeTest), "Bytes")  # 80 Bytes


# Below I will time how long it takes to create a list / tuple
# number = 100000 means that it will create one million of the element
print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000))  # 0.1856376
print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000))  # 0.0296536...
