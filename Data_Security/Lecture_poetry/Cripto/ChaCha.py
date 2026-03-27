from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64encode
import os # important to make NONCE a unique number, to generate nonce we actually dont use python, instead we as the OS to do it

def cipherChaCha20(msg, key):
    # ChaCha20 requer um Nonce de 16 bytes (128 bits)
    nonce = os.urandom(16)
    
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None) # ChaCha20 não usa modos como CBC/ECB
    
    # Cifragem
    encryptor = cipher.encryptor() # generates a encripted msg
    ciphertext = encryptor.update(msg) # updates it
    
    print(f"Nonce (HEX): {nonce.hex()}") # is a random number, NONCE -> NUMBER USED ONLY ONCE or Number Once! 
    # nonce is used to help the cypher to criptograte the KEY,
    print("Ciphertext (B64):", b64encode(ciphertext).decode())
    print("Ciphertext (BYTES):", [c for c in ciphertext])

    # Decifragem (Exige o mesmo Nonce e Chave)
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext)
    print("Plaintext (Decoded):", plaintext.decode())

def testaChaCha20():
    # ChaCha20 utiliza chaves de 256 bits (32 bytes)
    print("--- Teste ChaCha20 (Stream Cipher) ---")
    segredo = input('Digite a senha (será preenchida/truncada para 32 bytes): ')
    
    # Ajuste da chave para 32 bytes (256 bits)
    key = segredo.encode().ljust(32, b'\0')[:32] # puts 0 in the end to make the password always have 32 bits
    print(f'CHAVE (HEX): {key.hex()}') # then converts it to Hexadecimal

    while True:
        msg = input('\nDigite a mensagem: ')
        if not msg:
            print('Saindo...')
            break
        
        try:
            cipherChaCha20(msg.encode(), key)
        except Exception as e:
            print(f"Erro: {e}")
            break
