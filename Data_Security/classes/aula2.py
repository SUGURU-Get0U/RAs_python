'''

AULA SOBRE TEXTOS E ARQUIVOS BINÁRIOS, CODEC etc

'''

# Os codecs suportados pelo Python3 podem ser diferentes dependendo do sistema (MAC, Windows, Linux, etc.).
# Para saber quais codecs são suportados no seu sistema use o seguinte código:

import encodings.aliases # imports the dictionary with all the available CODECs!

aliases = encodings.aliases.aliases
unique_encodings = set(aliases.values())
sorted_encodings = sorted(unique_encodings)
for encoding in sorted_encodings:
    print(encoding)

# BASE64_CODEC is the one used on cypher and criptography

