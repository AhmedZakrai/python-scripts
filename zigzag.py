def zigzag():
  return '*' * 10

x=4
while x>0 :
  print (' ' * x, zigzag())
  x-=1

print (zigzag())

x=1
while x<5 :
  print (' ' * x , zigzag())
  x += 1
