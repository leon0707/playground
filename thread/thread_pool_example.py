import logging
import threading
import time
import concurrent.futures

def thread_function(x):
    logging.info("Thread %s: starting", x)
    time.sleep(2)
    logging.info("Thread %s: finishing", x)
    return x

def thread_function_no_parameter():
    logging.info("Thread %s: starting")
    # time.sleep(2)
    logging.info("Thread %s: finishing")
    return 'finished'

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(3) as executor:
        res = executor.map(thread_function, range(3)) # when use map, the thread_function must take parameters
        for i in res:
            print(i)

    with concurrent.futures.ThreadPoolExecutor(4) as executor:
        # future = executor.submit(thread_function_no_parameter) # when use submit, function may not take parameters
        # print(future.result())
        for i in range(4):
            executor.submit(thread_function_no_parameter)
            # the 4th execution of thread_function_no_parameter will wait for one thread to complete first


    
