#Scope
def myfunc():
  x = 300
  print(x)

myfunc()

#Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#Global Keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)
