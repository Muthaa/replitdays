import os, time

todo = []

def listview():
  os.system("clear")
  print("todo list")
  print()
  counter = 1
  for item in todo:
    print(f"{counter}: {item}")
    counter+=1
  time.sleep(1)
       
while True:
  print("""
     -------  -----------  ------
            To           Do
                  List
                  
        ******** Editor ********
        
""") 
  menu = input("1: Add Item\n2: Remove Item\n3: Edit Items\n4: Show Items\n5: Erase List\n> ")
  if menu == "1":
    item = input("Item > ").title()
    if item in todo:
      print("Already Exists")
    else:
      todo.append(item)
  elif menu== "2":
    listview()
    item = input("Item > ").title()
    check = input("Are you sure you want to remove this?\n")
    if check[0]=="y":
      if item in todo:
        todo.remove(item)
      else:
        print(f"{item} not in list")
  elif menu=="3":
    listview()
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(todo)):
      if todo[i]==item:
        if todo[i] == new or new == item:
          print("Already Exists")
        else:
          todo[i]=new
  elif menu == "4":
    listview()
  elif menu =="5":
    todo = []
  time.sleep(1)
  os.system("clear")