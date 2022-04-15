import json

fhand = open('./roster/roster_data_sample.json').read()

items = json.loads(fhand)
print(len(items))
for item in items[0:40]:
    print(item)
