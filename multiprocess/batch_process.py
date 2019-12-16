import multiprocessing as mp
import os
import time
import queue

def worker(q, results):
    batch_size = 36
    worker_id = os.getpid()
    print('worker {} starts working'.format(worker_id))
    timer_1 = time.time()
    counter = 0
    batch = []
    while True:
        try:
            val = q.get(block=False)
            batch.append(val)
            timer_1 = time.time()
            if len(batch) == batch_size:
                raise queue.Empty()
        except queue.Empty as e:
            if len(batch):
                print('worker {} processes {}'.format(worker_id, len(batch)))
                counter += len(batch)
                batch = []
            else:
                time.sleep(0.01)
                if time.time() - timer_1 > 5:
                    print('worker {} exits'.format(worker_id))
                    break

    results.put((worker_id, counter))


if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    workers = []
    results = mp.Queue()
    for i in range(3):
        p = mp.Process(target=worker, args=(q, results))
        workers.append(p)
        p.start()

    for i in range(15000):
        q.put(i)

    for w in workers:
        w.join()

    while not results.empty():
        print(results.get())
