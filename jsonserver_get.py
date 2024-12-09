import requests

id=input("Melyik kocsit keresed? ")
try:
	reply=requests.get("http://localhost:3000/cars/" +id)

except:
	print("HIBA!!")
	exit()
if reply.status_code == 200:
	print(reply.json())
print(reply.status_code)
