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
        self.padding = PKCS7(key_size)

    def encrypt(self, data: bytes) -> bytes:
        encryptor = self.algorithm.encryptor()
        padder = self.padding.create_padder()
        padded_data = padder.update(data) + padder.finalize()
        return encryptor.update(padded_data) + encryptor.finalize()

    def decrypt(self, data: bytes) -> bytes:
        decryptor = self.algorithm.decryptor()
        data = decryptor.update(data) + decryptor.finalize()
        unpadder = self.padding.create_unpadder()
        unpadded_data = unpadder.update(data) + unpadder.finalize()
        return unpadded_data