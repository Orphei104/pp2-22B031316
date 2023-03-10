#Modules
import mymodule
def greeting(name):
  print("Hello, " + name)

mymodule.greeting("Jonathan")

import mymodule as mx

a = mx.person1["age"]
print(a)

#Using the dir() Function
import platform

x = dir(platform)
print(x)


#Import From Module
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}