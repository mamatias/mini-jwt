from mini_jwt import mini_encode, mini_decode

payload = {
    "user":"usuario testt"
}
key = 'secretkeyyy'



print(u"Sección propia")
my_jwt = mini_encode(payload, key, exp=3).decode('utf-8')
print(my_jwt)

# testing decode
print(mini_decode(my_jwt, key))