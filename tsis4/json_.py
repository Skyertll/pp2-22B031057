import json

with open('C:\\Users\\skyer\\Downloads\\json.json', 'r') as f:
    data = json.load(f)


interfaces = []
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    descr = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes']['speed']
    mtu = interface['l1PhysIf']['attributes']['mtu']
    interfaces.append((dn, descr, speed, mtu))

header_format = '{:<50} {:<20} {:<8} {:<6}'
row_format = '{:<50} {:<20} {:<8} {:<6}'

print(header_format.format('DN', 'Description', 'Speed', 'MTU'))
print('=' * 80)

for interface in interfaces:
    print(row_format.format(*interface))