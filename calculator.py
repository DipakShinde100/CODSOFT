def calculator():
  num1=float(input("enter the first number: "))
  num2=float(input("enter the second number: "))
  print("select the basic operations that you want to perform: ")
  print("1.addition")
  print("2.subtraction")
  print("3.multiplication")
  print("4.division")

  choice=input("enter the choice of operation (1/2/3/4): ")

  if choice=='1':
    result=num1+num2
    print(f"addtion of {num1} + {num2} = {result}")

  elif choice=='2':
    result=num1-num2
    print(f"subtraction of two number {num1} - {num2} = {result}")

  elif choice=='3':
    result=num1*num2
    print(f"subtraction of two number {num1} * {num2} = {result}")

  elif choice=='4':
    if num2 != 0:
      result=num1/num2
      print(f"subtraction of two number {num1} / {num2} = {result}")
    else:
      print("the number 0 is invalide for computaion!")
  else:
    print("invalide input! please enter the valide input as mention above")


calculator()
  
