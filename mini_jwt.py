import base64, json
import hmac, hashlib

def mini_encode(data, key):
    '''
    Función encargada de generar un token JWT simple
    '''
    header = json.dumps({"typ":"JWT","alg":"HS256"}, sort_keys=False).replace(' ','')
    header_encoded = base64.urlsafe_b64encode(header.encode('utf-8'))

    payload = json.dumps(data, sort_keys=False).replace(' ','')
    payload_encoded = base64.urlsafe_b64encode(payload.encode('utf-8'))

    sign_encoded = mini_sign(key, b'.'.join([header_encoded, payload_encoded]))

    return b'.'.join([header_encoded, payload_encoded, sign_encoded])



def mini_decode(token):
    return



def mini_sign(key, content):
    '''
    Función encargada de firmar el contenido del token.
    key: llave secreta utilizada en la firma. Debe ser string
    '''
    key_encoded = key.encode('utf-8')

    sign = hmac.new(key_encoded, content, hashlib.sha256).digest().strip()
    return base64.urlsafe_b64encode(sign).rstrip(b'=')


