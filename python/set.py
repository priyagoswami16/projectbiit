# # set method

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# # Duplicates Not Allowed
# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)


# # True and 1 is considered the same value:
# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# # False and 0 is considered the same value:
# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)

# # Get the Length of a Set
# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

# # Set items can be of any data type:
# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}
# print(set1)
# print(set2)
# print(set3)

# # A set with strings, integers and boolean values:
# set1 = {"abc", 34, True, 40, "male"}
# print(set1)


# # type()
# myset = {"apple", "banana", "cherry"}
# print(type(myset))

# # set constructor
# thisset = set(("apple", "banana", "cherry"))
# print(thisset)

# # access set item
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# # Check if "banana" is present in the set:
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)

# # Check if "banana" is NOT present in the set:
# thisset = {"apple", "banana", "cherry"}
# print("banana" not in thisset)

# # Once a set is created, you cannot change its items, but you can add new items.

# # Add an item to a set, using the add() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)


# # update
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# # Add elements of a list to at set:
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# # remove
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# # discard
# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)

# # pop
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# # clear
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# # del
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# # loop
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# # join 
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# # union
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# print(set3)

# # join multiple set
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)
# print(myset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1 | set2 | set3 |set4
# print(myset)

# # Join a Set and a Tuple
# x = {"a", "b", "c"}
# y = (1, 2, 3)
# z = x.union(y)
# print(z)


# # Both union() and update() will exclude any duplicate items.
# # update
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

# # The intersection() method will return a new set, that only contains the items that are present in both sets.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)

# # You can use the & operator instead of the intersection() method, and you will get the same result.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)

# # Keep the items that exist in both set1, and set2:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1)

# # Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)


# # The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# # Keep all items from set1 that are not in set2:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)

# # Use the difference_update() method to keep the items that are not present in both sets:

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)


# # The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# # Example
# # Keep the items that are not present in both sets:

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)

# # Use the symmetric_difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)