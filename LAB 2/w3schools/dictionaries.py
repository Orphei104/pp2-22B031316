#dictionaries
dict = {
    "brand" : "Ford"
    "model" : "Mustang"
    "year " : "1964"
}

thisdict = dict(name = "John", age = 36, country = "Norway")

x = thisdict["name"]
x = dict.get("model") #ways to get value in dictionary

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#way to change original value in dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2022
print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}                                   #putting or updating a value in dict
thisdict.update({"year": 2020})
thisdict.update({"color": "red"}) # or you can use this

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964              #here pop removes an value
}
thisdict.pop("model")
print(thisdict)

'''
clear()	      Removes all the elements from the dictionary
copy()	      Returns a copy of the dictionary
fromkeys()	  Returns a dictionary with the specified keys and value
get()	      Returns the value of the specified key
items()	      Returns a list containing a tuple for each key value pair
keys()	      Returns a list containing the dictionary's keys
pop()	      Removes the element with the specified key
popitem()	  Removes the last inserted key-value pair
setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	  Updates the dictionary with the specified key-value pairs
values()	  Returns a list of all the values in the dictionary
'''

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])
