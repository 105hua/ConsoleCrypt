from cryptography.hazmat.primitives import padding

class PKCS7:
    def __init__(self, block_size: int):
        if 1 <= block_size <= 256:
            self.block_size = block_size
            self.padding = padding.PKCS7(block_size)
        else:
            raise ValueError("Invalid block size. PKCS7 requires a block size between 1 and 256.")
    def pad(self, data: bytes) -> bytes:
        padder = self.padding.padder()
        return padder.update(data) + padder.finalize()
    def unpad(self, data: bytes) -> bytes:
        unpadder = self.padding.unpadder()
        return unpadder.update(data) + unpadder.finalize()