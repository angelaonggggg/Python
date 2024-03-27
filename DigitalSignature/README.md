# Digital Signature using DSA

This Python project generates a digital signature using the Digital Signature Algorithm (DSA) and verifies the signature.

Signer and verifier need to have the same DSA parameters, which are `g`, `p`, `q`, and the public key `y`, to successfully verify the message.

**Installation:**

To run the code locally:

1. Download code.
2. Install the required dependencies by running:
    ```
    pip install pycryptodome
    ```
4. To run the script, navigate to the folder containing the code (digitalSignature.py) on the terminal.
5. Execute the following command:
    ```
    python digitalSignature.py
    ```

**The script will perform the following steps:**

- Generate DSA parameters (g, p, q, and public key y).
- Hash a message using the SHA256 algorithm.
- Sign the hashed message using the private key to generate a digital signature.
- Verify the signature using the public key.

**Output:**

The script will output whether the message is authentic or not.
