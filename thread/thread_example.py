import logging
import threading
import time
import concurrent.futures

def thread_function(x, result):
    # print(x)
    logging.info("Thread %s: starting", x)
    time.sleep(2)
    logging.info("Thread %s: finishing", x)
    result[0] = x

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    result = [None]
    x = threading.Thread(target=thread_function, args=(1, result)) # daemon = True thread will die if the program exits
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join() # main will wait for x to complete
    print(result[0])
    logging.info("Main    : all done")


    
