#saucedemo page
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#initialize chrome or different website with webriver
driver = webdriver.Chrome()

#maximize the window screen
driver.maximize_window()

#Navigate to url
url ="https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)

'''
ID Locators
username = user-name
password = password
login_button = login-button


XPATH Locators (only used when id, class name are  not found)
username : 
Relative Xpath for username
//*[@id="user-name"] , 
Absolute xpath
/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input

password:
 Relative XPath
 //*[@id="password"]
 Absolute
 /html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input

 login_button
 //*[@id="login-button"]

'''


#Locators
username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
# username = driver.find_element(By.ID, "user-name")
# password = driver.find_element(By.ID, "password")
password = driver.find_element(By.XPATH, '//*[@id="password"]')
login_button = driver.find_element(By.ID, "login-button")

#Actions
username.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(1)
login_button.click()
time.sleep(2)

#ASSERTION
# if driver.current_url =="https://www.saucedemo.com/inventory.html":
#     print("Login Successful")
# else:
#     print("Login unsuccessful")

# assert driver.current_url =="https://www.saucedemo.com/inventory.html", "Login unsucessfull"
# print("Login Successful")
driver.quit()


#from this element give me python selenium locators (for chatgpt)
#clerear, clicked 
#copy xpath and go to dev tool, ctrl+f and paste the xpath to know whre the xpath is