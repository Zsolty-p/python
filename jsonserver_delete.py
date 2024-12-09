import requests

id=input("Melyik kocsit szeretned torolni? ")
try:
        reply=requests.delete("http://localhost:3000/cars/" +id)

except:
        print("HIBA!!")
        exit()
if reply.status_code == 200:
        print(reply.status_code)
