print("Identity matrix") 
size = 2

for row in range(size, 0, -1):
  for col in range(1, size+1):
    if (row == col):
      print("1 ", end=" ")
    else:
      print("0 ", end=" ")
  print() 
