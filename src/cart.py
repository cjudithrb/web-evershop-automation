from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def navigate_to_women_section(driver):
    """
    Navega a la sección 'Women' en la página web.
    
    :param driver: La instancia del navegador controlada por Selenium.
    """
    try:
        women_section_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/women']"))
        )
        women_section_link.click()
    except TimeoutException:
        print("Timeout al intentar encontrar el enlace a la sección 'Women'.")
    except Exception as e:
        print(f"Error al navegar a la sección 'Women': {e}")

def add_products_to_cart(driver, products):
    """
    Agrega productos al carrito de compras en función de una lista de diccionarios de productos.

    :param driver: La instancia del navegador controlada por Selenium.
    :param products: Una lista de diccionarios con los detalles de los productos.
    """
    navigate_to_women_section(driver)  # Navegar a la sección "Women"

    for product in products:
        try:
            # Localizar el producto por nombre
            product_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f"//span[text()='{product['name']}']"))
            )
            
            # Hacer clic en el producto para ir a la página de detalles del producto
            product_element.click()

            # Seleccionar el color
            color_xpath = f"//a[text()='{product['color']}']"
            color_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, color_xpath))
            )
            color_element.click()
            
            # Seleccionar la talla
            size_xpath = f"//a[text()='{product['size']}']"
            size_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, size_xpath))
            )
            size_element.click()

            # Establecer la cantidad
            qty_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='qty']"))
            )
            qty_input.clear()
            qty_input.send_keys(str(product['qty']))

            # Hacer clic en el botón "ADD TO CART"
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(span/text(), 'ADD TO CART')]"))
            )
            add_to_cart_button.click()

            # Regresar a la lista de productos después de añadir al carrito
            #driver.back()
            navigate_to_women_section(driver)

            print(f"Producto '{product['name']}' añadido al carrito con éxito.")

        except TimeoutException:
            print(f"Timeout al intentar encontrar el producto '{product['name']}' o algún elemento relacionado.")
        except Exception as e:
            print(f"Error al agregar el producto '{product['name']}' al carrito: {e}")
