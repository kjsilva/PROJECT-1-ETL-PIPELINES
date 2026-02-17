from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import base64

class dBCred:
    def __init__(self):
        pass

    #password encryptor
    def encryptor(self, data):
        #generate and save fernet key
        key = Fernet.generate_key()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data.encode())

        return encrypted, key
    
    #password decryptor
    def decryptor(self, data, key):
        #convert the data into bytes
        data = data.encode()
        #key is the fernet key generated upon data encryption
        fernet = Fernet(key)

        decrypted = fernet.decrypt(data.decode())
        return decrypted
    
    # -------------------------
    # AES Encrypt Function
    # -------------------------
    def aes_encrypt(self, plaintext):
        key = get_random_bytes(32)  # AES-256 key
        plaintext_bytes = plaintext.encode()

        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext_bytes)

        return {
            "key": base64.b64encode(key).decode(),
            "nonce": base64.b64encode(cipher.nonce).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode(),
            "tag": base64.b64encode(tag).decode()
        }
    
    def key_decryptor(self, env_dict):
        key = base64.b64decode(env_dict["key"])
        nonce = base64.b64decode(env_dict["nonce"])
        ciphertext = base64.b64decode(env_dict["ciphertext"])
        tag = base64.b64decode(env_dict["tag"])

        cipher = AES.new(key, AES.MODE_EAX, nonce)
        decrypted_bytes = cipher.decrypt_and_verify(ciphertext, tag)

        return decrypted_bytes.decode()
    