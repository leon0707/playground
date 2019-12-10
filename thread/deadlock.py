import threading
import time
import logging


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


def acquire_a_b(a, b):
	logging.info("t1 wants to acquire a")
	a.acquire()
	logging.info("t1 acquires a")
	time.sleep(1)
	logging.info("t1 wants to acquire b")
	b.acquire()
	logging.info("t1 acquires b")
	a.release()
	b.release()

def acquire_b_a(a, b):
	logging.info("t2 wants to acquire b")
	b.acquire()
	logging.info("t2 acquires b")
	time.sleep(1)
	logging.info("t2 wants to acquire a")
	a.acquire()
	logging.info("t2 acquires a")
	b.release()
	a.release()

if __name__ == '__main__':
	a = threading.Lock()
	b = threading.Lock()
	t1 = threading.Thread(target=acquire_a_b, args=(a, b))
	t2 = threading.Thread(target=acquire_b_a, args=(a, b))
	t1.start()
	t2.start()
	t1.join()
	t2.join()