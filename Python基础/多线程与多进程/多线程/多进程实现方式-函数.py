import threading


# 子进程要执行的任务
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")


if __name__ == '__main__':
    # 创建两个子进程，分别执行两次加法计算
    p1 = threading.Thread(target=add, args=(2, 3))
    p2 = threading.Thread(target=add, args=(5, 7))
    # 启动子进程
    p1.start()
    p2.start()
    # 等待子进程执行完成，并回收资源
    p1.join()
    p2.join()
    print('Main process Ended!')
