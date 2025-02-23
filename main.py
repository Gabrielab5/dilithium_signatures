import time
import os
import oqs
from dilithium_signatures import generate_keys, sign_message, verify_signature, save_keys, load_keys

def measure_performance(dilithium_level="Dilithium3"):
    """
    Measure and display performance of key generation, signing, and verification.
    """
    message = "Performance test message"
    
    print("\n" + "="*50)
    print(f"Running Performance Test for {dilithium_level}")
    print("="*50)
    
    # Measure key generation time
    start_time = time.time()
    private_key, public_key = generate_keys(dilithium_level)
    key_gen_time = time.time() - start_time
    print(f"[{dilithium_level}] Key Generation Time: {key_gen_time:.6f} seconds")
    save_keys(private_key, public_key)

    # Measure signing time
    start_time = time.time()
    signature = sign_message(private_key, message)
    signing_time = time.time() - start_time
    print(f"[{dilithium_level}] Signing Time: {signing_time:.6f} seconds")

    # Measure verification time
    start_time = time.time()
    is_valid = verify_signature(public_key, message, signature)
    verification_time = time.time() - start_time
    print(f"[{dilithium_level}] Verification Time: {verification_time:.6f} seconds")
    
    print("✅ Signature Validity:", "✔ Valid" if is_valid else "❌ Invalid")
    print("="*50, "\n")

if __name__ == "__main__":
    for level in ["Dilithium2", "Dilithium3", "Dilithium5"]:
        measure_performance(level)
