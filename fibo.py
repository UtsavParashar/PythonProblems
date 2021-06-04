# Fibonacci numbers module
def fib(n):
    def rec_fib(n1):
        if n1 in [0, 1]:
            return n1
        else:
            return rec_fib(n1 - 1) + rec_fib(n1 - 2)

    for i in range(n):
        print(rec_fib(i), end=' ')

def fib2(n:int) -> list: ## Fib returning list
    print('Running fib2')
    fib_list = [0,1]
    for i in range(n-2):
        fib_list.append(fib_list[-1] + fib_list[-2])
    print(fib_list)
    return fib_list