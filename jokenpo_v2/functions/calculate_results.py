import time
# Does the logical part of the RPS game
# Analyses both inputs and returns who won the match

def game_logic(p1,p2,p1_op,p2_op):
    match p1_op: # similar to switch but with different name
        case "rock":
            match p2_op:
                case "rock":
                    print("DRAW")
                case "scissors":
                    print(f"{p1} WON!")
                    print("Restarting game...")
                    time.sleep(0.5)
                    return 1 # Returns 1 for p1 win
                case "paper":
                    print(f"{p2} WON!")
                    print("Restarting game...")
                    time.sleep(0.5)
                    return 0 # Returns 0 for p0 win
                
        case "paper":
            match p2_op:
                case "rock":
                    print(f"{p1} WON!")
                    print("Restarting game...")
                    time.sleep(0.5)
                    return 1 # Returns 1 for p1 win 
                case "scissors":
                    print(f"{p2} WON!")
                    print("Restarting game...")
                    time.sleep(0.5)
                    return 0 # Returns 0 for p0 win  
                case "paper":
                    print("DRAW")
                        
        case "scissors":
            match p2_op:
                case "rock":
                    print(f"{p2} WON!")
                    print("Restarting game...")
                    time.sleep(0.5)
                    return 0 # Returns 0 for p0 win   
                case "scissors":
                    print("DRAW")    
                case "paper":
                    print(f"{p1} WON!")
                    print("Restarting game...")
                    time.sleep(0.5)
                    return 1 # Returns 1 for p1 win
                    