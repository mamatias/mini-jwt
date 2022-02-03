import base64, json
from email import header

def mini_encode(data):
    head = {"typ":"JWT","alg":"HS256"}
    header_encoded = base64.urlsafe_b64encode(json.dumps(head, sort_keys=False).replace(' ','').encode('utf-8'))
    # payload_encoded = base64.urlsafe_b64encode(json.dumps({"some": "payload"}, sort_keys=False).replace(' ','').encode('utf-8'))
    payload_encoded = base64.urlsafe_b64encode(json.dumps(data, sort_keys=False).replace(' ','').encode('utf-8'))
    signature = ''
    return header_encoded.decode('utf-8')+'.'+payload_encoded.decode('utf-8')+'.'+signature

def mini_decode(somebytes):
    return base64.urlsafe_b64decode(somebytes)