import json
data = {}
data['play_list'] = []
data['play_list'].append({
    'name': 'Track1',
    'website': ('pythonist.ru','fdsfds.f','hfjkfsdfssds.fd'),
    'from': 21
})
data['play_list'].append({
    'name': 'Track2',
    'website': ('pythonist.ru',),
    'from': 100
})
data['play_list'].append({
    'name': 'Track3',
    'website': ('pythonist.ru', 'djdhcccjskdh.ru'),
    'from': 50
})
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4)


with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['play_list']:
        print('Name: ' + p['name'])
        print('Website: ' + str(p['website']))
        print('From: ', p['from'])
        print('')

with open('data.txt') as json_file:
    data=json.load(json_file)
    for p in data['play_list']:
        a=(len(p['website']),p['name'])
        print(a, type(str(len((p['website'])))))
for p['website'] in data['play_list']:
    a=(max(str(len(p['website']))))
b=str
if max(str(len(p['website'])))==3:
    b=str(p['name'])
print(b)
print(a)


with open('data.txt') as json_file:
    data=json.load(json_file)
for p in data['play_list']:
    if p['name']=='Track3':
        print(p['name'])





