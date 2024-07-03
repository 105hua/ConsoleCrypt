from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from libs.padding import PKCS7

class AES:
    valid_block_sizes = [128, 256]
    
    def __init__(self, key: bytes = None, iv: bytes = None):
        key_size = len(key) * 8
        if key_size not in self.valid_block_sizes:
            raise ValueError(f"Invalid key size. Must be one of {self.valid_block_sizes}, not {key_size}.")
        if iv is None:
            raise ValueError("IV must be provided.")
        self.key = key
        self.algorithm = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        self.padder = PKCS7(key_size)

    def encrypt(self, data: bytes) -> bytes:
        encryptor = self.algorithm.encryptor()
        padded_data = self.padder.pad(data)
        return encryptor.update(padded_data) + encryptor.finalize()

    def decrypt(self, data: bytes) -> bytes:
        decryptor = self.algorithm.decryptor()
        unpadded_data = self.padder.unpad(data)
        return decryptor.update(unpadded_data) + decryptor.finalize()