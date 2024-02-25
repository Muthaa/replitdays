import os , time
inv = []
try:
  with open("inv.txt", "r") as file:
    inv = file.read().splitlines()
except Exception as e:
  print(e)
  
def banner():
  print("""
        🌟Crusader Inventory🌟🌟🌟🌟🌟
          🌟🌟🌟🌟
  """)

def add():
  banner()
  itm = input("add item > ")
  inv.append(itm)
  print()
  
  print(itm,"added")
  print()
  done = input("done? ").lower()
  if done[0] == "y":
    os.system("clear")
    return
  else:
    os.system("clear")
    add()
  
def remove():
  os.system("clear")
  banner()
  print()
  try:
    deli = input("which item? > ")
    if deli in inv :
      inv.remove(deli)
      print(f"{deli} removed")
      time.sleep(1)
      return
    if deli == "return":
      return
    else:
      print("not in list")
  except Exception as e:
    print(e)
    

def view():
  os.system("clear")
  banner()
  print()
  res = {i:inv.count(i) for i in inv}
  for key ,value in res.items():
    print(key,"\t",value)
  print()
  time.sleep(4)
  os.system("clear")

def menu():
  st = ["Add", "View", "Remove"]
  for i,item in enumerate(st):
    print(i,item)
  choice = int(input(">"))
  if choice == 0:
    add()
  elif choice == 1:
    view()
  elif choice == 2:
    remove()

while True:
  os.system("clear")
  banner()  
  menu()
  try:
      with open("inv.txt", "w") as file:
          file.write('\n'.join(inv))
  except Exception as e:
      print(e)

  os.system("clear")