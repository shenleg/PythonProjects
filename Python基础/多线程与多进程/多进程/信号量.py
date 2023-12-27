import multiprocessing

# 创建信号量，初始计数器为2
semaphore = multiprocessing.Semaphore(2)


def worker():
    # 获取信号量
    semaphore.acquire()
    try:
        # 访问共享资源
        print("Worker is accessing the shared resource")
    finally:
        # 释放信号量
        semaphore.release()


# 创建多个进程并启动
processes = []
for _ in range(5):
    p = multiprocessing.Process(target=worker)
    processes.append(p)
    p.start()

# 等待所有进程结束
for p in processes:
    p.join()

print("All processes finished")
