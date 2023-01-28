from netmiko import Netmiko



cisco_sandbox_devices = {
    "ios": {
        "hostname": "sandbox-iosxe-latest-1.cisco.com",
        "port": 22,
        "username": "developer",
        "password": "C1sco12345",
        "device_type": "cisco_ios",
     }
    

}

Connection = Netmiko(cisco_sandbox_devices)