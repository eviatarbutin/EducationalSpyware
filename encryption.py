from Crypto.Cipher import AES
from Crypto import Random

KEY = b"somebytescoosomo"

def encrypt(packets:bytes) -> bytes: 
    """
    The function ecnrypts the bytes it recieves with the AES protocol and returns the encrypted bytes.


    Parameters
    -------------
    packets : bytes
        The packets/packet the sniffers sniffed.
    

    Returns
    -------------
    bytes
        The encrypted bytes.

    """
         
    message = packets + b"\0" * (AES.block_size - len(packets) % AES.block_size)
    iv = Random.new().read(AES.block_size)
    
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    enc = iv + cipher.encrypt(message)
    
    return enc

def decrypt(encrypted:bytes) -> bytes:
    """
    The function decnrypts the bytes it recieves with the AES protocol and returns the dencrypted bytes.

    
    Parameters
    -------------
    encrypted : bytes
        The bytes that were encrypted with the AES protocol.
    

    Returns
    -------------
    bytes
        The dencrypted bytes.

    """
    iv = encrypted[:AES.block_size]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    
    plaintext = cipher.decrypt(encrypted[AES.block_size:])
    
    return plaintext.rstrip(b"\0")

if __name__ == '__main__':
    moshe = b"abcdefghigjklmno"
    print(len(moshe))
    enc = encrypt(moshe)
    print(moshe.decode())
    print(enc)
    dec = decrypt(enc)
    print(dec.decode())