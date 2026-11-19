from selenium import webdriver
import time

driver = webdriver.Chrome()

time.sleep(1)

driver.maximize_window()

url = "https://www.google.com/"
driver.get(url)
time.sleep(2)
driver.get("https://sheguidesme.com/")
time.sleep(1)

print("the current url is", driver.current_url)

print("The title is", driver.title)

driver.refresh()
time.sleep(1)

driver.back()
time.sleep(1)

driver.forward()
time.sleep(1)

assert driver.current_url == "https://sheguidesme.com/" ,"Driver is not in that page"
print("Driver is in the " +driver.current_url+ " page")

assert driver.title == "sheguidesme", "Driver is not on the page"
print("Driver is in sheguidesme page")

driver.quit()