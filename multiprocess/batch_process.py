import multiprocessing as mp
import os
import time
import queue
import weakref
import threading

class Task(object):
    def __init__(self, id):
        self._id = id
        self._finish_event = threading.Event()
        self.__result = None

    def set_result(self, res):
        self.__result = res
        self._finish_event.set()

    def get_result(self, timeout=None):
        finished = self._finish_event.wait(timeout)
        if not finished:
            # if task is not finished within time period
            raise TimeoutError("Task: %d Timeout" % self._id)
        # return result
        return self.__result

    def _remove_from_cache(self):
        cache = self._cache_ref()
        if cache:
            del cache[self._id]

class _TaskCache(dict):
    'Dict for weakref only'
    pass


class Worker(object):
    def __init__(self, input_queue, output_queue, batch_size, batch_func):
        self._input_queue = input_queue
        self._output_queue = output_queue
        self._batch_size = batch_size
        self.batch_func = batch_func

    def loop_run(self):
        worker_id = os.getpid()
        print('worker {} starts working'.format(worker_id))
        timer_1 = time.time()
        counter = 0
        batch = []
        while True:
            batch = self.__fill_batch()
            if batch:
                inputs = [req for task_id, req in batch] # batch func doesn't need task_id
                results = self.batch_func(inputs)
                for i in range(len(batch)):
                    # find the coresponding result
                    self.__process_result(batch[i][0], results[i])
                print('worker {} processes {}'.format(worker_id, len(results)))
            else:
                time.sleep(0.01)

    def __fill_batch(self):
        batch = []
        timer_1 = time.time()
        for i in range(self._batch_size):
            try:
                task_tuple = self._input_queue.get(block=False)
                batch.append(task_tuple)
            except queue.Empty as e:
                break
        return batch

    def __process_result(self, task_id, result):
        self._output_queue.put((task_id, result))


class BatchProcessor(object):

    def __init__(self, batch_func, worker_num=1, batch_size=32, task_wait_time=4):
        self._current_task_id_obj = mp.Value('i', 0, lock=True)
        self._input_queue = mp.Queue() # queue can be full and raise exception
        self._output_queue = mp.Queue()
        self._task_wait_time = task_wait_time

        self._cache_ref = _TaskCache() # a dict to save result of task

        self._result_collector = threading.Thread(target=self.__loop_collect_result, daemon=True)
        self._result_collector.start()

        self._worker = Worker(self._input_queue, self._output_queue, batch_size, batch_func)
        self._worker_ps = []
        for i in range(worker_num):
            p = mp.Process(target=self._worker.loop_run, name='batch_worker', daemon=True)
            self._worker_ps.append(p)
            p.start()

    def __loop_collect_result(self):
        # infinite loop to collect result from output queue
        while True:
            try:
                task_id, res = self._output_queue.get(block=False)
                task = self._cache_ref[task_id]
                task.set_result(res)
            except queue.Empty as e:
                pass # or sleep

    def __add_request(self, req):
        with self._current_task_id_obj.get_lock():
            task_id = self._current_task_id_obj.value
            self._current_task_id_obj.value += 1
        task = Task(task_id)
        self._cache_ref[task_id] = task
        self._input_queue.put((task_id, req))
        return task_id

    def __get_result(self, task_id):
        task = self._cache_ref[task_id]
        try:
            res = task.get_result(self._task_wait_time)
        except Exception as e:
            print('have an exception')
            res = None
        # delete task from cache
        self.__delete_task(task_id)
        return res

    def __delete_task(self, task_id):
        if task_id in self._cache_ref:
            del self._cache_ref[task_id]

    def process(self, input_val):
        task_id = self.__add_request(input_val)
        res = self.__get_result(task_id)
        return res


def batch_func(batch):
    return [v + v for v in batch]

def create_bulk_request(n, processor):
    processor.process(n)

if __name__ == '__main__':
    mp.set_start_method('spawn')
    processor = BatchProcessor(batch_func, worker_num=2)
    
    threads = []
    for i in range(2000):
        t = threading.Thread(target=create_bulk_request, args=(i, processor))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
