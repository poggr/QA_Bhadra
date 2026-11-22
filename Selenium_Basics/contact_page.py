#sagar test about page
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

url ="https://sagar-test-qa.vercel.app/contact.html"
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

contact_name = driver.find_element(By.ID, "name")
email = driver.find_element(By.ID, "email")
message = driver.find_element(By.ID, "message")
submit_button = driver.find_element(By.XPATH, '//*[@id="contactForm"]/button')

contact_name.send_keys("Test")
time.sleep(2)
email.send_keys("test@yahoo.com")
time.sleep(2)
message.send_keys("this is test message")
time.sleep(1)
submit_button.click()
time.sleep(2)

driver.quit()

