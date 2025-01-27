import requests

URL="https://api.thecatapi.com/v1/breeds"
h={'x-api-key': 'DEMO_API_KEY'}
try:
	reply=requests.get(URL, headers=h)
except:
	print("HIBA!!")
	exit()
if reply.status_code == 200:
	print(reply.json())
print(reply.status_code)
