import logging
import threading
import time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        with self._lock:
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
        logging.info("Thread %s: finishing update", name)

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    db = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", db.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        for index in range(30):
            executor.submit(db.update, index)
    logging.info("Testing update. Ending value is %d.", db.value)