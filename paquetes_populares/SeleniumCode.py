from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv(dotenv_path='paquetes_populares/.env')

gh_user = os.environ.get("gh_user")
gh_pass = os.environ.get("gh_pass")

if gh_user is None or gh_pass is None:
    raise ValueError("Las variables de entorno gh_user o gh_pass no están configuradas correctamente.")

# Opciones del navegador
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://github.com")

# Iniciar sesión
link = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
)
link.click()

user_input = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.ID, "login_field"))
)
pass_input = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.ID, "password"))
)

# Ingresar las credenciales
user_input.send_keys(gh_user)
pass_input.send_keys(gh_pass)

# Enviar el formulario
pass_input.send_keys(Keys.RETURN)

# Esperar a que el botón del usuario esté presente y hacer clic en él
user_button = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-login='jayounghoyos']"))
)
user_button.click()

# Verificar el nombre del usuario en el menú desplegable
user_name_element = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "span.Button-label"))
)

user_name = user_name_element.text

assert "Juan Andrés Young Hoyos" in user_name
print("Verificación exitosa: El nombre del usuario es correcto.")

# Cerrar el navegador
browser.quit()
