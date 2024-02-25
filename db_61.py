# from replit import db
# import os , datetime
# def menu():
#   print("1.Add \n2.View")
# while True:
#   print("""
#       (((((ONe MedIa)))))
#   """)
#   menu()
#   s = int(input("> "))
#   if s == 1:
#     os.system("clear")
#     menu()
#     tw = input("Enter tw : ")
#     timestamp = datetime.datetime.now()
#     db[timestamp] = [tw]
#     c = input("add? > ").lower()
#     if c[0] == "n":
#       continue
#   elif s == 2:
#     os.system("clear")
#     menu()
#     try:
#       keys = db.keys()
#       for i in range(0,10,-1):
#         for key in keys:
#           print(f"""{key}: {db[key]}""")
#       a = input("more? > ").lower()
#       if a[0] == "n":
#         continue
      
#     except Exception as e:
#       print(e)
    
from replit import db
import os, datetime

def menu():
    print("1. Add\n2. View")

while True:
  os.system("clear")
  print("""
        ((((ONe MedIa))))
  """)
  menu()
  s = int(input("> "))

  if s == 1:
      while True:
        os.system("clear")
        menu()
        tw = input("Enter tw: ")
        timestamp = datetime.datetime.now()
        key = f"mes{timestamp}"
        db[key] = tw
        c = input("add more? (y/n) > ").lower()
        if c[0] == "n":
            break  
  elif s == 2:
    while True:
      try:      
        keys = list(db.keys())[::-1] 
        counter = 0
        for i in keys:
          print(db[i])
          print()
          counter += 1
          if (counter % 10 == 0):
            a = input("more 10?: ").lower()
            if(a[0]=="n"):
              break           
   
      except Exception as e:
          print(e)


# from replit import db
# db["t1"] = "h3110"
# db["login1"] = "david"
# db["login2"] = "pamela"
# db["login3"] = "sian"
# db["login4"] = "ian"
# db["david"] = {"username": "dmorgan", "password":"baldy1"}

# try:
#   keys = db.keys()
#   for key in keys:
#     print(f"""{key}: {db[key]}""")
#   valeu = db["t1"]
#   print(valeu)
#   matches = db.prefix("login")
#   print(matches)
#   value = db["david"]
#   print(value["password"])
# except Exception as e:
#   print(e)

