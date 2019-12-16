import multiprocessing
import os

def worker(idx):
    print('Worker {}'.format(idx))
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i, ))
        jobs.append(p)
        p.start()
