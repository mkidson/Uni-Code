from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://letterboxd.com/user/exportdata/")#put here the adress of your page
elem = driver.find_elements_by_xpath("//*[@id=\"modal\"]/article/div/div[2]/a")#put here the content you have put in Notepad, ie the XPath
# button = driver.find_element_by_id('buttonID') #Or find button by ID.
print(elem.get_attribute("class"))
elem.click()
driver.close()
