import random
import time
import multiprocessing
import numpy
arrsize = 1000000
NUM_CPU = 4
chunksize = int(arrsize/NUM_CPU)
lock = multiprocessing.Lock()
def generate():
    arr = []
    for i in range(arrsize):
        arr.append(random.randint(0,100000000))
    return arr
def generateC():
	manager = multiprocessing.Manager()
	arr = manager.list()
	return arr
def findmax(start,stop,A,glob):
    local = 0
    for i in range (start,stop):
        if A[i] > local :
            local = A[i]
    glob.append(local)
if __name__ == '__main__':
    ptr = 0
    A = generate()
    glob = generateC()
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
    print(f"Local maxima : {glob}")
    print(f"Global maxima : {max(glob)}")
    print(f"\nExecution time: {((et-st)*1000)} ms.")
