import multiprocessing


def worker(lock, shared_data):
    # 一般形式
    # lock.acquire()
    # access data
    # lock.release()

    # 简写形式
    with lock:
        # 在进入临界区之前获取锁
        print(f"Worker {multiprocessing.current_process().name} acquired the lock")
        # 访问共享资源
        shared_data.value += 1
        print(f"Worker {multiprocessing.current_process().name} modified the shared data")
        # 在离开临界区之前释放锁
        print(f"Worker {multiprocessing.current_process().name} released the lock")


if __name__ == "__main__":
    # 创建共享数据
    shared_data = multiprocessing.Value('i', 0)
    # 创建锁
    lock = multiprocessing.Lock()
    # 创建多个进程
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(lock, shared_data))
        processes.append(p)
        p.start()

    # 等待所有进程结束
    for p in processes:
        p.join()

    print("All processes finished")
    print("Final value of shared data:", shared_data.value)
