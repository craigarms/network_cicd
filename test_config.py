from netmiko import ConnectHandler
from ruamel.yaml import YAML
import json

r1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.100',
    'username': 'craig',
    'password': 'cisco',
}
config = 'Configs/r1.yml'

net_connect = ConnectHandler(**r1)
output = net_connect.send_command('show ip int brief', use_textfsm=True)

yaml = YAML()

with open(config) as f:
    y = yaml.load(f)
    json = json.loads(json.dumps(y))

for i in json['interfaces']:
    for j in output:
        if i['name'] == j['intf']:
            if j['ipaddr'] not in i['ip']:
                exit(1)
            if i['activate']:
                if j['status'] != 'up':
                    exit(1)
            else:
                if 'down' not in j['status']:
                    exit(1)
