import random
import time
import multiprocessing
import numpy
arrsize = 1000000
NUM_CPU = 4
chunksize = int(arrsize/NUM_CPU)
lock = multiprocessing.Lock()
glob = multiprocessing.Value('i',0)
def generate():
    arr = []
    for i in range(arrsize):
        arr.append(random.randint(0,100000000))
    return arr
def findmax(start,stop,A,glob):
    for i in range (start,stop):
        if A[i] > glob.value :
            with lock:
                glob.value = A[i]
if __name__ == '__main__':
    ptr = 0
    A = generate()
    proc = []
    st = time.time()
    for i in range (NUM_CPU):
        p = multiprocessing.Process(target = findmax, args = (ptr,ptr+chunksize,A,glob))
        proc.append(p)
        ptr = ptr+chunksize
    for p in proc:
        p.start()
    for p in proc:
        p.join()
    et = time.time()
    print(f"Global maxima : {glob.value}")
    print(f"\nExecution time: {((et-st)*1000)} ms.")
