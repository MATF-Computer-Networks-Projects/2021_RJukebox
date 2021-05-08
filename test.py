import jwt
import os

token='f53dd840-bf6f-4668-927f-5626978660c1'
encoded_token = str(jwt.encode({'token': token}, 'm1gHtYs3cR3T', algorithm="HS256"))
print(encoded_token)