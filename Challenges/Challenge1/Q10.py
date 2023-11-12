def fib_Recur(n):
    if n<= 0:
        return[]
    if n==1:
        return[0]
    if(n==2):
        return[0,1]
    else:
        fib_seq = fib_Recur(n-1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

n_term = 13
result = fib_Recur(n_term)
print(result)
