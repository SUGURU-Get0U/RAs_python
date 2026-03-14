import random


def cripto(msg, keyy):
    cripto = ''
    for c in msg:
        code = ord(c) + keyy  # UNICODEs to bytes
        cripto += chr(code) # shifts back to a Character 
    return cripto

sample = "Inserir Texto rs"
checksum = hash(sample)
print(f"Autentication code {checksum}")


key = random.randint(1,10)
print(f'Chave sorteada {key}')
cypher = cripto(sample, key)
print(f"Texto cifrado {cypher}")


# EXERCISES
# DECODE THE MESSAGE Sfif%ij%st{t%st%kwtsy

exec_key = 'Sfif%ij%st{t%st%kwtsy'

def brute_force(cypherS, space_keys, check):
    for key in space_keys:
        try:
            sample = cripto(cypherS, -key)
            print(f"{key} : {sample}")
            if check == hash(sample):
                print("Chave encontrada!")
                print(f"A chave correta é {key}")
                return
        except:
            print(f"a chave é menor que {key}")
            return


# if __name__ == "Julius_Caeser.py":
max_key = 10000
answer = brute_force(exec_key, range(1,max_key), checksum)
print(answer)

# short keys often means short decoded answers
# higher numbered keys tend to break the code due to the math equations to resolute a sentence


