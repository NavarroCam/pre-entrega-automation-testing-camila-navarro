#Funciones auxiliares para las pruebas automatizadas de saucedemo.com

import os

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Datos del sitio bajo prueba
URL_BASE = "https://www.saucedemo.com/"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"

# Tiempo máximo (en segundos) de las esperas explícitas
TIEMPO_ESPERA = 10

# Carpeta donde se guardan las capturas de pantalla (reports/capturas)
CARPETA_CAPTURAS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports", "capturas"
)


def crear_driver():
    #Configura y devuelve una instancia nueva de Chrome WebDriver
    opciones = Options()
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")
    opciones.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=opciones)


def esperar_elemento_visible(driver, localizador):
    """Espera explícitamente a que un elemento sea visible y lo devuelve."""
    return WebDriverWait(driver, TIEMPO_ESPERA).until(
        EC.visibility_of_element_located(localizador)
    )


def realizar_login(driver, usuario=USUARIO_VALIDO, password=PASSWORD_VALIDO):
    #Abre saucedemo.com e inicia sesión con las credenciales indicadas
    driver.get(URL_BASE)

    # Espera explícita: el formulario de login tiene que estar visible
    campo_usuario = esperar_elemento_visible(driver, (By.ID, "user-name"))
    campo_usuario.clear()
    campo_usuario.send_keys(usuario)

    # Localización por NAME para la contraseña
    campo_password = driver.find_element(By.NAME, "password")
    campo_password.clear()
    campo_password.send_keys(password)

    # Localización por CSS para el botón de login
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


def tomar_captura(driver, nombre_test):
    # Guarda una captura de pantalla en reports/capturas y devuelve la ruta
    os.makedirs(CARPETA_CAPTURAS, exist_ok=True)
    marca_tiempo = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = os.path.join(CARPETA_CAPTURAS, f"{nombre_test}_{marca_tiempo}.png")
    driver.save_screenshot(ruta)
    return ruta