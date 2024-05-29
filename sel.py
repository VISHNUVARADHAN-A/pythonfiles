from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Edge()

browser.get('https://money.rediff.com/gainers/bse/daily/groupa')

browser.maximize_window() 
# #time.sleep(5)
# a= browser.find_element(By.XPATH,"//*[@id='edit-select-138']/a").text
# # time.sleep(5)
# #browser.find_element(By.XPATH,'//*[@class="tabbed-content__right"]/ol/li[1]/a').click()
# browser.find_element(By.XPATH,"//*[@id='SIvCob']/a[2]").click()
# print(browser.find_element(By.XPATH,"//*[@id='SIvCob']/a[5]").text)
# time.sleep(2)
# print(browser.find_element(By.XPATH,"//*[@class='title-section__title']").text)

#child
# childs=browser.find_elements(By.XPATH,"//a[contains(text(),'HLE Glascoat')]/ancestor::tr/child::td")
# ancestor=browser.find_elements(By.XPATH,"//a[contains(text(),'HLE Glascoat')]/ancestor::tr/ancestor::*")
# print(len(ancestor))
# print(len(childs))#5
# print(browser.title)
# print(browser.name)
# print(browser.current_url)
print(browser.__class__)
#print(browser.page_source)
# for i in childs:
#     print(i)
browser.quit()
