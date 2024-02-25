import csv , os

with open("100MostStreamedSongs.csv", "r") as file:
  cn = csv.DictReader(file)
  
  # for row in cn: 
  #   print(row)
    # print (", ".join(row))

  # for row in cn:
  #   name = f"{row['Artist(s)']}"
  #   os.makedirs(f"strm/{name}", exist_ok=True)
    
  for row in cn:
    artist_name = row["Artist(s)"]
    song = row["Song"]
    
    path = os.path.join(f"strm/{artist_name}/", song)
    f = open(path, "w")
    f.close()
    
    # songf = f"strm/{artist_name}/{song}.txt"
    # os.popen(songf)
    
    # directory_name = f"strm/{artist_name}.txt"
    # os.makedirs(directory_name, exist_ok=True)

  # name = f"backup{random.randint(1,1000000000)}.txt"
  # os.popen(f"cp to.do backups/{name}")