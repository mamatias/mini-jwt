import base64, json
import hmac, hashlib

def mini_encode(data, key):
    key_encoded = key.encode('utf-8')
    header = json.dumps({"typ":"JWT","alg":"HS256"}, sort_keys=False).replace(' ','')
    header_encoded = base64.urlsafe_b64encode(header.encode('utf-8'))
    payload = json.dumps(data, sort_keys=False).replace(' ','')
    payload_encoded = base64.urlsafe_b64encode(payload.encode('utf-8'))
    sign = hmac.new(key_encoded, header_encoded+b'.'+payload_encoded, hashlib.sha256).digest().strip()
    sign_encoded = base64.urlsafe_b64encode(sign).rstrip(b'=')
    return b'.'.join([header_encoded, payload_encoded, sign_encoded])

# from codecs import encode, decode
# import requests
# import hashlib
# import hmac

# # read the assymetric key
# with open('public.pem', 'rb') as f:
#     key = f.read()

# # create an appropriate JSON object for header
# header = b'{"typ":"JWT","alg":"HS256"}'
# header = encode(header, 'base64').strip()

# # create an appropriate JSON object for payload
# payload = b'{"login":"admin"}'
# payload = encode(payload, 'base64').strip()

# # sign the payload
# sig = hmac.new(key, header + b'.' + payload, hashlib.sha256).digest().strip()
# sig = encode(sig, 'base64').strip()

# # print the json token
# jwt = '{}.{}.{}'.format(header.decode(), payload.decode(), sig.decode())
# print(jwt)