# -*- coding: utf-8 -*-
import sys, io
import re
import requests as rq
import time
import os
import threading

class SpiderThread(threading.Thread):
    def __init__(self, url, keyword, num_img_pages, wait_list):
        super().__init__()

        # mutex
        self.mutex = threading.Lock()
        
        # re patterns
        self.big_img_pattern = '<ul id="post-list-posts">(.*?)</ul>'
        self.img_pattern = '</div><a class=".*?" href="(.*?)"><span class=".*?"><span class=".*?">'

        # settings
        self.url = url
        self.keyword = keyword
        self.num_img_pages = num_img_pages
        self.wait_list = wait_list
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            # 'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
            # 'accept-encoding': 'gzip, deflate, br',
            # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }

    def run(self):
        print('[Spider] Spider thread is running ...')
        for page_id in range(self.num_img_pages):
            res = rq.get(self.url+'post?page='+str(page_id+1)+'&tags='+str(self.keyword), headers=self.headers)
            res.encoding = 'utf-8'
            if res.status_code != 200:
                print('[Spider] Cannot get page {}! Skip to next page!'.format(page_id+1))
                continue
            print('[Spider] Collecting from {} ...'.format(res.url))
            pic_url_big = re.findall(self.big_img_pattern, res.text, re.S)[0]
            pic_url = re.findall(self.img_pattern, pic_url_big, re.S)
            self.mutex.acquire() # lock the waiting list
            self.wait_list += pic_url # extend waiting list
            self.mutex.release() # unlock
        print('[Spider] Image urls of all pages are collected. Spider thread finished.')

class DownloadThread(threading.Thread):
    def __init__(self, wait_list, save_path):
        super().__init__()

        # mutex
        self.mutex = threading.Lock()

        # settings
        self.wait_list = wait_list
        self.save_path = save_path
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        }

    def run(self):
        while True:
            self.mutex.acquire()
            if len(self.wait_list) != 0:
                download_url = self.wait_list.pop(0)

                # download
                res = rq.get(download_url, headers=self.headers)
                if res.status_code != 200:
                    print('[Downloader] Thread {} cannot download {}!'.format(self.name, download_url))

                # save to local file
                download_url = download_url.split('/')[-1]
                try:
                    with open(self.save_path+'/'+download_url, 'wb') as f:
                        f.write(res.content)
                    print('[Downloader] '+download_url+' is saved. Remaining: {}'.format(len(self.wait_list)))
                except:
                    print('[Downloader] Cannot save to local!')
            else:
                break            
            self.mutex.release()
        print('[Downloader] Download waiting list is empty, downloading finished on thread {}.'.format(self.name))

if __name__ == "__main__":
    wait_list = []
    save_path = './imgs'
    keyword = 'long_hair'
    pages = 3
    url = 'https://konachan.net/'
    
    # initiate crawler thread
    crawler = SpiderThread(url, keyword, pages, wait_list)
    crawler.start()

    # initiate downloading thread
    d1 = DownloadThread(wait_list, save_path)
    d1.setName = 'downloader 1'
    d2 = DownloadThread(wait_list, save_path)
    d2.setName = 'downloader 2'
    d3 = DownloadThread(wait_list, save_path)
    d3.setName = 'downloader 3'

    time.sleep(5)

    if len(wait_list) > 0:
        d1.start()
        d2.start()
        d3.start()