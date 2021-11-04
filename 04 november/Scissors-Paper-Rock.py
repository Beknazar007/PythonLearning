a = input("Player1: ")
b = input("Player2: ")
if a == "sc" and b == "pp" or a == "pp" and b == "rc" or  a =="rc" and b == "sc":
    print("Winner is Player1")
elif b == "sc" and a == "pp" or b == "pp" and a == "rc" or  b =="rc" and a == "sc":
    print("Winner is Player2")
else:
    print("Draw")    