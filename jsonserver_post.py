mport requests

car= {
        "id":"9",
        "brand":"Skoda",
        "model":"Octavia"
        "production_year": 2025,
        "convertible": False
        }
try:
        reply=requests.put("http://localhost:3000/cars/" json = car)

except:
        print("HIBA!!")
        exit()
print(reply.status_code)

