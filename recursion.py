
# 5 * 4 * 3 * 2 * 1

def factoriel(n):
    
    if(n == 1):
        return n
    else:
        return n * factoriel(n - 1)

print(factoriel(5))
