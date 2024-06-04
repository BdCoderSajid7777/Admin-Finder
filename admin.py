import requests
site = input("Entet target site: ")

with open('admins.txt','r') as f:
  admins = f.read().splitlines()
  for admin in admins:
   url = f"{site}/{admin}"
   response = requests.get(url)
   if response.status_code ==200:
     print(f"\033[0;32m{url} found")
   else:
    print(f"\033[0;31m{url} not found")