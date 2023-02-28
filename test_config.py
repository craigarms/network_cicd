from netmiko import ConnectHandler
from ruamel.yaml import YAML

r1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.100',
    'username': 'craig',
    'password': 'cisco',
}

net_connect = ConnectHandler(**r1)

output = net_connect.send_command('show ip int brief', use_textfsm=True)

print(output)