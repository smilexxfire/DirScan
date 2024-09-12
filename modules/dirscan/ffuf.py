# -*- coding: UTF-8 -*-
'''
@Project ：DirScan 
@File    ：ffuf.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/12 11:46 
@Comment ： 
'''
import json
import os
import subprocess

from common.module import Module
from config.settings import MONGO_COLLECTION
from config.settings import data_dic_dir
from config.log import logger

class Ffuf(Module):
    def __init__(self, url, dir_file):
        self.modules = "dirscan"
        self.source ="ffuf"
        self.collection = MONGO_COLLECTION
        self.target = url + "/FUZZ"
        self.word_list = data_dic_dir.joinpath(dir_file)
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        Module.__init__(self)

    def do_scan(self):
        cmd = [self.execute_path, "-w", self.word_list, "-u", self.target, "-H", f"user-agent: {self.ua}",
               "-json", "-o", self.result_file]
        subprocess.run(cmd)

    def deal_data(self):
        logger.log("INFOR", "Start deal data process")
        if not os.path.exists(self.result_file):
            return
        with open(self.result_file, "r", encoding="utf8") as f:
            datas = json.loads(f.read())["results"]
            for data in datas:
                del data["resultfile"]
                del data["scraper"]
                del data["duration"]
                del data["position"]
            self.results = datas

    def save_db(self):
        # print(self.results)
        super().save_db()

    def run(self):
        self.begin()
        self.do_scan()
        self.deal_data()
        self.save_db()
        self.delete_temp()
        self.finish()
def run(url, dir_file):
    ffuf = Ffuf(url, dir_file)
    ffuf.run()

if __name__ == '__main__':
    run("https://qiniu.xxf.world", "dicc.txt")
    run("https://qiniu.xxf.world", "备份.txt")





