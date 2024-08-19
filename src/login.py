# src/login.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_website(driver, email, password):
    try:
        # Acceder a la página de inicio de sesión
        login_url = "/account/login"
        driver.get(driver.current_url + login_url)

        # Rellenar campos de inicio de sesión
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        
        # Hacer clic en el botón de inicio de sesión
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        print("Inicio de sesión exitoso.")
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")

def create_account(driver, full_name, email, password):
    try:
        # Acceder a la página de registro
        register_url = "/account/register"
        driver.get(driver.current_url + register_url)

        # Rellenar campos de registro
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "full_name"))).send_keys(full_name)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        
        # Hacer clic en el botón de registro
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        print("Cuenta creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la cuenta: {e}")
