from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


#bs4
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
driver.get(url)
driver.implicitly_wait(time_to_wait=2000) # 암시적으로 시간을 지정
driver.maximize_window 
action = ActionChains(driver)

#URL에 해당하는 페이지의 HTML를 가져옴
html = driver.page_source 

#가저온 코드로 bs4로 파싱하기
soup = BeautifulSoup(html, 'html.parser') 

xxxx = ul선택

url_list = []

for item in  ul(len):
    text= xpath~~ ul[item]
    url_list.append(text)    

with open('naver_news_covid19.csv','w',encoding='utf-8-sig') as f:
   writer = csv.writer(f)          
   writer.writerow(['title','paragraphs']) for row in ul_list: 
     writer.writerow(row)


while 1 :input("종료할려면 엔터")

else:
    print("service not available.")






