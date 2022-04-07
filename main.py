import random

from concurrent import futures
from multiprocessing import Queue


class TaskManager:
    def __init__(self, pool, io_manager):
        self._pool = pool
        self._io_manager = io_manager

    def run():
        pass

    def get_task(self):
        pass


class IOManager:
    def __init__(self):
        pass

    def read(self):
        pass

    def write(self):
        pass


def main():
    tm = TaskManager(futures.ProcessPoolExecutor())
    io_manager = IOManager()
    tm.run()


if __name__ == '__main__':
    main()
