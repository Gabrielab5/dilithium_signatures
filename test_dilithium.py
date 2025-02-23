import unittest
from dilithium_signatures import generate_keys, sign_message, verify_signature

class TestDilithium(unittest.TestCase):

    def test_key_generation(self):
        """Test if key generation produces valid key pairs."""
        for level in ["Dilithium2", "Dilithium3", "Dilithium5"]:
            with self.subTest(variant=level):
                private_key, public_key = generate_keys(level)
                self.assertIsInstance(private_key, bytes, f"Private key for {level} is not bytes")
                self.assertIsInstance(public_key, bytes, f"Public key for {level} is not bytes")

    def test_valid_signature(self):
        """Test if a message signed with the private key verifies correctly with the public key."""
        private_key, public_key = generate_keys()
        message = "Test message"
        signature = sign_message(private_key, message)
        self.assertTrue(verify_signature(public_key, message, signature), "Valid signature verification failed!")

    def test_tampered_message(self):
        """Ensure tampered messages do not pass verification."""
        private_key, public_key = generate_keys()
        message = "Test message"
        signature = sign_message(private_key, message)
        tampered_message = "Tampered message"
        self.assertFalse(verify_signature(public_key, tampered_message, signature), "Tampered message should not verify!")

    def test_invalid_signature(self):
        """Ensure an altered signature does not pass verification."""
        private_key, public_key = generate_keys()
        message = "Test message"
        signature = sign_message(private_key, message)
        invalid_signature = signature[:-1] + b"X"  # Modify the signature slightly
        self.assertFalse(verify_signature(public_key, message, invalid_signature), "Invalid signature should not verify!")

    def test_empty_message(self):
        """Ensure an empty message can still be signed and verified."""
        private_key, public_key = generate_keys()
        message = ""
        signature = sign_message(private_key, message)
        self.assertTrue(verify_signature(public_key, message, signature), "Empty message should verify correctly.")

    def test_missing_keys(self):
        """Ensure missing keys return appropriate errors."""
        with self.assertRaises(ValueError):
            sign_message(None, "Test message")
        with self.assertRaises(ValueError):
            verify_signature(None, "Test message", b"fake_signature")

    def test_official_test_vectors(self):
        """If available, validate against official test vectors."""
        test_vectors = [
            ("message1", b"testkey1", b"testsignature1"),
            ("message2", b"testkey2", b"testsignature2"),
        ]
        for msg, key, sig in test_vectors:
            with self.subTest(msg=msg):
                self.assertTrue(verify_signature(key, msg, sig), "Official test vector verification failed!")

if __name__ == "__main__":
    unittest.main()
