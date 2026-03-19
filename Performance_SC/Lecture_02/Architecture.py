
# Adreesing BINARY numbers in Python!!
ordinaryInteger = 101 
print(f"A normal number: {ordinaryInteger}")

# To make a Binary number we use 0b
binaryNumber = 0b101
print(f"the number {bin(binaryNumber)} converted to Decimal: {binaryNumber}") # outputs a 5
# what if we want it to print it as a binary? cast it with bin()
print(f"The same number represented as BIN: {bin(binaryNumber)}") # outputs 101

print("--" * 30)

# To make a Octal number use 0o
octalNumber = 0o6767
# casts with oct() method
print(f"the number {oct(octalNumber)} converted to Decimal: {octalNumber}") # outputs 3575
print(f"the number {oct(octalNumber)} in binary {bin(octalNumber)}")

print("--" * 30)
# To make a Hexa number we use 0x
hexaNumber = 0xC67
# casts with oct() method
print(f"the number {hex(hexaNumber)} converted to Decimal: {hexaNumber}") # outputs 3175
print(f"the number {hex(hexaNumber)} in binary {bin(hexaNumber)}")