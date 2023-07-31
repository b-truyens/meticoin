import bitcoin

# Generate a random private key
private_key = bitcoin.random_key()

print("Private Key: %s\n" % private_key)

# Generate the WIF format from the private key
wif_private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(private_key, 'hex'), 'wif')
print("Private Key (WIF): %s\n" % wif_private_key)

# Generate a public key from the private key
public_key = bitcoin.privtopub(private_key)
print("Public Key: %s\n" % public_key)

# Generate a compressed public key from the private key
compressed_public_key = bitcoin.compress(bitcoin.privtopub(private_key))
print("Compressed Public Key: %s\n" % compressed_public_key)
