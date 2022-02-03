from base64 import encode
from mini_jwt import mini_encode, mini_decode
import jwt

payload = {"some": "payload"}

print(u"Sección propia")
print(mini_encode(payload))
print(u"Sección Librería JWT")
print(jwt.encode(payload, "secret", algorithm="HS256"))