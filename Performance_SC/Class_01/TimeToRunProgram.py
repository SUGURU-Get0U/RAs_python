import time

def printSigma():
    for i in range(5000000):
        print("sigma!", end="") # this makes sure we are printing each SIGMA side by side
        # successfuly printing 5 million characters instead of 10 millions (couting the line jumps)
    
    
# criar um relogio para cronometrar o tempo para resolucao de cada tarefa
clock = time.time()

# call a random function, in this case it will print 67, 5 million times
printSigma()

finalTime = time.time() - clock

# finally display the ammount of time required
print(f"the amount of time to complete the function {printSigma} is {finalTime}")


# output 1 <function printSigma at 0x000002417D5BFA00> is 5.805199384689331
# output 2 <function printSigma at 0x000002585F81FA00> is 5.565826654434204
# output 3 <function printSigma at 0x000001D4BBA5FA00> is 5.655542612075806
# output 4 <function printSigma at 0x0000021B56ABFA00> is 5.668705940246582
# output 5 <function printSigma at 0x000001D1C482FA00> is 6.272045135498047

# average time is 