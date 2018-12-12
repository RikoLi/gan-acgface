# -*- coding: utf-8 -*-
# 对Konachan的图片抓取
# Made by Acokil
# in 2016/2/21
import re
import requests
import time
import os


def get_number():
    konachan = requests.get("https://konachan.net/")
    number_url = re.findall('<img src="/images/(.)\.gif"/>', konachan.text, re.S)
    a = ''
    for num in number_url:
        a += str(num)
    return int(a)


pictures = input("How many pictures you want to download:")
pictures = int(pictures)
tag = input('What tag:')
print("Download will begin soon...")

# 下载模块
i = 0
for x in range(1, pictures):
    html = requests.get('https://konachan.net/post?page='+str(x)+'&tags='+str(tag))
    pic_url_big = re.findall('<ul id="post-list-posts">(.*?)</ul>', html.text, re.S)[0]
    pic_url = re.findall('</div><a class=".*?" href="(.*?)"><span class=".*?"><span class=".*?">', pic_url_big, re.S)
    for each in pic_url:
        print("Now downloading:\n"+'Pictures:'+str(i+1)+'\n', each)
        pic = requests.get(each)
        f = open('../datasets/imgbuffer2/'+str(i+1)+'.jpg', 'wb')
        f.write(pic.content)
        f.close()
        i += 1
        if i >= pictures:
            break
    if i >= pictures:
        break