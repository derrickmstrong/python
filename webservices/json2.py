# JSON
import json # REQUIRED

# Simple JSON object
data = '''{
    "name": "Derrick",
    "phone": {
        "type": "intl",
        "number": "+1 234 567 7899"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Phone Number:', info["phone"]["number"])

print('\n')

# Complex JSON Object using a list
data = '''[
    {
        "id": "003",
        "name": "Mike",
        "age": 7
    },
    {
        "id": "004",
        "name": "Ike",
        "age": 11
    }
]'''

info = json.loads(data)
print('User Count:', len(info))
print('\n')
for i in info:
    print('ID:', i['id'])
    print('Name:', i['name'])
    print('Age:', i['age'])
    print('\n')