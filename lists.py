# A string which will be repeated alot in print statements
lineSpacer = "\n------------------------\n"

# Lists: ordered, mutable, allows duplicate elements
myList = ["potato", "cucumber", "tomato", "tomato"]
print(lineSpacer, myList, end=lineSpacer)

# create an empty list
myList2 = list()
print(myList2, end=lineSpacer)

# Lists can contain integers, floats, bools, strings
dataTypeList = [3, 1.23, True, "potato"]
print(dataTypeList, end=lineSpacer)

# get the item in the list by its index number
item = myList[0]
print(item, end=lineSpacer)

# itterate through the list
for i in myList:
    print(i)

# Check if an value is in a list
if "lemon" in myList:
    print("yes")
else:
    print("no")

# A list can be made up of existing lists
listOfLists = [myList, myList2, dataTypeList]
print(listOfLists)

# get the first list, first item, and slice the first 3 characters of the item
listsItem = listOfLists[0][0][0:3]
print(listsItem)

# a list of unordered numbers
intList = [5, 3, 10, 6, 20, -4, 12]
print("List before it is altered: " + str(intList))

# sort() will sort numbers and strings, it will not return the list
# It will replace the original list
intList.sort()
print("Altered Sorted List: " + str(intList))

# Reverse flips the output, but doesn't sort
# Where sort is above this code, it will be sorted, and then reversed
intList.reverse()
print("Altered Reversed + Sorted List: " + str(intList))


# if you dont want to alter the original list,
# you can set the variable to a new variable and apply a method
# sorted and sort are very similar, but will be used in different applications
originalIntList = [8, 2, 16, 4, -5, 32]
sortedIntList = sorted(originalIntList)
print("Sorted list: " + str(sortedIntList))
print("Original Unaltered list: " + str(originalIntList))

# If you want to create multiple duplicates within a list, you can do this
dupList = [0] * 5
print(dupList)

# You can concatenate lists together
conList = [1, 2, 3, 4, 5]
conList2 = [6, 7, 8, 9, 10]
print(conList + conList2)


# slicing is useful for accessing specified indexes
# [0:3] == [:3], [::2] steps of 2, [2:] will list index 2 to end of list
# [2:5] will slice from the 2nd index to the 5th
# [::-1] is a trick to reverse the list
slicedConlist = conList[::-1]
print(slicedConlist)

# here I am using list comprehension to create a list of square numbers
# from another list
compdList = [i*i for i in conList]
print(conList)
print(compdList)
