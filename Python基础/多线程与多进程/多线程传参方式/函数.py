import threading


def worker(count):
    for i in range(count):
        print(i)


# 第一种方式，元组。注意不能少了逗号
thread1 = threading.Thread(target=worker, args=(5,))
thread1.start()

# 第二种方式，字典
thread1 = threading.Thread(target=worker, kwargs={"count": 8})
thread1.start()

print("master")
