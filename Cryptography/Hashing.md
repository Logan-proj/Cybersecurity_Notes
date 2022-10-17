# Hashing
### Definition
- Takes input data of any size and creates a fixed-size text string (digest) of the data. Hashing data produces no keys and is irreversible.
### Uses
- **Verify data integrity:** Use hashing to check if a file has been tampered with or corrupted by comparing a saved hash value to a more current one. Because any data alteration will result in a different hash output, comparing the two hashes can indicate any data changes to a file. 
	- The data has been altered if the file hash is different. 
	- The data is not altered if the file hash is the same.
- **Verify passwords:** allows companies to store the hashed version of user passwords to help protect against a database leak. However, hashed passwords are vulnerable to a rainbow table attack.

#### Example Hashes
Checkout [Hashcat](https://hashcat.net/wiki/doku.php?id=example_hashes) for hash formats and password prefixes

#### Identifing Hashes
- Online [Hashes](https://hashes.com/en/tools/hash_identifier) hash identifier
- [Hash-Identifier](https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master) Python tool
	- Install: ``wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py``
	- Run: `python3 hash-id.py` in python, `hash-identifier` in Kali

#### Vulnerabilities & Attacks
* **Hash collision:** a scenario where two different plaintext inputs produce the same hashed output. Hash functions are designed to create unique hashes for every plaintext string; for example, "STRING(A)" always hashes to "HASH(A)," and "STRING(B) = "HASH(B)." However, a hash collision occurs when "STRING(A)" and "STRING(B)" are both equal to HASH(A) and cause a severe security vulnerability. Attackers can use hash collisions to imitate, access, or change data. MD5 and SHA1 are examples of hash functions that have been attacked and made technically insecure due to engineering hash collisions
* **Rainbow Table Attack:** An attack where a hash file is compared against a large table or wordlist of different hashes and their corresponding plaintext value. 
	* Because a hash function always returns the same output, in the scenario of a database leak that includes password hashes, attackers can search for hashes and find the corresponding plaintext password. 
	* _**Salting**_ methods can protect against these rainbow table attacks.
	* Tools for rainbow table attacks:
		* [Hashes.com](https://hashes.com/en/decrypt/hash
		* [Crackstation](https://crackstation.net/)


# Definitions
* **Plaintext** - Data before encrypting or hashing

- **Salting:** The process of adding random values to the hashed data stored in a database. Adding salt to hashes helps protect against _**rainbow table**_ attacks by creating unique hashes different from their common hash value. 
	-   More challenging to look up the corresponding plaintext value for a standard hash output.
	-   It prevents duplicate hashes for those who use the same password.