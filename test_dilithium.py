import unittest
from dilithium_signatures import generate_keys, sign_message, verify_signature

class TestDilithium(unittest.TestCase):
    def test_key_generation(self):
        private_key, public_key = generate_keys()
        self.assertEqual(len(private_key), 10)
        self.assertEqual(len(public_key), 10)

    def test_valid_signature(self):
        private_key, public_key = generate_keys()
        message = "Test message"
        signature = sign_message(private_key, message)
        self.assertTrue(verify_signature(public_key, message, signature))

    def test_tampered_message(self):
        private_key, public_key = generate_keys()
        message = "Test message"
        signature = sign_message(private_key, message)
        tampered_message = "Tampered message"
        self.assertFalse(verify_signature(public_key, tampered_message, signature))

    def test_invalid_signature(self):
        private_key, public_key = generate_keys()
        message = "Test message"
        signature = sign_message(private_key, message)
        invalid_signature = [s + 1 for s in signature]  # Modify the signature slightly
        self.assertFalse(verify_signature(public_key, "Tampered message", signature))

    def test_empty_message(self):
        private_key, public_key = generate_keys()
        message = ""
        signature = sign_message(private_key, message)
        self.assertTrue(verify_signature(public_key, message, signature))

if __name__ == "__main__":
    unittest.main()
