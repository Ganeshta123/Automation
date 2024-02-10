#Test case1: Login to orangehrmlive page and verify the title of the page
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element("name",'username').send_keys("Admin")
time.sleep(5)
driver.find_element("name","password").send_keys("admin123")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@type="submit"]').click()
time.sleep(5)
act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("pass")
else:
    print("fail")