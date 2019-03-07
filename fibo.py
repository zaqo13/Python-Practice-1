def fastFib (n, memo):
    global numCalls
    numCalls +=1
    print('fibi called with',n)
    if not n in memo:
        memo[n] = fastFib (n-1, memo)+ fastFib(n-2, memo)
    return memo[n]

def fibi (n):
    memo = {0:1, 1:1}
    return fastFib(n, memo)

