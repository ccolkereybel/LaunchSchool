def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
    
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

print(rps(rps(rps('paper'), rps("rock", "scissors")), 'rock'))

print(rps(rps('paper', "rock"), 'rock'))

print(rps('paper', 'rock'))

#paper