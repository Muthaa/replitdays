# import requests # import the required library

# result = requests.get("https://randomuser.me/api/") # ask the site for data and store it in a variable

# print(result.json()) # interpret the data in the variable as json and print it.

# import requests, json #imports the json library

# result = requests.get("https://randomuser.me/api/")
# user = result.json() #a dictionary containing the user's data
# print(json.dumps(user, indent=2)) #outputs the json to the console with an indent to make it more readable.

# import requests, json 

# result = requests.get("https://randomuser.me/api/")
# user = result.json() 
# # print(json.dumps(user, indent=2)) 

# name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}""" # Get the first and last names from the results dictionary and assign to a variable

# print(name) # output the variable

# import requests, json #imports the json library

# result = requests.get("https://randomuser.me/api/")
# user = result.json() #a dictionary containing the user's data
# # print(json.dumps(user, indent=2)) #outputs the json to the console with an indent to make it more readable.

# name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}""" # Get the first and last names from the results dictionary and assign to a variable

# image = f"""{user["results"][0]["picture"]["medium"]}""" # Get the user's profile picture and assign to a variable, changing 'medium' to 'large' will make the image less pixelated
# picture = requests.get(image) #downloads the image
# f = open("image.jpg", "wb") # opens the image.jpg file for writing in binary (data of the image is added to the repl)
# f.write(picture.content) #writes the image to the file  
# f.close() #closes the file

# print(image) # output the variable

import requests, json

bots = []
for i in range(10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
    user = result.json()
    # print(json.dumps(user, indent=2))  
  
    for person in user['results']:
      name = f"""{person["name"]["first"]} {person["name"]["last"]}""" #creates a string with the name of the person
      bots.append(name)
      file = f"""{person["name"]["first"]} {person["name"]["last"]}.jpg"""
      picture = requests.get(person["picture"]["medium"])
      with open(file, "wb") as f:
        f.write(picture.content)
        f.close()
      print(f"Saved {filename}")
            
print(bots)
