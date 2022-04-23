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



while 1 :input("종료할려면 엔터")

else:
    print("service not available.")






