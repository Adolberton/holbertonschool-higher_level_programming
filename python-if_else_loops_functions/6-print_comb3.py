for i in range(10):
    for j in range(10):
        if j > i:
            if i == 8 and j == 9:
                print("{}{}".format(i, j), end="\n")
            else:
                print("{}{}".format(i, j), end=", ")
