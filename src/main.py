# src/main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from login import login_to_website, create_account
#from cart import add_products_to_cart
#from checkout import complete_checkout

def setup_browser():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)
    chrome_options.add_argument("--disable-gpu")  # Deshabilitar GPU
    service = Service(executable_path="/drivers/chromedriver.exe")  # Ajusta la ruta si es necesario
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def main():
    driver = setup_browser()
    
    try:
        # Acceder a la página de inicio
        driver.get("https://demo.evershop.io/")
        
        # Crear una cuenta
        #create_account(driver, "Judith", "cjudithrb.shop@gmail.com", "123456")
        
        # Iniciar sesión
        login_to_website(driver, "cjudithrb.shop@gmail.com", "123456")
        
        # Agregar productos al carrito
        #add_products_to_cart(driver, 3)
        
        # Completar el proceso de pago
        #complete_checkout(driver)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
