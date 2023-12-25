import time
import multiprocessing

def daemon_process():
    while True:
        print("Daemon process is running...")
        time.sleep(1)

if __name__ == "__main__":
    daemon = multiprocessing.Process(target=daemon_process)
    # daemon.daemon = True  # 设置为守护进程
    daemon.start()

    # 主进程继续执行其他任务
    time.sleep(5)
    print("Main process is done.")