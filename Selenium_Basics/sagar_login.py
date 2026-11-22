#Sagar test login page
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

url = "https://sagar-test-qa.vercel.app/"
driver.get(url)
time.sleep(2)

'''
ID Loccatord
username: username
password: password
login_button: //*[@id="loginForm"]/button


'''
username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/button')

username.send_keys("user_name")
time.sleep(2)
password.send_keys("pass123")
time.sleep(1)
login_button.click()
time.sleep(2)

driver.quit()
