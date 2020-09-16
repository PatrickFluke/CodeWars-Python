#Migraine today, I think this was an all right solution.

def is_prime(num):
    prime = True
    if num < 2:
        prime = False;
    else:
        for x in range(2,num-1):
            if (num % x) == 0:
                prime = False;
                break;
            if x*x > num:
                break;
    return prime;
