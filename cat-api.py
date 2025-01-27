import requests

url="https://api.catapi.com/v1/breeds"
head={'x-api-key' : 'DEMO-API-KEY'}
try:
	reply = requests.get(url, headers=head)
except:
	print("Valami nem jo.")
	exit()
if reply.status_code == 200:
	print(reply.json)
