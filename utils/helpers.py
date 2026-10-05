#Funciones auxiliares para las pruebas automatizadas de saucedemo.com

import os

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


def crear_driver():
    #Configura y devuelve una instancia nueva de Chrome WebDriver
    opciones = Options()
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")
    opciones.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=opciones)