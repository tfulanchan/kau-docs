Integrity

Hashes are used to verify and ensure data integrity. A hash function is a computational method that maps an indeterminate size of data into a fixed size of data. (David O. Manz et al., 2017) It provides a number quantity that represents the input data. (David O. Manz et al., 2017) A cryptographic hash function is a one-way function that takes as its input a message of any size and then returns a fixed-length string, named hash value. (Mehrdad Nojoumian et al., 2020) Once computed, it is computationally infeasible to invert the hash value and get the original message. (Mehrdad Nojoumian et al., 2020) Common hash functions are MD-5 and the SHA family such as SHA-1, SHA-2 and SHA-3. (David O. Manz et al., 2017) Hashing is used in blockchain for tamper-proof storage, block mining, and digital signature on transactions. (Choong Seon Hong et al., 2021) 

The purpose of computing hashes is to ensure data integrity, provide a unique identifier for data, and to securely store data. (Leighton Johnson, 2020) Hashing is also used in digital forensics to verify the authenticity of files and to detect any changes made to them. (Steven Bolt et al., 2013) Cryptographic hashing algorithms are used to scramble data and produce a fixed length product, called the hash value. (Derrick Rountree, 2011) Hashing relies on the fact that hashes are one-way, meaning that you can use the hash and the data to create the hash value, but you cannot figure out the data given the hash value. (Derrick Rountree, 2011) Hash functions should also avoid collisions, where two different sets of data produce the same hash value. (Derrick Rountree, 2011) Finally, hashing is used to create checksums or message digests to ensure data has not been altered. (Leighton Johnson, 2020) 

https://www.sciencedirect.com/science/article/pii/B9781597496537000050
Jason Andress wrote in The Basics of Information Security, 2011
"Hash functions represent a third cryptography type alongside symmetric and asymmetric cryptography, what we might call keyless cryptography. Hash functions, also referred to as message digests, do not use a key, but instead create a largely unique and fixed-length hash value, commonly referred to as a hash, based on the original message, something along the same lines as a fingerprint.

Hashes cannot be used to discover the contents of the original message, or any of its other characteristics, but can be used to determine whether the message has changed. In this way, hashes provide confidentiality, but not integrity. Hashes are very useful when distributing files or sending communications, as the hash can be sent with the message so that the receiver can verify its integrity. The receiver simply hashes the message again using the same algorithm, then compares the two hashes. If the hashes match, the message has not changed. If they do not match, the message has been altered.

Although it is theoretically possible to engineer a matching hash for two different sets of data, called a collision, this is a very difficult task indeed, and generally requires that the hashing algorithm be broken in order to accomplish. Some algorithms, such as Message-Digest algorithm 5 (MD5), have been attacked in this fashion, although producing a collision is still nontrivial. When such cases occur, the compromised algorithm usually falls out of common use. Hashing algorithms such as SHA-2 and the soon-to-arrive SHA-3 have replaced MD5 in cases where stringent hash security is required.

Many other hash algorithms exist and are used in a variety of situations, such as MD2, MD4, and RACE."

A sender transmits a document and separately a hash value, so that the receiver can check the authenticity by using the function and to be sure the file is unchanged (Figs. 4 & 5) (Fill and Meier, 2020; Fill and Meier, 2020).

[Fig. 4. Hashing information between two successive stakeholders.][Fig. 5. Validating Hash value.]

Origin Authentication
The combination of Hash function and Message Authentication Code can ensure origin authentication and integrity assurance. HMAC uses an additional secret key as input to the hash function.



HMAC Hashing Algorithm
An HMAC is calculated using any cryptographic algorithm that combines a cryptographic hash function with a secret key. Only the sender and the receiver know the secret key, and the output of the hash function depends on the input data and the secret key. Only parties who have access to that secret key can compute the digest of an HMAC function. If two parties share a secret key and use HMAC functions for authentication, a properly constructed HMAC digest of a message that a party has received indicates that the other party was the originator of the message. The steps of HMAC are as follows:
1. Creating the HMAC Value. The sending device inputs data into the hashing algorithm and calculates the fixed-length HMAC digest. This authenticated digest is then attached to the message and sent to the receiver.
2. Verifying the HMAC Value. The receiving device removes the digest from the message and uses the plaintext message with its secret key as input into the same hashing function.
If the digest that is calculated by the receiving device is equal to the digest that was sent, the message has not been altered. The origin of the message is authenticated because only the sender possesses a copy of the shared secret key. The HMAC function ensures the authenticity of the message.

Confidentiality

