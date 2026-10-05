# Pruebas automatizadas sobre saucedemo.com

import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import realizar_login, esperar_elemento_visible, TIEMPO_ESPERA

logger = logging.getLogger(__name__)


# 1. Login
def test_login_exitoso(driver):
    # Un usuario válido inicia sesión y es redirigido al inventario
    realizar_login(driver)

    # Espera explícita: la URL debe cambiar a /inventory.html
    WebDriverWait(driver, TIEMPO_ESPERA).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

    # Validar título de la pestaña y encabezado
    assert driver.title == "Swag Labs", f"Título inesperado: {driver.title}"
    encabezado = esperar_elemento_visible(driver, (By.CSS_SELECTOR, ".title"))
    assert encabezado.text == "Products", f"Encabezado inesperado: {encabezado.text}"

    logger.info("Login exitoso")


# 2. Catálogo
def test_titulo_inventario(driver_logueado):
    # El título de la página de inventario es el correcto
    encabezado = esperar_elemento_visible(driver_logueado, (By.CSS_SELECTOR, ".title"))
    assert encabezado.text == "Products"
    logger.info("Título del inventario verificado")


def test_productos_visibles(driver_logueado):
    # Hay productos visibles y se muestra nombre/precio del primero, al menos un producto tiene que estar visible
    esperar_elemento_visible(driver_logueado, (By.CLASS_NAME, "inventory_item"))
    productos = driver_logueado.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No hay productos visibles"

    # Obtener nombre y precio del primer producto
    primer_producto = productos[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre != "", "El primer producto no tiene nombre"
    assert precio.startswith("$"), f"Precio con formato inesperado: {precio}"

    logger.info(f"Cantidad de productos: {len(productos)}")
    logger.info(f"Primer producto: {nombre} - {precio}")
    print(f"Primer producto: {nombre} - {precio}")


def test_elementos_interfaz(driver_logueado):
    # Menú, filtro y carrito están presentes, espera del menú hamburguesa (localizado por ID)
    menu = esperar_elemento_visible(driver_logueado, (By.ID, "react-burger-menu-btn"))
    # Filtro de ordenamiento y carrito (localizados por CLASS_NAME)
    filtro = driver_logueado.find_element(By.CLASS_NAME, "product_sort_container")
    carrito = driver_logueado.find_element(By.CLASS_NAME, "shopping_cart_link")

    assert menu.is_displayed(), "El menú no está visible"
    assert filtro.is_displayed(), "El filtro no está visible"
    assert carrito.is_displayed(), "El carrito no está visible"

    logger.info("Elementos de la interfaz presentes")


# 3. Carrito
def test_agregar_producto_al_carrito(driver_logueado):
    # Agregar un producto incrementa el contador y aparece en el carrito
    esperar_elemento_visible(driver_logueado, (By.CLASS_NAME, "inventory_item"))

    # Guardar el nombre del primer producto para compararlo después
    primer_producto = driver_logueado.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre_esperado = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Clic en "Add to cart" del primer producto
    primer_producto.find_element(By.CSS_SELECTOR, "button[data-test^='add-to-cart']").click()

    # Espera explícita del badge del carrito y validación del contador
    badge = esperar_elemento_visible(driver_logueado, (By.CLASS_NAME, "shopping_cart_badge"))
    assert badge.text == "1", f"El contador debería ser 1, pero es {badge.text}"

    # Navegar al carrito
    driver_logueado.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver_logueado, TIEMPO_ESPERA).until(EC.url_contains("/cart.html"))

    # Comprobar que el producto agregado aparece en el carrito
    item = esperar_elemento_visible(driver_logueado, (By.CLASS_NAME, "cart_item"))
    nombre_en_carrito = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_en_carrito == nombre_esperado, (
        f"Se esperaba '{nombre_esperado}' en el carrito, pero aparece '{nombre_en_carrito}'"
    )

    logger.info(f"'{nombre_esperado}' agregado y visible en el carrito")
    print("Test OK")