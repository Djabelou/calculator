print("A simple calculator.")
print("")
finished = False

def calc():
  int1 = input("Number 1>")
  int2 = input("Number 2>")
  int1=int(int1)
  int2=int(int2)
  num1 = str(int1)
  num2 = str(int2)
  if ope =="a":
    res=int1+int2
    operator= "+"
  elif ope == "s":
    res=int1-int2
    operator= "-"
  elif ope == "m":
    res=int1*int2
    operator= "*"
  elif ope =="d":
    res=int1/int2
    operator= "/"
  resu=str(res)
  print("")
  print(num1 + operator + num2 + "=" + resu)

while finished == False:
  print("")
  ope=input("Would you like to (a)dd, (s)ubstract, (m)ultiply, (d)ivide, a(v)erage or (stop) ?>")
  if ope == "a":
    calc()
  elif ope =="s":
    calc()
  elif ope =="m":
    calc()
  elif ope =="d":
    calc()
  elif ope =="v":
    avstop = False
    counter=0
    sum = 0
    while avstop == False:
      counter=counter+1
      print("")
      print("Enter the number, then press enter. To stop, press (s)")
      intx = input("Number " + str(counter) +": ")
      if intx != "s":
        intx = int(intx)
        data = []
        data.append(intx)
        sum = sum + intx
      elif intx == "s":
        avstop = True
    res = sum/counter
    print("")
    print("The average of "+str(sum)+"/"+str(counter)+"="+str(res))
  elif ope == "stop":
    finished = True
    print("Good bye")
  else:
    print("I did not understand "+ "'"+ope+"'")
#print("The result of the addition " + in1 + " + " + in2 + " is " + add)
#print(in1 + " + " + in2 + " = " + add)
