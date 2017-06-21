import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import progressbar#进度条模块
import sys
import os
'''
保存视频固定模块
G:\weibo\weibo_video
'''

def save_content(num,content):
    f = open('G:\weibo\weibo_video\\' + 'content.txt', 'a')
    f.write(str(num) +'、'+ content + '\n')
    f.close()

def save_video(name):
    videosrc=driver.find_element_by_tag_name('video').get_attribute('src')
    r=requests.get(videosrc,stream=True)
    #save_video_makepath=os.mkdir('G:\weibo\weibo_video\\'+str(name))
    bar = progressbar.ProgressBar(max_value=int(r.headers['content-length']))

    with open('G:\weibo\weibo_video\\'+str(name)+'.mp4','wb') as fd:
        i=0
        for chunk in r.iter_content():
            fd.write(chunk)
            #time.sleep(0.1)
            i=i+1
            bar.update(i)
        print('ok!')
#############################################################
url = 'http://weibo.com/tv/vfun'
#path = r"D:\Program Files\Python36-32\Scripts\phantomjs.exe"
#driver = webdriver.PhantomJS(executable_path=path)
path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
driver.maximize_window()
time.sleep(5)

for i in range(3):
    driver.find_element_by_xpath\
        ('/html/body/div/div[4]/ul/a['+str(i+1)+']/li/div[1]/img').click()
    window=driver.window_handles
    driver.switch_to.window(window_name=window[1])
    time.sleep(10)
    content=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/div[1]').text
    save_content(i+1,content)
    save_video(i+1)
    driver.close()
    time.sleep(10)
    driver.switch_to.window(window_name=window[0])
#time.sleep(5)
####################################################
'''
如果有新窗口要重新window_handles一次
视频下载完成关闭窗口，先用单线程，以后修改成一边下载，一边打开新窗口，处理视频下载.

'''
######################################################
driver.quit()
'''
/html/body/div/div[4]/ul/a[1]/li/div[1]/img
/html/body/div/div[4]/ul/a[2]/li/div[1]/img

/html/body/div/div[4]/ul/a[297]/li/div[1]/img
a[i]----for 
'''
#driver.execute_script('window.scrollTo(0,500)')
#time.sleep(10)

'''
获取视频路径
'''
#print(driver.find_element_by_tag_name('video').get_attribute('src'))


