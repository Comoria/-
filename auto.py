from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#vpn
from smspva import SMSpva
from smspva.countries import Country
from smspva.services import Service


import time
import pyperclip
import pyautogui


driver = webdriver.Chrome(executable_path='C:/Users/moa/Documents/mProject/smspva-master/smspva-master/chromedriver.exe')
url = 'https://naver.com'
driver.get(url)
driver.maximize_window 
action = ActionChains(driver)

driver.find_element_by_css_selector('.link_join').click()

#time.sleep(2000)
driver.find_element_by_css_selector('.input_chk').click()
#time.sleep(2000)
driver.find_element_by_css_selector('#btnAgree').click()

pyperclip.copy('ksjjj121')
driver.find_element_by_css_selector('#id').click()
time.sleep(2)  
pyautogui.hotkey('ctrl', 'v')

#action.send_keys('akook2dd9d2').perform()
time.sleep(2)  
driver.find_element_by_css_selector('#pswd1').click()
pyperclip.copy('qlal1004')
pyautogui.hotkey('ctrl', 'v')
#action.send_keys('qlal1004').perform()
time.sleep(2)  
driver.find_element_by_css_selector('#pswd2').click()
pyperclip.copy('qlal1004')
pyautogui.hotkey('ctrl', 'v')
#action.send_keys('qlal1004').perform()
time.sleep(3)  
driver.find_element_by_css_selector('#name').click()
pyperclip.copy('강민지')
pyautogui.hotkey('ctrl', 'v')
#action.send_keys('강민지').perform()
time.sleep(4)  
driver.find_element_by_css_selector('#yy').click()
pyperclip.copy('1991')
pyautogui.hotkey('ctrl', 'v')
#action.send_keys('1991').perform()
time.sleep(3)  
driver.find_element_by_css_selector('#mm').click()
action.send_keys('12').perform()
#pyperclip.copy('12')
#pyautogui.hotkey('ctrl', 'v')
time.sleep(2)  
driver.find_element_by_css_selector('#dd').click()
time.sleep(1)
pyperclip.copy('5')
pyautogui.hotkey('ctrl', 'v')
action.key_down(Keys.TAB).key_down(Keys.DOWN).key_down(Keys.DOWN).perform()
# action.send_keys('5').key_down(Keys.TAB).key_down(Keys.DOWN).key_down(Keys.DOWN).perform()
time.sleep(2)  

driver.find_element_by_css_selector('#nationNo').click()
time.sleep(1)
action.key_down(Keys.HOME).perform()
time.sleep(1)

# 40 루마니아  +40
# 112 아르헨티나 +54
# 197 폴란드  +48

#key = open("key").read()
client = SMSpva('bsmjQttxKxW5sfHuebNTnh4KGbgeMo')

# relatively complete example
service = Service.NAVER
country = client.get_cheapest_country(service)
if country is not None:
    request = client.request_sms(service, country)
    request.send()
#    print(request.full_number)
    print(request.country_code)
#    print(request.number)
    
    print(request.country_code=="+40")
    print(request.country_code=="+54")
    print(request.country_code=="+48")

    if request.country_code == "+40": 
        downCnt = 40  #루마니아
    elif request.country_code == "+54" :
        downCnt = 112  # 아르헨티나
    elif request.country_code == "+48" :
        downCnt = 197  #폴란드
    else :
        print("service not available.")
    
    print("키다운시작")
    for i in range(downCnt) :
        action.key_down(Keys.DOWN).perform()
    time.sleep(2)  
    print("엔터텝")   
    action.key_down(Keys.ENTER).perform()

    driver.find_element_by_css_selector('#phoneNo').click()
    pyperclip.copy(request.number)
    pyautogui.hotkey('ctrl', 'v')
    #action.send_keys(request.number).perform()    
    time.sleep(3)  

    print("인증번호 생성번튼")   
    driver.find_element_by_css_selector('#btnSend').click()
    time.sleep(3)  
    sCode = request.run() 
    print(sCode)
    time.sleep(5)  
    print("인증번호 압력")   
    driver.find_element_by_css_selector('#authNo').click()   
    pyperclip.copy(sCode)
    pyautogui.hotkey('ctrl', 'v')
    # action.send_keys(sCode).perform()    
    time.sleep(3)
    action.key_down(Keys.TAB).perform()
    time.sleep(3)
    action.key_down(Keys.ENTER).perform()

#    print("회원가입")   
#    time.sleep(3)       
#    driver.find_element_by_css_selector('#btnJoin').click()      
    

while 1 :input("종료할려면 엔터")

else:
    print("service not available.")




