def persistence(n):
    print("Starting: " + str(n))
    count = 0
    while len(str(n)) > 1:
        a = 1
        for x in list(str(n)):
            print("a: " + str(a))
            print("x: " + str(x))
            a = a * int(x)
            print("a * x = " + str(a))
        n = a
        count = count + 1
    return count
    # your code
