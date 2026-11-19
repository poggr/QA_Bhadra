#import webdriver
from selenium import webdriver
import time

#initialize chrome or different website with webriver
driver = webdriver.Chrome()

#waits 3 sec
time.sleep(1)

#maximize the window screen
driver.maximize_window()

#Navigate to url
url ="https://www.google.com/"
driver.get(url)
time.sleep(2)
driver.get(" https://www.saucedemo.com/")
time.sleep(1)

#checks current url
print("The current url is: ", driver.current_url)

#gives the title of current page
print("The page title is ", driver.title)

#refresh the window/brower
driver.refresh()
time.sleep(1)

#browsers back navigation
driver.back()
time.sleep(1)

#browsers forward navigation
driver.forward()
time.sleep(1)

#Quit driver
driver.quit()