from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    # 子进程要执行的任务
    def run(self):
        result = self.a + self.b
        print(f"{self.a} + {self.b} = {result}")


if __name__ == '__main__':
    # 创建两个子进程，分别执行两次加法计算
    p1 = MyProcess(2, 3)
    p2 = MyProcess(5, 7)
    # 启动子进程
    p1.start()
    p2.start()
    # 等待子进程执行完成，并回收资源
    p1.join()
    p2.join()
    print('Main process Ended!')
