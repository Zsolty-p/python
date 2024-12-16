import requests
URL = "https://postman-echo.com/basic-auth"
try:
	r = requests.get(URL, auth=("postman","password"))
except:
	print("Hiba!")
	exit()
if r.status_code == 200:
	print(r.status_code)
	print(r.json())

