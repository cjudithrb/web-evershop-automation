from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def complete_checkout(driver):
    """
    Completa el proceso de compra en la página web.

    :param driver: La instancia del navegador controlada por Selenium.
    """
    try:
        # Navegar al carrito de compras
        print("Buscando el icono del carrito...")
        mini_cart_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='mini-cart-icon']"))
        )
        mini_cart_icon.click()

        # Hacer clic en el botón de 'CHECKOUT'
        print("Buscando el botón de checkout...")
        checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='button primary' and contains(@href, '/checkout')]"))
        )
        checkout_button.click()

        # Intentar ingresar el correo electrónico
        try:
            print("Buscando el campo de correo electrónico...")
            email_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='email']"))
            )
            email_input.send_keys("cjudithrb.shop@gmail.com")
        except TimeoutException:
            print("El campo de correo electrónico no se encontró. Continuando con el siguiente paso.")

        try:
            # Hacer clic en 'Continue to shipping'
            print("Buscando el botón 'Continue to shipping'...")
            continue_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='button primary' and contains(text(), 'Continue to shipping')]"))
            )
            continue_button.click()
        except TimeoutException:
            print("El boton no se encontró. Continuando con el siguiente paso.")

        print("Proceso de checkout iniciado con éxito.")
    except Exception as e:
        print(f"Error: {e}")

def complete_shipping_form(driver):
    """
    Completa el formulario de dirección de envío en la página de checkout.

    :param driver: La instancia del navegador controlada por Selenium.
    """
    complete_checkout(driver)
    # Ingresar el nombre completo
    full_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "address[full_name]"))
    )
    full_name_input.clear()
    full_name_input.send_keys("Judith rojas")

    # Ingresar el número de teléfono
    telephone_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "address[telephone]"))
    )
    telephone_input.clear()
    telephone_input.send_keys("912345678")

    # Ingresar la dirección
    address_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "address[address_1]"))
    )
    address_input.clear()
    address_input.send_keys("Av. Petit Thouars 5273, Miraflores, Lima.")

    # Ingresar la ciudad
    city_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "address[city]"))
    )
    city_input.clear()
    city_input.send_keys("Lima")

    # Seleccionar el país
    country_select = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "address[country]"))
    )
    country_select.send_keys("United States")  # Puedes cambiar a otro país según sea necesario

    # Seleccionar la provincia/estado
    province_select = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "address[province]"))
    )
    province_select.send_keys("California")  # Cambia a la provincia/estado adecuado

    # Ingresar el código postal
    postcode_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "address[postcode]"))
    )
    postcode_input.clear()
    postcode_input.send_keys("15404")  # Reemplaza "codigo zip" con el código postal real

    print("Esperando a que la caja de métodos de envío sea visible...")
    time.sleep(5)  # Espera fija de 5 segundos para permitir que los métodos de envío se carguen

    # Seleccionar el método de envío
    try:
        print("Buscando el método de envío 'Standard Delivery'...")
        # Seleccionar el método de envío "Standard Delivery"
        standard_delivery = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Standard Delivery - $5.00')]/preceding-sibling::input[@type='radio']"))
        )
        standard_delivery.click()
        print("Método de envío 'Standard Delivery' seleccionado.")
    except TimeoutException:
        print("No se encontró el método de envío 'Standard Delivery'. Intentando con 'Express Delivery'.")
        try:
            express_delivery = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Express Delivery - $15.00')]/preceding-sibling::input[@type='radio']"))
            )
            express_delivery.click()
            print("Método de envío 'Express Delivery' seleccionado.")
        except TimeoutException:
            print("No se encontraron los métodos de envío. Asegúrate de que los elementos estén presentes en la página.")
            return

    # Hacer clic en 'Continue to payment'
    continue_to_payment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='button primary']"))
    )
    continue_to_payment_button.click()

    print("Formulario de dirección de envío completado con éxito.")
