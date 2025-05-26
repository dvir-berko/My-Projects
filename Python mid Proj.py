
#Create a dictionary that maps each original letter to a random letter

def make_enc_key():
    import random
    import string

    letters = list(string.ascii_letters)
    shuffled = letters.copy()
    random.shuffle(shuffled)

    enc_key = dict(zip(letters, shuffled))
    return enc_key

key = make_enc_key()
#print(key)

#create the decryption key from the encryption key

def compute_dec_key(enc_key):
    dec_key = {v: k for k, v in enc_key.items()}
    return dec_key

enc_key = make_enc_key()
dec_key = compute_dec_key(enc_key)

#print("Encryption key:", enc_key)
#print("Decryption key:", dec_key)


#encrypting function

def encrypt_text(text, enc_key):
    encrypted = ""
    for char in text:
        if char in enc_key:
            encrypted += enc_key[char]
        else:
            encrypted += char  # if it's not in the key, keep it (like spaces or punctuation)
    return encrypted

    key = make_enc_key()
text = "hello world"
encrypted = encrypt_text(text, key)

#print("Original:", text)
#print("Encrypted:", encrypted)

#This function is the reverse of encrypt_text
def decrypt_text(encrypted_text, dec_key):
    decrypted = ""
    for char in encrypted_text:
        if char in dec_key:
            decrypted += dec_key[char]
        else:
            decrypted += char
    return decrypted


enc_key = make_enc_key()
dec_key = compute_dec_key(enc_key)

original = "hello world"
encrypted = encrypt_text(original, enc_key)
decrypted = decrypt_text(encrypted, dec_key)

print("Original: ", original)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

