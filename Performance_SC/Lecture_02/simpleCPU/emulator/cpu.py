class CPU:
    AcumulatorRegistry: int = 0 # A simple math counter, if we want to add 5 + 5, it saves 5 here than adds 5 later
    ProgramCounter: int = 0 # This is the Counter for the programs, Whenever a program is executed on the stack, it adds 1
    InstructionRegistry: int = 0 # this is where the CODE gets saved as binary to get interpreted by the PC
    memory = memory
    
    # Constructor, it should have:
    # A memory OBJECT, where it is stored
    # the rest of the variables
    def __init__(self,memory):
        self.memory = memory

    # THE CPU has 3 methods, FETCH, DECODE TO BINARY and EXECUTE the piece of code decoded
    def FetchInRam(self,memoryAdress):
     for GET_CODE in range(0,256):
        # should fetch the ram for tasks
        self.ram.Read(self.ProgramCounter)
        # after it reads, increment the PC
        self.ProgramCounter += 1
        return 


    def DecodeToBin(self,humanCode):
        pass

    def run():
        pass