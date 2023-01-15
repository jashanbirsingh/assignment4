for i in range(1, 200):
    num = True
    if i % 5 != 2:
        num = False
    if i % 6 != 3:
        num = False
    if i % 7 != 2:
        num = False
    if num == True:
        print(i)