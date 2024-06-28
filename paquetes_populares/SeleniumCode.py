# no poner Selenium.py como nombre
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)
browser.get("https://github.com")

link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys(os.environ.get("gh_user"))
user_input.send_keys(os.environ.get("gh_pass"))