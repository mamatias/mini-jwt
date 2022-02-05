from mini_jwt import mini_encode
import jwt

payload = {"some":"payload"}
key = 'secretkey'



print(u"Sección propia")
print(mini_encode(payload, key).decode('utf-8'))
print(u"Sección Librería JWT")
print(jwt.encode(payload, key, algorithm="HS256"))

