# Implementation of polynomial rolling hash function
# hash(s) = s[0] + s[1]*p + s[2]*p^2 + ... + s[n-1]*p^(n-1) mod m 

def to_hash(string: str):
    # As long as our string contains both low and upper case (total amount 52) 
    # prime number 53 is chosen for p
    p = 53
    
    m = 1e9 + 9
    hash = 0
    p_pow = 1
    for i in range(len(string)):
        hash = (hash + (ord(string[i]) - ord('a') + 1)*p_pow) % m
        p_pow = (p_pow * p) % m
    return hash