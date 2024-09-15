def fatc(n):
    if(n == 0):
        return 1
    
    return n * fatc(n-1)

print(fatc(5))