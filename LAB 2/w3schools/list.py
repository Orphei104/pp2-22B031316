lambomodels = ["sestoelemento" , "avenatador" , "huracan" "miura" , "diablo", "veneno" , "centenario" , "countach", "sian"]
print(lambomodels)
print(len(lambomodels)) #length of the list
print(type(lambomodels)) #type fo list
print(lambomodels[1 : 3]) #range of items from to
print(lambomodels[-1]) #last item in list
print(lambomodels[:4]) #not included
print(lambomodels[5:]) #from included
if "diablo" in lambomodels :
    print ("Yes, 'diablo' is one of the Lamborghini car models")

bruh = ["tomato", "potato", "eggplant"]
bruh[1:3] = ["cucumber"]
bruh.insert(1, "onion") #put to a place where you want +address
bruh.append() #add to list
bruh.extend('''name of the another list to add''') #tuple can be added to
bruh.remove() #remove and "name of item "
bruh.pop(1) #remove with specifie index
del bruh[2] #also remove or deletes item
bruh.clear() #clears the lists content 


for x in bruh: #loop for for printing
    print (x)

for i in range(len(bruh)): #loop for
    print(bruh[i])

i = 0
while i < len(bruh):
    print(bruh[i])  #while loop using 
    i += 1

[print(i) for i in bruh] #shortcut for loop for

fruits  = [ "apple" , "banana" , "pineapple"]
newlist = []
for x in bruh:
    if "a" in x:
        newlist.append(x) #if a letter exist in word that if in list add it to newlist
print(newlist)
#of u can write for loop like this
newlist1 = [x for x in bruh if "a" in x]
newlsit2 = [x if x != "banana" else "orange" for x in fruits]

bruh.sort() #sorting the list (alphabetically)
bruh.sort(reverse = True) #sorting the lisrevertly

def myFunc(n) :
    return abs(n - 50)

numbers = [100 , 50 ,65 ,82, 23 ,59 ,47]
numbers.sort(key = myFunc) #sorting the list nearest to number 50
numbers.sort(key = str.lower)

#copy the list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
brolist = list.copy()
#copy the list without writing copy
brolist = list(list)

#joining lists
list11 = ["a" , "b" , "c"]
list22 = [1, 2, 3]
list33 = list11 + list22

for x in list22:
    list11.append(x)
print(list11)
# or you can write with extend
list11.extend(list22)
print(list11)

'''
append()	Adds an element at the end of the list
clear()   	Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''

#Exercises
fruits = ["apple", "banana" , "cherry"]
print(fruits[1])

#
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
