import unittest
from dilithium_signatures import generate_keys, sign_message, verify_signature

class TestDilithium(unittest.TestCase):
    def test_key_generation(self):
        private_key, public_key = generate_keys()
        self.assertEqual(len(private_key), 10)
        self.assertEqual(len(public_key), 10)

    def test_signature_verification(self):
        private_key, public_key = generate_keys()
        message = "Test message"
        signature = sign_message(private_key, message)
        self.assertTrue(verify_signature(public_key, message, signature))

    def test_invalid_signature(self):
        private_key, public_key = generate_keys()
        message = "Test message"
        signature = sign_message(private_key, message)
        self.assertFalse(verify_signature(public_key, "Tampered message", signature))

if __name__ == "__main__":
    unittest.main()
