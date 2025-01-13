import time
from dilithium_signatures import generate_keys, sign_message, verify_signature

def measure_performance():
    """
    Measure and display performance of key generation, signing, and verification.
    """
    message = "Performance test message"
    
    # Measure key generation time
    start_time = time.time()
    private_key, public_key = generate_keys()
    key_gen_time = time.time() - start_time
    print(f"Key Generation Time: {key_gen_time:.6f} seconds")
    
    # Measure signing time
    start_time = time.time()
    signature = sign_message(private_key, message)
    signing_time = time.time() - start_time
    print(f"Signing Time: {signing_time:.6f} seconds")
    
    # Measure verification time
    start_time = time.time()
    is_valid = verify_signature(public_key, message, signature)
    verification_time = time.time() - start_time
    print(f"Verification Time: {verification_time:.6f} seconds")
    print("Is the signature valid?", is_valid)

if __name__ == "__main__":
    measure_performance()
