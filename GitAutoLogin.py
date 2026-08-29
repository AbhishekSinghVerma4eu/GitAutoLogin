from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
import time

usr = input("Username or email address: ")
pwd = getpass("Password: ")

driver = webdriver.Chrome()
driver.get("https://github.com/login")

username_box = driver.find_element(By.XPATH,"//*[@id='login_field']")
username_box.send_keys(usr)

password_box = driver.find_element (By.XPATH,"//*[@id='password']")
password_box.send_keys(pwd)

sign_in_btn = driver.find_element(By.NAME,("commit"))
sign_in_btn.submit()
time.sleep(10)
driver.quit()