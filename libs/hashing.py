from cryptography.hazmat.primitives import hashes

class SHA3:
    valid_key_sizes = [224, 256, 384, 512]
    def __init__(self, key_size: int = 256):
        if key_size not in self.valid_key_sizes:
            raise ValueError(f"Invalid key size. Must be one of {self.valid_key_sizes}.")
        self.key_size = key_size
        match self.key_size:
            case 224:
                self.hasher = hashes.Hash(hashes.SHA3_224())
            case 256:
                self.hasher = hashes.Hash(hashes.SHA3_256())
            case 384:
                self.hasher = hashes.Hash(hashes.SHA3_384())
            case 512:
                self.hasher = hashes.Hash(hashes.SHA3_512())
    def hash_string(self, string: str) -> bytes:
        self.hasher.update(string.encode("utf-8"))
        return self.hasher.finalize()