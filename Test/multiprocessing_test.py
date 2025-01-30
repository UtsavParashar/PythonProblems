import multiprocessing
import multiprocessing.process
import multiprocessing.queues

# shared memory for processes

def calc_square(numbers, result, v, q):
    v.value = 10.11
    for idx,n in enumerate(numbers):
        result[idx] = n*n
        q.put(n*n)
    print('Inside result', result[:])
    print('Inside Queue', q)


if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    # Shared Memory Data Structures
    result = multiprocessing.Array('i', 5)
    v = multiprocessing.Value('d', 0.1)
    q = multiprocessing.Queue()
    
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v, q))

    print(f'Value start {v.value}')

    p.start()
    p.join()

    print('Outside result', result[:])
    print('Value End', v.value)
    
    while not q.empty():
        print('Outside Queue', q.get())

    