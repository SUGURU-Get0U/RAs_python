import time

# the double starts '**' represent 'to the power of'
#
#
#
# Notice how we are multiplying number by -1 10 million times, we can just switch the signal of 1

def Approximating_Pi(limit):
    number = 0
    result = 0 
    num1 = 1.0
    for _ in range(limit):
       result +=  num1 / (2 * number + 1)
       num1 = -num1
       number += 1
    pi = 4 * result
    return pi


Start_time = time.time()

pi = Approximating_Pi(100 000 000 000)

finalTime = time.time() - Start_time

print(f" PI is equal to {pi}")
print(f"{finalTime} was the time to run the function")


