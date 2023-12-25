# https://cuiqingcai.com/3335.html

import multiprocessing


def producer(queue):
    for i in range(5):
        message = f"Message {i}"
        queue.put(message)
        print(f"Producer put: {message}")


def consumer(queue):
    while True:
        message = queue.get()
        if message == "DONE":
            break
        print(f"Consumer got: {message}")


if __name__ == "__main__":
    # 创建队列
    queue = multiprocessing.Queue()
    # 创建生产者进程和消费者进程
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))
    # 启动进程
    producer_process.start()
    consumer_process.start()
    # 等待生产者进程结束
    producer_process.join()
    # 在队列中放置结束信号
    queue.put("DONE")
    # 等待消费者进程结束
    consumer_process.join()

    print("All processes finished")
