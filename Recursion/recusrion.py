

count = 1


def recusion():
    global count  # To use global variable in a function we do this, else it would consider count as local variable
    if count >= 6:  # BASE CONDITION
        return
    print(count)
    count += 1
    recusion()


recusion()
