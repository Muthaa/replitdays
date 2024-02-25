from replit import db
import datetime, os, time, random

def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def viewEntry():
  keys = db.keys()
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break

def acess():
  global salt 
  user  = input("set user name > ").capitalize()
  passw = input("set pasword > ")
  salt = random.randint(1000,9999)
  passw =f"{passw}{salt}"
  passw = hash(passw)
  db[user] = {"password":passw,"salt":salt}

def acessl():
  usern = input("Username: ").capitalize()
  keys = db.keys()
  if usern not in keys:
    print("ERROR: Username does not exists")
    return
    
  password = input("Password: ")
  salt = db[usern]["salt"]
  password = f"{password}{salt}"
  password = hash(password)
  
  if password != db[usern]["password"]:
    print("Incorrect")
    exit()
    
# for keys in db.keys.(): first run
# if usr not exists run create else cont
print("LOgin Control")
keys = db.keys()
if len(keys) == 0:
  acess()
else:
  acessl()
  
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()