from cryptography.hazmat.primitives import serialization
from Crypto.hashing import calculate_file_hash


def sign_document(file_path):
    # Load private key
    with open("keys/private_key.pem", "rb") as file:
        private_key = serialization.load_pem_private_key(
            file.read(),
            password=None
        )

    # Calculate SHA-256 hash of the PDF
    file_hash = calculate_file_hash(file_path)

    # Convert hash string into bytes
    hash_bytes = file_hash.encode()

    # Sign the hash
    signature = private_key.sign(hash_bytes)

    return signature

signature = sign_document("test.pdf")

print(signature)