import random
from threading import Event, Thread
from time import sleep

MAX_N = 7


def printer(id: int, message: str, wait_for: Event, notify_who: Event):
    print(f'start {id}: {message} {wait_for} {notify_who}')
    for _ in range(10):
        wait_for.wait()
        wait_for.clear()
        print(message)
        sleep(0.1 * random.randint(3, 5))
        notify_who.set()


def main():
    events = [Event() for _ in range(MAX_N)]

    it = zip(events, events[1:] + events)

    threads = [
        Thread(target=printer, args=(i, str(i), *next(it))) for i in range(MAX_N)
    ]

    for t in threads:
        t.start()

    events[0].set()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
