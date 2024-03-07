import os , time , random
def menu():
  print("""
     ⚔️  BATTLE TIME ⚔️ 
          Rager Games
    
    """)
def roller(nside):
  rn = random.randint(1,nside)
  return rn
  
def health():
  health = ((roller(6) * roller(12))/2) + 10
  return health
def stat():
  stats = ((roller(6) * roller(8))/2) + 12 
  return stats
  
menu()

p1n = input("Name your Legend:")
p1c = input("Character type (Human ,Elf, Wizard, Orc):")
print("\033[31m",p1n)
print("\033[31m",p1c)
p1h = health()
p1s = stat()
print("\033[33m","Health:","\033[35m",p1h)
print("\033[33m","Mana:","\033[35m",p1s)
print("\033[0m")

p2n = input("Name your Legend:")
p2c = input("Character type (Human ,Elf, Wizard, Orc):")
print("\033[31m",p2n)
print("\033[31m",p2c)
p2h = health()
p2s = stat()
print("\033[33m","Health:","\033[35m",p2h)
print("\033[33m","Mana:","\033[35m",p2s)
print("\033[0m")

time.sleep(2)
# os.system("clear")
round = 1
while True:
  print("""
    ⚔️  BATTLE TIME ⚔️ 
          Round""",round)
  print(p1n, p1h)
  print(p2n, p2h)
  time.sleep(1)
  
  p1r = roller(6)
  time.sleep(1)
  p2r = roller(6)
  time.sleep(1)
  
  # amg = (p1s - p2s) + 1
  # damage = random.randint(1,amg)
  
  p1d = random.randint(int(p1r), int(p1s))
  p2d = random.randint(int(p2r), int(p2s))
  
  if p1r > p2r:
    print(p1n,"lands a hit")
    p2h = p2h - p1d
    time.sleep(1)
    print(p2n," has taken damage","-",p1d)
    time.sleep(1)
    print(p2n, "Health:","\033[31m",p2h,"\033[0m")
    print(p1n, "Health:", p1h)
    print()
          
  else:
    print(p2n,"lands a hit")
    p1h = p1h - p2d
    time.sleep(1)
    print(p1n," has taken damage","-",p2d)
    time.sleep(1)
    print(p1n, "Health:","\033[31m",p1h,"\033[0m")
    print(p2n, "Health:", p2h)
    print()
  
  print(p1n, p1h)
  print(p2n, p2h)
  time.sleep(3)
  
  if p1h <= 0:
    print(p1n,"is down!!!", "\033[32m","WINNER",p2n.upper(),"Crowd goes aaaaah")
    print(p2n, "Health:", p2h)
    print(p1n, "Health:", p1h)
    exit()
  elif p2h <= 0:
    print(p2n,"is down!!!", "\033[32m","WINNER",p1n.upper(),"\033[0m","Crowd goes aaaaah")
    print(p1n, "Health:", p1h)
    print(p2n, "Health:", p2h)
    exit()
  else:
    round +=1
    time.sleep(2)
    print()
    print("👉👉👉Next bout👉👉👉")
  
  time.sleep(2)
  # os.system("clear")
    