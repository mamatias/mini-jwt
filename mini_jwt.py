import base64, json
import hmac, hashlib
from time import time

def mini_encode(data, key, exp=600):
    '''
    Generate a simple jwt
    data: Data to encode in token. User for example. Must be a python dictionary.
    key: The key to sign the token.
    exp: Expiration of the token expressed in seconds from NOW
    '''
    header = json.dumps({"typ":"JWT","alg":"HS256"}, sort_keys=False).replace(' ','')
    header_encoded = base64.urlsafe_b64encode(header.encode('utf-8'))

    # Adding expiration time (date)
    data['exp'] = '{0}'.format(time()+exp)
    

    payload = json.dumps(data, sort_keys=False).replace(' ','')
    payload_encoded = base64.urlsafe_b64encode(payload.encode('utf-8')).rstrip(b'=')

    sign_encoded = mini_sign(key, b'.'.join([header_encoded, payload_encoded]))

    return b'.'.join([header_encoded, payload_encoded, sign_encoded])



def mini_decode(token, key):
    '''
    Decode the jwt token and returns a python dictionary with data
    
    token: JWT token in string format
    key: Secret key for signing (check sign)
    '''
    tkn = token.split('.')
    if len(tkn) != 3:
        return None

    tr = {}
    tr['header'] = base64.urlsafe_b64decode(tkn[0].encode('utf-8'))
    claims = tkn[1].encode('utf-8')
    if len(claims)%4 == 1:
        claims = claims+b'==='
    elif len(claims)%4 == 2:
        claims = claims+b'=='
    if len(claims)%4 == 3:
        claims = claims+b'='

    tr['claims'] = base64.urlsafe_b64decode(claims)

    # Correctly signed?
    local_sign = mini_sign(key, b'.'.join([tkn[0].encode('utf-8'), tkn[1].encode('utf-8')]))
    if tkn[2] == local_sign.decode('utf-8'):
        tr['verified'] = True
    else:
        tr['verified'] = False

    # Expired?
    claim_dict = json.loads(tr['claims'])
    exp_date = claim_dict.get('exp')

    tr['expired'] = True
    try:
        if exp_date:
            if float(exp_date)-time() >= 0:
                tr['expired'] = False
    except:
        pass
    
    return tr



def mini_sign(key, content):
    '''
    Sign the token content (xxxxxx.yyyyyyy). Returns the sign encoded and clean from padding (=)
    key: llave secreta utilizada en la firma. Debe ser string
    content: The content part of the token made by the header and the claim or payload. The content must be 
    encoded as bytes.
    '''
    key_encoded = key.encode('utf-8')

    sign = hmac.new(key_encoded, content, hashlib.sha256).digest().strip()
    return base64.urlsafe_b64encode(sign).rstrip(b'=')


