import multiprocessing


def sender(conn):
    message = "Hello from sender!"
    conn.send(message)  # 向管道发送消息
    conn.close()


def receiver(conn):
    message = conn.recv()  # 从管道接收消息
    print("Received message:", message)
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()  # 创建管道

    sender_process = multiprocessing.Process(target=sender, args=(parent_conn,))
    receiver_process = multiprocessing.Process(target=receiver, args=(child_conn,))

    sender_process.start()  # 启动发送进程
    receiver_process.start()  # 启动接收进程

    sender_process.join()
    receiver_process.join()
