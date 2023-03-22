from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://google.co.in")
driver.maximize_window()
time.sleep(5)
search_box = driver.find_element("name", "q")
search_box.send_keys('codechef')
time.sleep(5)
search_box.submit() 
time.sleep(5)
driver.close()