import multiprocessing
import time


def square(x):
    time.sleep(1)
    return x ** 2


if __name__ == "__main__":
    # 创建进程池，指定进程数量为3，默认自动选择进程数量
    pool = multiprocessing.Pool(processes=3)

    # 准备任务列表
    numbers = [1, 2, 3, 4, 5]

    # 使用进程池执行任务，会阻塞主进程
    results = [pool.apply(square, (num,)) for num in numbers]

    # 执行其他代码
    print("Other code")

    # 打印结果
    print("Results:", results)

    # 关闭进程池
    pool.close()
    pool.join()

    print("All tasks completed")
