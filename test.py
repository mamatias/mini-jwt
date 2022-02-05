import base64
from mini_jwt import mini_encode
import jwt

payload = {"some":"payload"}
key = 'matiastorres'



print(u"Sección propia")
print(mini_encode(payload, key).decode('utf-8'))
print(u"Sección Librería JWT")
print(jwt.encode(payload, key, algorithm="HS256"))

