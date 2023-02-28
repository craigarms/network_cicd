from netmiko import ConnectHandler
from jinja_renderer import main
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description = 'YAML to config with Jinja',
                                     prog = 'jinja_renderer.py')
parser.add_argument("tpl", help="Jinja template file")
parser.add_argument("config", help="YAML Dictionary file")

args = parser.parse_args()

tpl = str(Path(args.tpl)).replace('\\','/')
config = str(Path(args.config)).replace('\\','/')

r1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.100',
    'username': 'craig',
    'password': 'cisco',
}

config = main(tpl, config)

commands = config.split('\n')

net_connect = ConnectHandler(**r1)
 
output = net_connect.send_config_set(commands)

print(output)