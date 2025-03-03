import requests

url="https://172.19.255.216/restconf/data/ietf-interfaces/interfaces=GigabitEthernet1"
h={"Accept":"application/yang-data+json"}
a=("admin","admin")
#try:
r=requests.get(url,headers=h,auth=a,verify=False)
#except:
#	print("Valami nem jo.")
if r.status_code == 200:
	print(reply.json)
print(r.status_code)
