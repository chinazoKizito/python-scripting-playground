# library for reading and parsing and manipulating JSON object in python
import json

# Json object
data = """{"name": "Kizito", 
"phone": {"type": "intl", "number": "+234 903 445 8299"},
"age": {"type": "intl",  "value": "25"},
"email": {"hide": "yes"},
"nationality": "Nigerian",
"marital-status": "Single",
"job": "Student"
}
"""

# Loading and accessing different contents of the data
info = json.loads(data)
print("Name: ", info['name'])
print("Nigerian Phone No: ", info['phone']['number'])
print("Email Hide: ", info['email']['hide'])
print("Employable: ", info['job'])
print('Marital-Status: ', info['marital-status'])
print('Nationality: ', info['nationality'])
print('Age: ', info['age']['value'])