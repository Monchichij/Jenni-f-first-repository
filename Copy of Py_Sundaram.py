def primes_era(n):
    # Eratothenes
    # primes smaller n
    n += 1
    
    marked = [True] * (n)
        
    for i in xrange(2, n):
        if marked[i]:
            for j in range(i*i, n, i):
                marked[j] = False

    the_list = [i for i in xrange(2, len(marked)) if marked[i] == True]
    return the_list

def primes_sun(n):
    # Sundaram: http://en.wikipedia.org/wiki/Sieve_of_Sundaram
    # n: integer
    # returns a list with primes <= n

    n = n/2
    
    marked = [True] * n

    for i in xrange(1, n):
        for j in xrange(i, (n-i)/(2*i+1)+1):
            if (i + j + 2 * i * j) >= len(marked):
                continue
            marked[i + j + 2 * i * j] = False

    the_list = [2*i+1 for i in xrange(0, len(marked)) if marked[i] == True]
    return the_list
