import time
import multiprocessing


def daemon_process():
    while True:
        print("Daemon process is running...")
        time.sleep(1)


if __name__ == "__main__":
    daemon = multiprocessing.Process(target=daemon_process)
    # 标记为守护进程
    # 特征：当主进程结束时，守护进程也会被终止，防止进程无法退出
    daemon.daemon = True
    daemon.start()

    # 主进程继续执行其他任务
    time.sleep(5)
    print("Main process is done.")
