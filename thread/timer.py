import threading

def delayed_func():
	print('hi')

if __name__ == '__main__':
    t = threading.Timer(2, delayed_func)
    t.start()
    print('print after 2 secs')