
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyperclip
import pyautogui





def countUP2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://accounts.kakao.com/login?continue=https%3A%2F%2Fcreators.kakao.com'
    driver.get(url)
    driver.maximize_window 
    action = ActionChains(driver)

    #아이디
    pyperclip.copy(USER_ID)
    driver.find_element_by_css_selector('#id_email_2_label').click()
    time.sleep(2)  
    pyautogui.hotkey('ctrl', 'v')

    pyperclip.copy(USER_PWD)
    driver.find_element_by_css_selector('.id_password_3_label').click()
    time.sleep(2)  
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(2)  
    driver.find_element_by_css_selector('.id_password_3_label').click()



