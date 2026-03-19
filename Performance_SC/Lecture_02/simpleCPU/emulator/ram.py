class Memory:
    buffer: int = [256]
    # tam: int = 0

    # The constructor for this class
    def __init__(self, size):
        self.buffer = [0] * size
       #self.tam = 2**nbits, the size of the Memory should be 2 to the power of the number of bits

    def Write(self, memoryAddress, values):

        values = values & 0xFF # Does a BITMASK operation to keep the values always in 8 bit!
        if memoryAddress >= 0 and memoryAddress < 256: # validates the memory address, if its greater than 255 it doesnt add
            # NEEDS TO CONTAIN 0, 0 is where important instructions such as boot are saved
            memoryAddress = memoryAddress
            # maybe add a validation to see if the Address is available otherwise it will overwrite stuff
            self.buffer[memoryAddress] = values # saves the values on the specified address
            return
    
    def Read(self,memoryAddress):
        if memoryAddress < len(self.buffer): # again, if the inputed address is greater than the buffer size, it doesnt read
            info = self.buffer[memoryAddress] # saves the info for display
            print(f"Info in {memoryAddress}: {info}") # displays the info
            return
            