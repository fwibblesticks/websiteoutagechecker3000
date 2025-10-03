'''
hello
this script is for seeing if a website is down or not
hope you like uhmmm like the script
ai helped me with strftime cause a wise man once said:
getting the time in programming fucking sucks.
'''
import requests
from datetime import datetime

# grab time
now = datetime.now()
tm = now.strftime('%Y-%m-%d %H:%M:%S') + f".{now.microsecond // 1000:03d}"
try:
    # initial request thingymabob and url define
    url = input("input le url (including https://):")
    response = requests.get(url)

    # request
    print(f"status: {response.status_code}")
    if response.status_code == int("200"):
        print("basically: fine")
    else:
        print("basically: its down")
    # time
    print("request send:", tm)
except:
    print(" input the website correctly twin! error was found ")


