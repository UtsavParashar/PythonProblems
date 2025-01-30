import multiprocessing
import time

def deposit(balance, lock):
    for _ in range(100):
        time.sleep(.001)
        lock.acquire()
        balance.value += 1
        lock.release()


def withdraw(balance, lock):
    for _ in range(100):
        time.sleep(.0011)
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == '__main__':

    lock = multiprocessing.Lock()

    balance = multiprocessing.Value('d', 200)

    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(f'Final Balance - {balance.value}')