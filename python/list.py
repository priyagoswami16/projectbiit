# mylist = ["apple", "banana", "cherry"]
# print(mylist)

# # Allow Duplicates
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# # length
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# # data types
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(list1)
# print(list2)
# print(list3)

# # type
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# # list constructor
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# # access list item
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# # Change Item Value

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)


# # add list item
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# remove list

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# loop
# thislist = ["apple", "banana", "cherry","priya"]
# for x in thislist:
#   print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

# short list
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# Case Insensitive Sort

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# revers order
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# copy list
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# join list
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)