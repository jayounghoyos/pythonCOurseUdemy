from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)
browser.get("https://github.com")

#Cargar variables de entorno
load_dotenv(dotenv_path='paquetes_populares/.env')

gh_user = os.environ.get("gh_user")
browser.implicitly_wait(5)
gh_pass = os.environ.get("gh_pass")

if gh_user is None or gh_pass is None:
    raise ValueError("Las variables de entorno gh_user o gh_pass no están configuradas correctamente.")

link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys(os.environ.get("gh_user"))
user_input.send_keys(os.environ.get("gh_pass"))

browser.implicitly_wait(10)
pass_input.send_keys(Keys.RETURN)

profile = browser.find_element(By.CLASS_NAME,"css-truncate.css-target.ml-1")

label = profile.get_attribute("innerHTML")

assert "jayounghoyos" in label