# Encryption
Encryption converts a plaintext value into a new encrypted value using a code or cipher. An encrypted value can be decrypted using the same code or cipher along with an encryption key.

## Uses
- **Confidentiality:** Keeping information and communications private and protecting them from unauthorized access
- **Integrity:** Keeping organizational information accurate, free of errors, and w/o unauthorized modifications
- **authenticity:** Used as a digital signature that identifies and authenticates an individual who created or modified a file.


## Types of Encryption
### Symmetric Encryption
Encryption and decryption are both performed by the same key.
- Single key encryption
- Used for Confidentiality
- Fast and well suited to bulk encrypting large amounts of data.
	- Examples:
		-   **AES** (Advanced Encryption Standard) - Strongest / Block cipher 128, 192, 256-bit
		-   **DES** (Data Encryption Standard) - Weak / Block cipher 56-bit
		-   **Blowfish** - Weak / Block cipher 64-bit
		-   **RC** (Rivest Cipher) - RC4 Stream cipher, RC5/RC6 Block cipher
### Asymmetric Encryption
Encryption and decryption are performed by two different but related public and private keys in a pair.
- Public key encrypts data, while the private key decrypts the data.
- Each key can reverse the cryptographic operation performed by its pair but cannot reverse a procedure performed by itself.
- Asymmetric encryption is mainly used for authentication. 
- Uses more computing power making it less efficient for extensive data encryption.
- Examples:
	-   **[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))** (RIvest, Shamir, Adleman)
		- CTF tools for RSA:
			- [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
			- [rsatool](https://github.com/ius/rsatool)
	-   **Diffie-Hellman**
	-   **DSA** (Digital Signature Algorithm) - Endorsed by NIST for their digital signature standard
	-   **ElGamal** - Used in GNU privacy guard, Pretty Good Privacy (PGP)
