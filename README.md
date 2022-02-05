# Mini JWT

There are a lot of good implementations of JWT. PyJWT the best
of all in my opinion, but because I'm using jython 2.7
I needed something simplier and usefull in that enviroment.
So I implement this little JWT interpretation.

## How to use

```
from mini_jwt import mini_encode

payload = {"some":"payload"}
key = 'somekey'

# for python 3.X
print(mini_encode(payload, key).decode('utf-8'))

# for python 2.7
print mini_encode(payload, key).decode('utf-8')
```