from .. import *

class Crypto():

    @staticmethod
    def gen_password(length, type):
        text = ""
        if type=="a": text=ascii_lowercase
        elif type=="A": text=ascii_uppercase
        elif type=="0": text=digits
        elif type=="@": text=ascii_letters+digits
        else: text=ascii_letters+digits+punctuation

        pprint("".join(choices(text, k=length)))

    def gen_key():
        print(b64encode(AESGCM.generate_key(bit_length=256)))

    @staticmethod
    def decrypt(cipher_text_b64: str, key: bytes) -> str:
        data = b64decode(cipher_text_b64)
    
        iv = data[:16]              # AES block size = 16 bytes
        ciphertext = data[16:]
    
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv)
        )
    
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
        # PKCS7 unpadding
        unpadder = padding.PKCS7(128).unpadder()  # 128 bit = block size AES
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
        text = plaintext.decode("utf-8").lstrip("\ufeff")
        return text
    
    @staticmethod
    def encrypt(plain_text: str, key: bytes) -> str:
        iv = os.urandom(16)
    
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text.encode("utf-8")) + padder.finalize()
    
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv)
        )
    
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        result = iv + ciphertext
    
        return b64encode(result).decode("utf-8")
