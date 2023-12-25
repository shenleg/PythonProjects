import time
import multiprocessing


def worker():
    name = multiprocessing.current_process().name
    print(f"Worker {name} started")
    time.sleep(2)
    print(f"Worker {name} finished")


if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    # 等待所有子进程结束
    for p in processes:
        p.join()

    print("All processes finished")
