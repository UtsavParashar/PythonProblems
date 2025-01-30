import multiprocessing
import time

def f(n):
    sums = 0
    for x in range(100000):
        sums += x*x
    return sums



if __name__ == '__main__':

    t1 = time.perf_counter()
    p = multiprocessing.Pool()
    result = p.map(f, range(1000))
    print(result)
    p.close()
    p.join()

    print(f'Time taken - {time.perf_counter() - t1}')

    t2 = time.perf_counter()
    for _ in range(1000):
        res = f(range(1000))
    print(res)
    print(f'Time taken - {time.perf_counter() - t2}')

