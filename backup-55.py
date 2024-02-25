import os

print(os.listdir()) # Lists all the files in the current directory. Useful for checking that a file is in the folder we think it is.

files = os.listdir()
# if "quickSave.txt" not in files:
#   print("Error: Quick Save not found.")
#Checks if a file is in a directory and outputs an error if not.

data = "some Data"
with open("two.txt","a+") as file:
  file.write(data + "\n")
  
if "Backup" not in files:
  os.mkdir("Backup")
else:
  os.popen("cp two.txt  Backup")
  print("synchronized..")
  # name = f"backup{random.randint(1,1000000000)}.txt"
  # os.popen(f"cp to.do backups/{name}")
    
