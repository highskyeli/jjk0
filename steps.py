def stepcounter():
    global steps
    steps = 0
    steps =+ 1
    if steps >= 10:
        print("The skinwalker has found you. You are dead. There is nothing you can do. Just let it happen.")
        exit()
    else:
        print()