# Mini JWT

There are a lot of good implementations of JWT. PyJWT the best
of all in my opinion, but because I'm using jython 2.7
I needed something simplier and usefull in that enviroment.
So I'm implementing this little JWT interpretation.

## How to use

```python
from mini_jwt import mini_encode

payload = {"some":"payload"}
key = 'somekey'

# for python 3.X
my_jwt = mini_encode(payload, key).decode('utf-8')
print(my_jwt)

# for python 2.7
print my_jwt


# testing decode
# for python 3.X
print(mini_decode(my_jwt, key))

# for python 2.7
print mini_decode(my_jwt, key)
```