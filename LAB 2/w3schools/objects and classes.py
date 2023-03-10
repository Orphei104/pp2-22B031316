#Class
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

#Create a Class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

KING = Person("Arthas", 24)

print(KING.name)
print(KING.age)

#Object Methods
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

KING = Person("Arthas", 24)
KING.myfunc()
