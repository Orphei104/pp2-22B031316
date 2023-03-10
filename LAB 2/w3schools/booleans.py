a = 100
b = 99
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#ALL FALSE
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})



#ALL TRUE
bool("abc")
bool(123)
bool(["guava","pineaple", "watermelon"])



class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


x = 200
print(isinstance(x, int))

x = "Bugatti"
print(isinstance(x , str))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))



print (10 > 9)
# True


print (10 == 9)
# False


print (10 < 9)
# False


print (bool("abc"))
# True


print (bool(0))
# False