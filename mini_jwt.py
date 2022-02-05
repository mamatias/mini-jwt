import base64, json
import hmac, hashlib

def mini_encode(data, key):
    '''
    Función encargada de generar un token JWT simple
    '''
    key_encoded = key.encode('utf-8')

    header = json.dumps({"typ":"JWT","alg":"HS256"}, sort_keys=False).replace(' ','')
    header_encoded = base64.urlsafe_b64encode(header.encode('utf-8'))

    payload = json.dumps(data, sort_keys=False).replace(' ','')
    payload_encoded = base64.urlsafe_b64encode(payload.encode('utf-8'))

    sign = hmac.new(key_encoded, header_encoded+b'.'+payload_encoded, hashlib.sha256).digest().strip()
    sign_encoded = base64.urlsafe_b64encode(sign).rstrip(b'=')

    return b'.'.join([header_encoded, payload_encoded, sign_encoded])