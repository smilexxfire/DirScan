# -*- coding: UTF-8 -*-
'''
@Project ：DirScan 
@File    ：dirscan_worker.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/12 12:26 
@Comment ： 
'''
import json
from common.database.consumer import RabbitMQConsumer
from modules.dirscan import ffuf
from config.settings import RABBITMQ_QUEUE_NAME

class DirScanWorker(RabbitMQConsumer):
    def __init__(self, queue_name):
        super().__init__(queue_name)

    def task_handle(self):
        task = json.loads(self.message)
        ffuf.run(task["url"], task["dir_file"])

if __name__ == '__main__':
    # 启动子域名扫描服务
    worker = DirScanWorker(RABBITMQ_QUEUE_NAME)
    worker.start_consuming()