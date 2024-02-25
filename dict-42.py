moeo = {}
def printe():
  print(f"Beast\t\tElement\t\tClass\tHP\t\tMP")
  for key, value in moeo.items():
    print(f"""{key:^12}|{value["Element"]:^10}|{value["Class"]:^6}|{value["Hp"]:^6}|{value["Mp"]:^6}""")

def bar():
  print("""
             ****Moeo Beasts***
        ---Just on more Challenge---
  """)
bar()
while True:
  print("Add your Beast!")
  Beast = input("Beast > ").title()
  Element = input("Element > ").strip().capitalize()
  Class = input("Class > ").title()
  Hp = int(input("Hp > "))
  Mp = int(input("Mp > "))
  
  moeo[Beast] = {"Element": Element, "Class": Class, "Hp": Hp, "Mp": Mp }
  print()
  
  if Element=="Earth":
    print("\033[32m", end="")
  elif Element=="Air":
    print("\033[37m", end="")
  elif Element=="Dark":
    print("\033[40m", end="")
  elif Element=="Fire":
    print("\033[31m", end="")
  elif Element=="Water":
    print("\033[34m", end="")
  else:
    print("\033[93m", end="")
  
  print("----------")
  print()
  printe()
  print()

  print("\033[0m")
  add = input("Again? y/n > ").lower()
  if add[0] == "n":
    break
  print()
  


  
# clue = {}
# def prettyPrint():
#   print()
  
#   for key, value in clue.items():
#     print(key, end=": ")
#     for subKey, subValue in value.items():
#       print(subKey, subValue, end=" | ")
#     print()
    
# while True:
#   name = input("Name: ")
#   location = input("Location: ")
#   weapon = input("Weapon: ")

#   clue[name] = {"location": location, "weapon":weapon} 

#   prettyPrint()

# john = {"daysCompleted": 46, "streak": 22}
# janet = {"daysCompleted": 21, "streak": 21}
# erica = {"daysCompleted": 75, "streak": 6}

# courseProgress = {"John":john, "Janet":janet, "Erica":erica}

# print(courseProgress["Erica"]["daysCompleted"])
# print(courseProgress["Janet"]["streak"])

# print("""
#            ****Moeo Beasts***
#       ---Just on more Challenge---
# """)
# moeo = {"Beast": None, "Element": None, "class": None, "Hp": None, "Mp": None }

# for key in moeo.keys():
#   moeo[key] = input(f"{key} > ").strip().capitalize()
# print()

# if moeo["Element"]=="Earth":
#   print("\033[32m", end="")
# elif moeo["Element"]=="Air":
#   print("\033[37m", end="")
# elif moeo["Element"]=="Dark":
#   print("\033[40m", end="")
# elif moeo["Element"]=="Fire":
#   print("\033[31m", end="")
# elif moeo["Element"]=="Water":
#   print("\033[34m", end="")
# else:
#   print("\033[93m", end="")

# for key ,value in moeo.items():
#   print(f"{key}: {value}")

    