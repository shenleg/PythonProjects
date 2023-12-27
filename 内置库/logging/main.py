import logging

# level: 捕获日志级别
# format: 日志输出格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

logging.debug('hello world')
logging.info('hello world')
logging.warning('hello world')
logging.error('hello world', exc_info=True)  # exc_info=True: 打印异常堆栈信息

