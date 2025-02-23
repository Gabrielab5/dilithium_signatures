import os
import oqs
import hashlib

def generate_keys(dilithium_level="Dilithium3"):
    """Generates a key pair using the specified Dilithium variant."""
    try:
        with oqs.Signature(dilithium_level) as dilithium:
            public_key = dilithium.generate_keypair()
            private_key = dilithium.export_secret_key()
            return private_key, public_key
    except Exception as e:
        print(f"Error generating keys: {e}")
        return None, None

def save_keys(private_key, public_key, folder="keys/"):
    """Saves private and public keys to files."""
    try:
        os.makedirs(folder, exist_ok=True)
        with open(folder + "private.key", "wb") as f:
            f.write(private_key)
        with open(folder + "public.key", "wb") as f:
            f.write(public_key)
        print("Keys saved successfully.")
    except Exception as e:
        print(f"Error saving keys: {e}")

def load_keys(folder="keys/"):
    """Loads previously saved keys from files."""
    try:
        with open(folder + "private.key", "rb") as f:
            private_key = f.read()
        with open(folder + "public.key", "rb") as f:
            public_key = f.read()
        print("Keys loaded successfully.")
        return private_key, public_key
    except FileNotFoundError:
        print("Key files not found. Generating new keys...")
        return generate_keys()
    except Exception as e:
        print(f"Error loading keys: {e}")
        return None, None

def sign_message(private_key, message):
    """Signs a message using the Dilithium private key."""
    if not private_key:
        raise ValueError("Invalid private key.")
    if not message:
        raise ValueError("Message cannot be empty.")
    try:
        with oqs.Signature("Dilithium3") as dilithium:
            dilithium.import_secret_key(private_key)
            return dilithium.sign(message.encode())
    except Exception as e:
        print(f"Error signing message: {e}")
        return None

def verify_signature(public_key, message, signature):
    """Verifies a signature using the Dilithium public key."""
    if not public_key or not signature:
        raise ValueError("Public key or signature is invalid.")
    try:
        with oqs.Signature("Dilithium3") as dilithium:
            dilithium.import_public_key(public_key)
            return dilithium.verify(message.encode(), signature)
    except Exception as e:
        print(f"Error verifying signature: {e}")
        return False

def command_line_verifier():
    """Command-line tool for verifying Dilithium signatures."""
    import sys
    if len(sys.argv) < 4:
        print("Usage: python verify.py <public_key_file> <message> <signature_file>")
        sys.exit(1)
    try:
        with open(sys.argv[1], "rb") as f:
            public_key = f.read()
        message = sys.argv[2]
        with open(sys.argv[3], "rb") as f:
            signature = f.read()
        is_valid = verify_signature(public_key, message, signature)
        if is_valid:
            print("Signature is valid.")
        else:
            print("Signature verification failed.")
    except Exception as e:
        print(f"Error in verification: {e}")

if __name__ == "__main__":
    command_line_verifier()
