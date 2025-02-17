from netmiko import ConnectHandler
from getpass import getpass

kapcs = {
	"device_type":"mikrotik_routeros", 
	"host":"172.17.255.195",
	"username":"admin",
	"password":getpass()
}
 
cmd = "/ip address print"

with ConnectHandler(**kapcs) as k:
	out = k.send_command(cmd)
print(out)
