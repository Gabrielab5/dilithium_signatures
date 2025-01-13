# Digital Signatures with Dilithium

## Overview
This project explores and implements a simplified version of the Dilithium-based digital signature algorithm, focusing on key generation, signing, and verification. The implementation is designed for educational purposes, showcasing the core principles of post-quantum cryptographic methods in Python.

With a clean and modular structure, this project offers an accessible way to understand digital signatures, even for those new to the field of cryptography. It provides a strong foundation for further exploration of advanced cryptographic concepts.

## Features
- **Key Generation**: Generate a private and public key pair.
- **Message Signing**: Sign messages using the private key.
- **Signature Verification**: Verify signed messages using the public key.
- Performance measurement
- Unit tests for robustness

## Requirements
- Python 3.8 or higher
- Libraries:
  - `numpy`

## Installation
1. Clone this repository:
   
    git clone https://github.com/your-repo/dilithium-signatures.git
   cd dilithium-signatures
   
2.Create a virtual environment:
python -m venv venv
.\venv\Scripts\activate  # For Windows
source venv/bin/activate  # For macOS/Linux

3.install dependencies:
pip install -r requirements.txt

-Verify the installation of PyCryptodome (used for ECC-based signatures):
pip show pycryptodome

4.Run the demonstration:
python main.py

5.Run tests:
python -m unittest test_dilithium.py



## Usage
1.Run the dilithium_signatures.py file:
python dilithium_signatures.py
2.The program will:
-Generate a key pair.
-Sign a test message.
-Verify the signature and display whether it's valid.

## File Structure
dilithium_signatures.py: Main script for the implementation.
README.md: Documentation for the project.

Future Enhancements
-Add real cryptographic components of the Dilithium algorithm.
-Support additional hash functions.
-Provide a web-based interface for demonstration.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This project is inspired by the NIST post-quantum cryptography standardization and aims to provide a hands-on introduction to modern cryptographic methods.

