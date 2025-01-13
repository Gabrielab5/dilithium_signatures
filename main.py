from dilithium_signatures import generate_keys, sign_message, verify_signature

def main():
    message = "Hello, Dilithium!"
    private_key, public_key = generate_keys()
    
    print("Private Key:", private_key)
    print("Public Key:", public_key)
    
    signature = sign_message(private_key, message)
    print("Signature:", signature)
    
    is_valid = verify_signature(public_key, message, signature)
    print("Is signature valid?", is_valid)

if __name__ == "__main__":
    main()
