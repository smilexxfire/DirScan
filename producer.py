# -*- coding: UTF-8 -*-
'''
@Project ：DirScan 
@File    ：producer.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/12 12:28 
@Comment ： 
'''
import json

from common.database.producer import RabbitMQProducer
from config.settings import RABBITMQ_QUEUE_NAME

def purge_queue():
    """
    清空队列

    :param queue_name: 队列名称
    :return:
    """
    producer = RabbitMQProducer(RABBITMQ_QUEUE_NAME)
    producer.purge_queue()

def send_task(task):
    producer = RabbitMQProducer(RABBITMQ_QUEUE_NAME)
    producer.publish_message(json.dumps(task))

if __name__ == '__main__':
    task = {
        "url": "http://qiniu.xxf.world",
        "dir_file": "dicc.txt"
    }
    send_task(task)