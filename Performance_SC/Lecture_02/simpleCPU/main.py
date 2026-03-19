from emulator.ram import Memory # imports the memory class from the ram file!  




if __name__ == "__main__":
    # 1. Hardware Setup (Testing the Constructor)
    my_RAM = Memory(256)
    print("RAM initialized with 256 slots.")

    # 2. The Write Test
    print("Testing Write...")
    my_RAM.Write(10, 3000) # Testing the 8-bit mask!
    print("Write Successful")

    # 3. The Read Test
    print("Testing Read...")
    my_RAM.Read(10)