
bmw=input("Do you want to do this program")
count=0
while (bmw=="Yes"):
  count=count+1
  yus=int(input("Please enter quant"))
  razeen=int(input("Please enter price"))
  math=(yus*razeen)
  if(math>10000):
    discount=.25
  else:
    discount=.10

  print(math)
  print(math*discount)
  print(math-(math*discount))
  bmw=input("Do you want to do this program again")
print(count)
