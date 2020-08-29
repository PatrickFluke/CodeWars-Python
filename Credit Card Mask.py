# Again, I am fully aware this is likely longer than it has to be. I haven't yet looked at others solutions, but it works!
# return masked string
def maskify(cc):
    x = 1
    maskedNum = ""
    for a in cc:
        if x > len(cc) - 4:
            maskedNum = maskedNum + str(a)
        else:
            maskedNum = maskedNum + "#"
        x = x + 1
    return maskedNum
    pass
