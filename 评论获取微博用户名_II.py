import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def check_findmore():
    try:
        driver.find_element_by_xpath(
            '//*[@id="Pl_Official_WeiboDetail__74"]'
            '/div/div/div/div[4]/div/div[2]/div[2]'
            '/div/div/a/span')#能否找到查看更多
    except:
        text='break'#找不到那就返回退出
    else:#找到就点击,并返回继续
        driver.find_element_by_xpath(
            '//*[@id="Pl_Official_WeiboDetail__74"]'
            '/div/div/div/div[4]/div/div[2]/div[2]'
            '/div/div/a/span').click()
        for j in range(3):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
        text='continue'
    return text

def find_name():
    for i in range(99999):
        time.sleep(0.5)
        try:
            weibo_name = driver.find_element_by_xpath(
                '//*[@id="Pl_Official_WeiboDetail__74"]'
                '/div/div/div/div[4]/div/div[2]/div[2]'
                '/div/div/div['+str(i+1)+']/div[2]/div[1]/a[1]')
            if weibo_name.text!='日食记':
                print(weibo_name.text)
                save_name(weibo_name.text)
        except:
            check_findmore()
        else:
            continue
    return

def save_name(name):
    f = open('C:' + '\\Users' + '\Administrator\Desktop' + '\\test\\' + 'Name.txt', 'a')
    f.write(name + '\n')
    f.close()

def login_in():
    driver.find_element_by_xpath('//*[@id="pl_common_top"]'
                                 '/div/div/div[3]/div[2]/ul/li[3]/a').click()#点击登录
    driver.find_element_by_id('layer_14978632578041')
url = 'http://weibo.com/3948713134/F7PmeeOyH?filter=hot&root_comment_id=0&type=comment'
path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
driver.maximize_window()
time.sleep(3)

for i in range(3):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)#屏幕移动到最低，方便加载更多
login_in()
#find_name()







