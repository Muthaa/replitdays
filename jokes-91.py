import requests, json, os
while True:
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
    
  joke = result.json()
  print(joke['joke'])
  
  print("""//////Dad Jokes.com////""")
  
  opt = input("\n(s)-save joke\n(l)-load jokes\n(n)-new joke\n\n > ")
  if opt == 's':
    with open ("jokes.txt" "a+") as file:
      file.append(joke['joke']+"\n")

  elif opt == "l":
    with open ("jokes.txt" "r") as file:
      file.seek(0)
      c = file.readlines()
      print(c)
  elif opt == "n":
    result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
    
    joke = result.json()
    print(joke['joke'])
  elif opt[0] == "e":
    exit()
    