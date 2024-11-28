import math

SBOX = [
    [3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 4, 2, 7, 0, 9, 12],
    [15, 12, 2, 7, 9, 0, 5, 10, 1, 11, 14, 8, 6, 13, 3, 4],
    [8, 6, 7, 9, 3, 12, 10, 15, 13, 1, 14, 4, 0, 11, 5, 2],
    [0, 15, 11, 8, 12, 9, 6, 3, 13, 1, 2, 4, 10, 7, 5, 14],
    [1, 15, 8, 3, 12, 0, 11, 6, 2, 5, 4, 10, 9, 14, 7, 13],
    [15, 5, 2, 11, 4, 10, 9, 12, 0, 3, 14, 8, 13, 6, 7, 1],
    [7, 2, 12, 5, 8, 4, 6, 11, 14, 9, 1, 15, 13, 3, 10, 0],
    [1, 13, 15, 0, 14, 8, 2, 11, 7, 4, 12, 10, 9, 3, 5, 6],
]

INVERSE_SBOX = [[row.index(i) for i in range(16)] for row in SBOX]

def rotate_left(value, shift, size=128):
    return ((value << shift) & (2**size - 1)) | (value >> (size - shift))

def rotate_right(value, shift, size=128):
    return ((value >> shift) | (value << (size - shift))) & (2**size - 1)

def generate_subkeys(key):
    w = [0] * 140
    for i in range(8):
        w[i] = (key >> (32 * (7 - i))) & 0xFFFFFFFF

    for i in range(8, 140):
        temp = w[i - 8] ^ w[i - 5] ^ w[i - 3] ^ w[i - 1] ^ 0x9E3779B9 ^ (i - 8)
        w[i] = rotate_left(temp, 11, size=32)

    subkeys = [0] * 33
    for i in range(33):
        subkeys[i] = sum((w[4 * i + j] << (32 * (3 - j))) for j in range(4))

    return subkeys

def substitute(block, sbox):
    result = 0
    for i in range(32):
        nibble = (block >> (4 * i)) & 0xF
        result |= sbox[nibble] << (4 * i)
    return result

def serpent_encrypt_block(key, block):
    subkeys = generate_subkeys(key)
    for round_num in range(32):
        block ^= subkeys[round_num]
        block = substitute(block, SBOX[round_num % 8])
        block = rotate_left(block, 3)

    block ^= subkeys[32]
    return block

def serpent_decrypt_block(key, block):
    subkeys = generate_subkeys(key)
    block ^= subkeys[32]
    for round_num in range(31, -1, -1):
        block = rotate_right(block, 3)
        block = substitute(block, INVERSE_SBOX[round_num % 8])
        block ^= subkeys[round_num]

    return block

def pad(data):
    """Ajoute un padding PKCS#7 pour atteindre une longueur multiple de 16 octets."""
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length] * padding_length)

def unpad(data):
    """Supprime le padding PKCS#7."""
    padding_length = data[-1]
    return data[:-padding_length]

def serpent_encrypt(key, plaintext):
    plaintext = pad(plaintext)
    ciphertext = b""
    for i in range(0, len(plaintext), 16):
        block = int.from_bytes(plaintext[i:i+16], byteorder="big")
        encrypted_block = serpent_encrypt_block(key, block)
        ciphertext += encrypted_block.to_bytes(16, byteorder="big")
    return ciphertext

def serpent_decrypt(key, ciphertext):
    plaintext = b""
    for i in range(0, len(ciphertext), 16):
        block = int.from_bytes(ciphertext[i:i+16], byteorder="big")
        decrypted_block = serpent_decrypt_block(key, block)
        plaintext += decrypted_block.to_bytes(16, byteorder="big")
    return unpad(plaintext)

# Programme principal
if __name__ == "__main__":
    key = 0x0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF

    # Entrée utilisateur
    plaintext_input = input("Entrez le texte clair : ").encode("utf-8")

    # Chiffrement
    ciphertext = serpent_encrypt(key, plaintext_input)
    print(f"Texte clair : {plaintext_input.decode('utf-8')}")
    print(f"Texte chiffré (hex) : {ciphertext.hex()}")

    # Déchiffrement
    decrypted_text = serpent_decrypt(key, ciphertext).decode("utf-8")
    print(f"Texte déchiffré : {decrypted_text}")
