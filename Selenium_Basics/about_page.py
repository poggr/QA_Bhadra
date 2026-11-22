#sagar test about page
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

url ="https://sagar-test-qa.vercel.app/about.html"
driver.get(url)
time.sleep(2)

'''
ID Locators:
full_name:fullname
phone:phone
email: email
hobby: hobby
submit_button: //*[@id="aboutForm"]/button
'''

full_name = driver.find_element(By.ID, "fullname")
phone = driver.find_element(By.ID, "phone")
email = driver.find_element(By.ID, "email")
hobby = driver.find_element(By.ID, "hobby")
submit_button = driver.find_element(By.XPATH, '//*[@id="aboutForm"]/button')

full_name.send_keys("Test")
time.sleep(2)
phone.send_keys(9841234567)
time.sleep(1)
email.send_keys("test@yahoo.com")
time.sleep(2)
hobby.send_keys("Games")
time.sleep(1)
submit_button.click()
time.sleep(2)

driver.quit()

