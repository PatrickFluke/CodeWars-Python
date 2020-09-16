def find_outlier(integers):
    even = 0;
    odd = 0;
    #Might find first round, but will ultimately classify the set.
    for x in integers:
        if x % 2 == 0: even += 1;
        if x % 2 > 0: odd += 1;
        if even > 1 and x % 2 > 0: return x;
        if odd > 1 and x % 2 == 0: return x;
        
    #Catch all.
    for x in integers:
        if even > 1 and x % 2 > 0: return x;
        if odd > 1 and x % 2 == 0: return x;
    return None
