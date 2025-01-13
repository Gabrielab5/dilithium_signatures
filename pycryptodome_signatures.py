from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Function to generate ECC keys
def generate_ecc_keys():
    private_key = ECC.generate(curve='P-256')
    public_key = private_key.public_key()
    return private_key, public_key

# Function to sign a message
def sign_message_with_ecc(private_key, message):
    h = SHA256.new(message.encode())
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(h)
    return signature

# Function to verify a message signature
def verify_ecc_signature(public_key, message, signature):
    h = SHA256.new(message.encode())
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(h, signature)
        return True
    except ValueError:
        return False
