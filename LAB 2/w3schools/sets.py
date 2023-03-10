myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #the same u can use function remove
print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
print(x)          #remoce random item with pop
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()                 #clears and shows the existance
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset                       #completely deletes the set
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) #same u can use "update"
print(set3)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"} #will keep only that apears in both sets
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"} #this type of function is reverse of intersection
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

'''  
add()	                      Adds an element to the set
clear()	                      Removes all the elements from the set
copy()	                      Returns a copy of the set
difference()	              Returns a set containing the difference between two or more sets
difference_update()	          Removes the items in this set that are also included in another, specified set
discard()	                  Remove the specified item
intersection()	              Returns a set, that is the intersection of two other sets
intersection_update()	      Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	              Returns whether two sets have a intersection or not
issubset()	                  Returns whether another set contains this set or not
issuperset()	              Returns whether this set contains another set or not
pop()	                      Removes an element from the set
remove()	                  Removes the specified element
symmetric_difference()	      Returns a set with the symmetric differences of two sets
symmetric_difference_update() inserts the symmetric differences from this set and another
union()	                      Return a set containing the union of sets
update()	                  Update the set with the union of this set and others
'''
