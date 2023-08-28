import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

chrome_driver = webdriver.Chrome()
chrome_driver.get('https://priority_URL')
chrome_driver.maximize_window()
time.sleep(2)

chrome_driver.find_element(By.XPATH, '//*[@id="details-button"]').click()
time.sleep(2)
# input()
chrome_driver.find_element(By.XPATH, '//*[@id="proceed-link"]').click()
time.sleep(5)

username = chrome_driver.find_element(By.XPATH, '//*[@id="menuholder"]/div/table/tbody/tr/td/div/div[3]/table/tbody/tr[1]/td/div/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/input')
username.send_keys('Username')

password = chrome_driver.find_element(By.XPATH, '//*[@id="menuholder"]/div/table/tbody/tr/td/div/div[3]/table/tbody/tr[1]/td/div/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/input')
password.send_keys('P@ssw0rd')
password.send_keys(Keys.ENTER)
time.sleep(3)

language = chrome_driver.find_element(By.XPATH, '//*[@id="PriModalDialog"]/div/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/div').click()
company = chrome_driver.find_element(By.XPATH, '//*[@id="PriModalDialog"]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div')
company.click()

select_company = chrome_driver.find_element(By.XPATH, '//*[@id="PriModalDialog"]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/table/tbody/tr[2]/td/div/div/table/tbody[1]/tr[2]')
select_company.click()

accept = chrome_driver.find_element(By.XPATH, '//*[@id="PriModalDialog"]/div/table/tbody/tr[3]/td[2]/div[2]/div[1]/table/tbody/tr/td/div')
accept.click()

ksafim = chrome_driver.find_element(By.XPATH, '//*[@id="merk_menu_item_109475_0"]/div/img')
ksafim.click()
time.sleep(10)

finish = chrome_driver.find_element(By.XPATH, '//*[@id="reactModalBtns"]/button')
finish.click()

time.sleep(2)
