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



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
driver.get(url)
driver.maximize_window 
action = ActionChains(driver)


while 1 :input("종료할려면 엔터")

else:
    print("service not available.")






