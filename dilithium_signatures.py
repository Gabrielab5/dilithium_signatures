# Import necessary libraries
import numpy as np
import hashlib

# Function to generate private and public keys
def generate_keys():
    """
    Generates a pair of keys:
    - Private key: A vector of random integers.
    - Public key: Derived from the private key (simplified for this example).
    """
    private_key = np.random.randint(0, 100, size=(10,))  # Example private key as a random vector
    public_key = private_key * 2  # Public key derived by multiplying the private key
    return private_key, public_key

# Function to sign a message
def sign_message(private_key, message):
    """
    Sign a message using the private key.
    Args:
        private_key (list): The private key for signing.
        message (str): The message to be signed.
    Returns:
        list: The generated signature.
    Raises:
        ValueError: If the message is empty or private key is invalid.
    """
    if not message:
        raise ValueError("Message cannot be empty.")
    if not private_key.any():
        raise ValueError("Private key is invalid.")

    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    signature = [int(char, 16) * pk for char, pk in zip(hashed_message[:len(private_key)], private_key)]
    return signature

# Function to verify a signature
def verify_signature(public_key, message, signature):
    """
    Verifies a message signature using the public key.
    - Hashes the message.
    - Recreates the expected signature based on the public key.
    - Compares the recreated signature with the provided signature.   
    Args:
        public_key (list): The public key used for verification.
        message (str): The message to verify.
        signature (list): The signature to verify.        
    Raises:
        ValueError: If the message, public key, or signature is invalid.
    """
    if not message:
        raise ValueError("Message cannot be empty.")
    if not public_key.any() or not signature:
        raise ValueError("Public key or signature is invalid.")
    
    hashed_message = hashlib.sha256(message.encode()).hexdigest()  # Hash the message
    print("Hashed message for verification:", hashed_message)  # Debugging
    # Recreate the expected signature using the public key
    expected_signature = [int(char, 16) * (pk // 2)  for char, pk in zip(hashed_message[:len(public_key)], public_key)]
    print("Expected signature:", expected_signature)  # Debugging
    return signature == expected_signature

# Main function to demonstrate the process
def main():
    """
    Demonstrates the process of key generation, signing, and verifying:
    - Generates a key pair (private and public).
    - Signs a test message using the private key.
    - Verifies the signature using the public key.
    """
    # Test message to sign
    message = "Hello, this is a test message!"
    
    # Generate keys
    private_key, public_key = generate_keys()
    print("Private Key:", private_key)
    print("Public Key:", public_key)
    
    # Sign the message
    signature = sign_message(private_key, message)
    print("Signature:", signature)
    
    # Verify the signature
    is_valid = verify_signature(public_key, message, signature)
    print("Is the signature valid?", is_valid)

# Entry point for the program
if __name__ == "__main__":
    main()
