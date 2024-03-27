from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import binascii

# DSA key generator
key = DSA.generate(1024)

# signer and verifier need to have the same g, p, q
tup = [key.y, key.g, key.p, key.q]

# Hash the message into hash object using SHA256 algo
message = b"Hello" 
hash_obj = SHA256.new(message)

# generate a digital signature based on the hash value of the message
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)

# print out the hash outcome
# print(hash_obj.hexdigest())

signature_hex = binascii.hexlify(signature)

# print out the signature
# print(signature_hex)

pub_key = DSA.construct(tup)

# signature can be verified using this method
hash_obj = SHA256.new(message)
verifier = DSS.new(pub_key, 'fips-186-3')
try:
	verifier.verify(hash_obj, signature)
	print("The message is authentic.")
except ValueError:
	print("The message is not authentic.")