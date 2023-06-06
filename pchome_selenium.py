from bs4 import BeautifulSoup
from selenium import webdriver
#使用隱藏瀏覽器記得import
#from selenium.webdriver.chrome.options import Options
import time

#註解部分是隱藏瀏覽器的部分
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
#chrome_options.add_argument('--user-agent={}.format(userAgent)')
#chrome = webdriver.Chrome(options=chrome_options)

# 使用隱藏瀏覽器就不用加上第15行開啟瀏覽器
chrome = webdriver.Chrome()
chrome.get('https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone')
time.sleep(3)

for i in range(2):
	chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	time.sleep(1)

time.sleep(5)
pageSrc = chrome.page_source

soup = BeautifulSoup(pageSrc, 'html.parser')
# 使用隱藏瀏覽器就不用加上第28行關閉瀏覽器
chrome.close()

for prods in soup.find_all('h5', class_='prod_name'):
	print(prods.text)