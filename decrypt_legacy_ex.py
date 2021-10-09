import base64
import zlib
import json
import hashlib
from Cryptodome import Random   
from Cryptodome.Cipher import AES

class CDNKeys:
    key460 = "uRqLnp6p9WUrTJ6nNXlv7z9VZRjbXvRFKEcF/spEn9k="
    key470 = "DJ1LTHLgxRNq7v7fsyG3AQONlsdN49gJ+oY9UuVCSzQ="
    key500 = "CADqND0WPwViwTPzhAiOjR/IrB5TCFInww+k1cmUg70="
    key510 = "GgkY5gFWXzqqxaqUFGb2x+CzdGuJ00nJ2XwV+AoBwuc="
    key520 = "gqONp7FrUqdbp3hS/iMmhphUQ5yPH8eKlkDQk+2QVkI="
    legacykey = b"5BCC2D6A95D4DF04A005504E59A9B36E"
 
decr_key = base64.b64decode(CDNKeys.legacykey)

def decrypt(body):
        cipher = AES.new(decr_key, AES.MODE_ECB)
        encbody = body[8:]
        b64_body = base64.b64decode(raw)
        
        input_body = b64_body
        dcrpted_v1 = cipher.decrypt(input_body)
        cooked_v1 = "".join([chr(c + 1) for c in dcrpted_v1]).replace("\u0001", "")
        base64_v2 = base64.b64decode(cooked_v1[8:])
        z_in_raw = base64_v2[4:len(base64_v2)]
        z_out = zlib.decompress(z_in_raw).decode("utf16")
        plained = json.loads(z_out)
        return plained
 
with open("news.txt") as f:
    content_body = f.read()
    with open("newsmy_fi.txt", "w") as text_file:
        text_file.write(str(decrypt(content_body)))
