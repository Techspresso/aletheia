import base64
import binascii

def base64_decode(query):
    try: 
        return base64.b64decode(query, validate=True).decode()
    except binascii.Error:
        raise ValueError("Invalid base64 string: " + query)