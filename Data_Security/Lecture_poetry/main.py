from Cripto.ChaCha import *
from Cripto.AES import *

if __name__ == "__main__":
    op = input("Escolha o teste: [1] ChaCha20 (Stream) [2] AES (Block): ")
    if op == '1':
        testaChaCha20()
    else:
        testaAES()  