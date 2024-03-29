import random
import string
import requests


for _x in range(200):
  f = open("proxies.txt", "r").readlines()
  for i in f:
    ip = i.split(":")[0]
    port = i.split(":")[1]
    if port == "80":
      proxyx = {
        "http": f"http://{ip}:{port}"
      }
    else:
      proxyx = {
        "https": f"http://{ip}:{port}"
      }
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=24))
    req = requests.get(
      f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    , proxies=proxyx)
    if req.status_code == 200:
      print(f"Valid | https://discord.gift/{code}")
    elif req.status_code == 429:
      print(f"Rate Limted | https://discord.gift/{code}")
    else:
      print(f"Invalid | https://discord.gift/{code}")