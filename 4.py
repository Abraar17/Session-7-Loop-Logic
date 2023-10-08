
bmw=input("Do you want to do this program")
count=0
while (bmw=="Yes"):
  yus=input("Please enter last name")
  razeen=int(input("Please enter hours"))
  yushusband=int(input("Please enter pay"))
  if (razeen>40):
      razeen=razeen-40
      ot=razeen*(yushusband*1.5)
      
  gp=razeen*yushusband
  print(yus)
  print(gp)
  count=count+1
  bmw=input("Do you want to do this program again")
print(count)
