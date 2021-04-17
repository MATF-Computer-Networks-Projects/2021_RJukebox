import json
import names
import hashlib

data = {}
data['users'] = []

for i in range(50):
    data['users'].append({
        'user':names.get_full_name(),
        'password':hashlib.sha224(b"12345").hexdigest()
    })

with open("users.json", 'w') as outfile:
    json.dump(data, outfile)