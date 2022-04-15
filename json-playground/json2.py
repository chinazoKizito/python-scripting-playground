# library for reading and parsing and manipulating JSON object
import json

fhand = open('./my-family.json').read()

family = json.loads(fhand)

print("JSON object enclosed in list: ", family)
print("User Counts: ", len(family))

for item in family:
    print('id:', item['id'])
    print('Name:', item['name'])
    print('Attribute:', item['x'])
