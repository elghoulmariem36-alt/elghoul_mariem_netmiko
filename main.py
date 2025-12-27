iprint("Hello, Git!")
from netmiko import ConnectHandler

def acces_netmiko():
    router = {
        "device_type": "cisco_xr",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }

    connexion = ConnectHandler(**router)

    clock = connexion.send_command("show clock")
    print("Date du routeur :")
    print(clock)
  
    interfaces = connexion.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)

    connexion.disconnect()

print("Hello, Git!")
