#while loop
i = 1
while i < 6:
  print(i)
  i += 1

#while with using break
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#while with using continue
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#while with else
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")