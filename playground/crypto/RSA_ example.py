from Crypto.PublicKey import RSA


key = RSA.generate(2048)

print(key.publickey())

encrypted_key = key.export_key()
print(encrypted_key)

