# Pruebas automatizadas sobre saucedemo.com

import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import realizar_login, esperar_elemento_visible, TIEMPO_ESPERA

logger = logging.getLogger(__name__)


# 1. Login
def test_login_exitoso(driver):
    """Un usuario válido inicia sesión y es redirigido al inventario."""
    realizar_login(driver)

    # Espera explícita: la URL debe cambiar a /inventory.html
    WebDriverWait(driver, TIEMPO_ESPERA).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

    # Validar título de la pestaña y encabezado
    assert driver.title == "Swag Labs", f"Título inesperado: {driver.title}"
    encabezado = esperar_elemento_visible(driver, (By.CSS_SELECTOR, ".title"))
    assert encabezado.text == "Products", f"Encabezado inesperado: {encabezado.text}"

    logger.info("Login exitoso")