There are two classes of encryption used to provide data confidentiality; asymmetric and symmetric. These two classes differ in how they use keys.
Symmetric encryption algorithms such as Data Encryption Standard (DES), 3DES, and Advanced Encryption Standard (AES) are based on the premise that each communicating party knows the pre-shared key. Implementing asymmetric algorithms ensure data confidentiality, the most common algorithms are Rivest, Shamir, and Adleman (RSA) and the public key infrastructure (PKI).

Symmetric Encryption
Symmetric algorithms use the same pre-shared key (secret key) to encrypt and decrypt data. Symmetric encryption algorithms are commonly used with VPN traffic because they use less CPU resources than asymmetric encryption algorithms. When using these algorithms, the longer the key, the longer it will take for someone to discover the key. Most encryption keys are between 112 and 256 bits. The longer key is, the more secure the communications are. Symmetric encryption algorithms can be classified as a block cipher or a stream cipher. 

Block Ciphers
Block ciphers transform a fixed-length block of plaintext into a common block of ciphertext of 64 or 128 bits. Common block ciphers include DES with a 64-bit block size and AES with a 128-bit block size.

Stream Ciphers
Stream ciphers encrypt plaintext one byte or one bit at a time. Stream ciphers are basically a block cipher with a block size of one byte or bit. Stream ciphers are typically faster than block ciphers because data is continuously encrypted. Stream Ciphers is implmented in RC4 and A5, which are used to encrypt GSM cell phone communications.

Two other symmetric encryption algorithms are Data Encryption Standard (DES) and Advanced Encryption Standard (AES).

Asymmetric Encryption
Asymmetric algorithms are also known as public-key algorithms. They are designed in a way that the encryption and the decryption keys are different. Asymmetric algorithms use a public key and a private key. Both keys are capable of the encryption process, but the complementary paired key is required for decryption. The process is also reversible. Data that is encrypted with the public key requires the private key to decrypt. This ensure confidentiality and authenticity.

Asymmetric encryption can use key lengths between 512 to 4,096 bits. Asymmetric algorithms are substantially slower than symmetric algorithms. 

Asymmetric encryption ensures confidentiality, authenticity and integrity.

Asymmetric algorithms are used to provide confidentiality without pre-sharing a password. The confidentiality objective of asymmetric algorithms is initiated when the encryption process is started with the public key. When the public key is used to encrypt data, the private key must be used to decrypt data. Only one host has the private key; therefore, confidentiality is achieved.

The authentication objective of asymmetric algorithms is initiated with the private key encryption process. When the private key is used to encrypt the data, the corresponding public key must be used to decrypt the data.  Because only one host has the private key, only that host could have encrypted the message, providing authentication of the sender. When a host successfully decrypts a message using a public key, it is trusted that the private key encrypted the message, which verifies who the sender is. This is a form of authentication. Alice uses her private key

Alice encrypts a message using her private key and sends it to Bob. Bob decrypts using the public key. After Bob obtains Alice’s public key, he uses it to decrypt the message and to authenticate that the message has been received from Alice.

One of the most common asymmetric algorithms is Diffie-Hellman. This algorithm allows two parties to agree on a key that they can use to encrypt messages they want to send to each other. The security depends on the assumption that it is easy to raise a number to a certain power, but difficult to compute which power was used, given the number and the outcome.

Diffie-Hellman is an asymmetric mathematical algorithm that allows two computers to generate an identical shared secret without having communicated before. The new shared key is never actually exchanged between the sender and receiver. The key can be used by an encryption algorithm to encrypt traffic between the two systems as both parties know it.
Following are two examples of instances when DH is commonly used:
Data is exchanged using an IPsec VPN
SSH data is exchanged
The security of DH is based on the fact that it uses very large numbers in its calculations. 

Another common asymmetric algorithm is Digital Signature Standard (DSS) and Digital Signature Algorithm (DSA). It specifies DSA as the algorithm for digital signatures. DSA is a public key algorithm based on the ElGamal signature scheme. Signature creation speed is similar to RSA, but is 10 to 40 times slower for verification.

Digital signatures are commonly used to provide assurance of the authenticity and integrity of software code. Executable files are wrapped in a digitally signed envelope, which allows the end user to verify the signature before installing the software. Digitally signing code provides several assurances about the code: The code is authentic and is actually sourced by the publisher. The code has not been modified since it left the software publisher. The publisher undeniably published the code. This provides nonrepudiation of the act of publishing. The purpose of digitally signed software is to ensure that the software has not been tampered with, and that it originated from the trusted source as claimed. 
