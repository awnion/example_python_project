import asyncio
import multiprocessing as mp
import random
from concurrent.futures import ProcessPoolExecutor
from time import sleep
from typing import Awaitable, List, Tuple

CpuBoundResult = Tuple[int | None, int]


def cpu_bound(i: int) -> CpuBoundResult:
    process = mp.current_process()
    pid = process.pid
    print(pid, 'start')
    k = pow(i * random.randint(1, 4), i)
    sleep(0.1 * random.randint(1, 4))
    return pid, k % 99


async def main() -> None:
    tasks = [10**6] * 14 + [10**5] + [10**3] * 10
    jobs: List[Awaitable[CpuBoundResult]] = []

    with ProcessPoolExecutor() as pool:
        for t in tasks:
            jobs.append(asyncio.wrap_future(pool.submit(cpu_bound, t)))

        for j in asyncio.as_completed(jobs):
            print('-->', *await j)


if __name__ == '__main__':
    asyncio.run(main())
