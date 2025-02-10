import requests

head={'x-api-key' : 'DEMO-API-KEY'}
try:
	reply = requests.get("https://api.thecatapi.com/v1/breeds", headers=head)
except:
	print("Valami nem jo.")
	exit()
if reply.status_code == 200:
	print(reply.json)
